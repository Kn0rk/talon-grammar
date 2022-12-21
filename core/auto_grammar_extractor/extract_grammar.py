#!/usr/bin/python3.9
import ast
import re
import sys
from _ast import Expression, Assign
from pathlib import Path
from typing import List, Any


class TreeNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.count = 1
        self.end_count = 0

    def add_child(self, child):
        if child not in self.children:
            self.children[child] = TreeNode(child, self)
        else:
            self.children[child].increment_count()

    def increment_count(self):
        self.count += 1

    def increment_end_count(self):
        self.end_count += 1

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_count(self):
        return self.count

    def get_endcount(self):
        return self.end_count

    def __str__(self):
        return f"{self.name} {self.count}"

    def __hash__(self):
        return hash(self.name)


def add_tokens_to_node(node: TreeNode, tokens: List[str]):
    if len(tokens) == 0:
        return

    token = tokens.pop(0)
    node.add_child(token)
    add_tokens_to_node(node.children[token], tokens)


def python_visitor(current_node: TreeNode):
    command = None
    if current_node.get_count() > 0:
        command = current_node.get_name()
        contains_any_alphabetic_characters = re.findall('[A-Za-z]', command)
        if len(contains_any_alphabetic_characters) == 0:
            return None
        # pattern that checks if they are matching parentheses
        # pattern= re.compile(r'\(.*\)')
        contains_any_alphabetic_characters = re.findall('[^A-Za-z]', command)
        if len(contains_any_alphabetic_characters) > 3:
            return None

        if len(command) < 3 or len(command) > 15:
            return None

    return command


def generic_visitor(current_node: TreeNode, vocabulary, visitor_function, depth=0, max_depth=10):
    if depth > max_depth:
        return

    command = visitor_function(current_node)
    parent = current_node.get_parent()
    while parent and command is not None:
        parent_command = visitor_function(parent)
        if parent_command:
            command = parent_command + " " + command
            parent = parent.get_parent()
    if command:
        vocabulary.append(command)
        for child in current_node.get_children().values():
            generic_visitor(child, vocabulary, visitor_function, depth + 1)


def removed_children_that_are_in_root(root: List[TreeNode]):
    root_copy = root.copy()
    for node in root_copy.values():
        node_copy = node.get_children().copy()
        for child in node_copy.values():
            name = re.sub(r'[:/.,=><$@#]', '', child.get_name())
            if name in root:
                root[node.get_name()].get_children().pop(child.get_name())


def clean_command(command):
    command= re.sub(r'[._]', ' ', command)
    command= re.sub(r'[:"\']', '', command)
    return command


def tokenize(line):
    line=re.sub(r'#.*','', line)
    line = re.sub(r'\n', '', line)
    # Remove anything that is in between any kind of parentheses
    line = re.sub(r'(\(.*\)|\[.*\]|{.*})', '', line)
    line = re.sub(r'[\)>}\],\[\(]','', line)
    #Split the incoming string on white spaces unless they are in quotes
    tokens = re.findall(r'[^ |=|\.\']+|"[^"|\']+"', line)

    return tokens

def extract_from_file(filepath: Path):
    nodes = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # split each line into tokens
            tokens = tokenize(line)
            if len(tokens) == 0:
                continue
            for token in tokens:
                if token not in nodes:
                    nodes[token] = TreeNode(token)
                else:
                    nodes[token].increment_count()
    command_list = []
    removed_children_that_are_in_root(nodes)
    for node in nodes.values():
        generic_visitor(node, command_list, python_visitor)
    #
    command_map={}
    for command in command_list:
        command_map[clean_command(command)]=command
    return command_map


class Replace(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = mapping

    def visit_Assign(self, node: Assign) -> Any:
        print(ast.dump(node))
        if isinstance(node.targets[0], ast.Name) and \
         node.targets[0].id == 'automatically_generated_mapping':

            replacement = ast.Dict(keys=[ast.Str(key) for key in talon_dictionary.keys()],
                                   values=[ast.Str(value) for value in talon_dictionary.values()])
            node.value=ast.copy_location(replacement, node.value)
        return node

    def visit_Expression(self, node: Expression) -> Any:
        print(ast.dump(node))
        return super().visit_Expression(node)


if __name__ == '__main__':
    if  len(sys.argv) ==2:
        filepath=sys.argv[1]
    else:    #filepath = Path('~/.bash_history').expanduser()
        filepath = Path('~/PycharmProjects/raat-search/search_server/fkie_search/__main__.py').expanduser()
        # filepath = Path('~/PycharmProjects/raat-search/search_server/fkie_search/core/ttt.py').expanduser()

    talon_dictionary=extract_from_file(filepath)


    with open(Path('~/.talon/user/core/auto_grammar_extractor/auto_python.py').expanduser(), 'r') as f:
        parsed = ast.parse(f.read())
        parsed=Replace(talon_dictionary).visit(parsed)
    with open(Path('~/.talon/user/core/auto_grammar_extractor/auto_python.py').expanduser(), 'w') as f:
        f.write(ast.unparse(parsed))

    print(talon_dictionary)
