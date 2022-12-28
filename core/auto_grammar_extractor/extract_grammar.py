#!/usr/bin/python3.9
import ast
import re
import sys
from _ast import Expression, Assign
from pathlib import Path
from typing import List, Any
import keyword


class TreeNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.count = 1
        self.glue = self.isGlue()

    def add_child(self, child):
        if child not in self.children:
            self.children[child] = TreeNode(child, self)
        else:
            self.children[child].increment_count()


    def increment_count(self):
        self.count += 1

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_count(self):
        return self.count

    def __str__(self):
        return f"{self.name} {self.count}"

    def __hash__(self):
        return hash(self.name)

    def isGlue(self) -> bool:
        pattern = r'(\.|->)'
        match = re.fullmatch(pattern, self.name)
        if match:
            self.setName(re.sub(pattern, '', self.name))
            return match.group(1)
        else:
            return ""

    def setName(self, name):
        self.name = name


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
    command = re.sub(r'[._]', ' ', command)
    command = re.sub(r'[:"\']', '', command)
    return command


def tokenize(line):
    org=line
    # remove comments
    line = re.sub(r'#.*', '', line)
    line = re.sub(r'\n', '', line)
    # Remove anything that is in between any kind of parentheses
    #line = re.sub(r'(\(.*\)|\[.*\]|{.*})', '', line)
    #line = re.sub(r'[\)>}\],\[\(]', '', line)
    # Split the incoming string on white spaces unless they are in quotes
    str_tokens = re.findall(r'(".+?"|\'.+?\')+', line)
    tokens = []
    for token in str_tokens:
        if len(token) < 10 and len(token.split()) < 2:
            tokens.append(token)
        line=line.replace(token, '')
    tokens.extend([token[0] for token in re.findall(r'((\.|->)?[A-Za-z_][A-Za-z_0-9]+)', line)])

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
                    nodes[token] = (token,0)
                else:
                    nodes[token] = (token,nodes[token][1]+1)

    #cleaned_name=[idx for node,idx in nodes.items()]
    nodes_count_same_name={}
    for idx,node in enumerate(nodes.values()):
        clean_name=re.sub(r'[\.\'"]', '', node[0])
        clean_name = re.sub(r'[_]', ' ', clean_name)
        clean_name= clean_name.strip()
        clean_name=clean_name.lower()
        if clean_name not in nodes_count_same_name:
            nodes_count_same_name[clean_name]=[(node[0],node[1],idx)]
        else:
            nodes_count_same_name[clean_name].append((node[0],node[1],idx))

    command_list = {}
    for key, node in nodes_count_same_name.items():
        if len(key)< 3 or len(key) > 15:
            continue
        node.sort(key=lambda x:x[1],reverse=True)
        mapping_string=node[0][0]
        mapping_string=re.sub(r'[\.\'"]', '', mapping_string)
        command_list[key]=mapping_string
        split_key=key.split()
        if len(split_key)>1:
            command_list[split_key[0]]=split_key[0]

        i=3

    return command_list


class Replace(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = mapping

    def visit_Assign(self, node: Assign) -> Any:
        print(ast.dump(node))
        if isinstance(node.targets[0], ast.Name) and \
                node.targets[0].id == 'automatically_generated_mapping':
            replacement = ast.Dict(keys=[ast.Str(key) for key in talon_dictionary.keys()],
                                   values=[ast.Str(value) for value in talon_dictionary.values()])
            node.value = ast.copy_location(replacement, node.value)
        return node

    def visit_Expression(self, node: Expression) -> Any:
        print(ast.dump(node))
        return super().visit_Expression(node)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        filepath =  Path(sys.argv[1]).expanduser()
    else:  # filepath = Path('~/.bash_history').expanduser()
        filepath = Path('~/PycharmProjects/raat-search/search_server/fkie_search/__main__.py').expanduser()
        # filepath = Path('~/PycharmProjects/raat-search/search_server/fkie_search/core/ttt.py').expanduser()

    talon_dictionary = extract_from_file(filepath)

    with open(Path('~/.talon/user/core/auto_grammar_extractor/auto_python.py').expanduser(), 'r') as f:
        parsed = ast.parse(f.read())
        parsed = Replace(talon_dictionary).visit(parsed)
    with open(Path('~/.talon/user/core/auto_grammar_extractor/auto_python.py').expanduser(), 'w') as f:
        f.write(ast.unparse(parsed))


