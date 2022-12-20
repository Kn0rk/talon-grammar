import re
from pathlib import Path
from typing import List


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

def add_tokens_to_node(node:TreeNode,tokens:List[str]):
    if len(tokens) == 0:
        return


    token = tokens.pop(0)
    node.add_child(token)
    add_tokens_to_node(node.children[token],tokens)

def python_visitor(node:TreeNode, vocabulary, depth=0, max_depth=10):
    command=None
    if node.get_count()>0:
        command =node.get_name()

    return command

def generic_visitor(node:TreeNode, vocabulary, visitor_function,depth=0, max_depth=10):
    if depth > max_depth:
        return
    command=visitor_function(node,vocabulary)
    if command:
        parent = node.get_parent()
        while parent:
            command = parent.get_name() + " " + command
            parent = parent.get_parent()
        vocabulary.append(command)
    for child in node.get_children().values():
        extract_bash_commands(child, vocabulary, depth + 1)

def extract_bash_commands(node:TreeNode, vocabulary, depth=0, max_depth=10):
    if depth > max_depth:
        return
    if node.get_count()>3:
        command =node.get_name()



        parent= node.get_parent()
        while parent:
            command= parent.get_name() + " " + command
            parent = parent.get_parent()
        vocabulary.append(command)
    for child in node.get_children().values():
        extract_bash_commands(child, vocabulary, depth + 1)

def extract_from_file(filepath:Path):
    nodes = {}
    with open(filepath,'r') as f:
        lines = f.readlines()
        for line in lines:
            # split each line into tokens
            tokens = line.split()
            if len(tokens) == 0:
                continue
            if tokens[0] in nodes:
                nodes[tokens[0]].increment_count()
            else:
                nodes[tokens[0]] = TreeNode(tokens[0])
            if len(tokens[1:]) > 1:
                add_tokens_to_node(nodes[tokens[0]],tokens[1:])
            else:
                nodes[tokens[0]].increment_end_count()
    command_list = []
    for node in nodes.values():
        generic_visitor(node, command_list,python_visitor)
    #
    return nodes

if __name__ == '__main__':
    # get the path to the file
    filepath = Path('~/.bash_history').expanduser()
    filepath = Path('~/PycharmProjects/raat-search/search_server/fkie_search/core/interface.py').expanduser()
    extract_from_file(filepath)