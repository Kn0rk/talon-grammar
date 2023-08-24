#!/usr/bin/python3.9
"""
 You can call this module from the commandline
 and you should provide the path to file you wish
 to extract the or vocabulary from as the first argument.

   this script currently only supports python files.

 if you are using jetbrains products you can automatically update se vocabulary by adding
  a file watcher to execute this script on a change to a python file.

"""
import argparse
import ast
import enum
import re
import sys
from _ast import Expression, Assign
from pathlib import Path
from typing import List, Any, Set, Union, Dict
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

#
# def add_tokens_to_node(node: TreeNode, tokens: List[str]):
#     if len(tokens) == 0:
#         return
#
#     token = tokens.pop(0)
#     node.add_child(token)
#     add_tokens_to_node(node.children[token], tokens)
#
#
# def python_visitor(current_node: TreeNode):
#     command = None
#     if current_node.get_count() > 0:
#         command = current_node.get_name()
#         contains_any_alphabetic_characters = re.findall('[A-Za-z]', command)
#         if len(contains_any_alphabetic_characters) == 0:
#             return None
#         # pattern that checks if they are matching parentheses
#         # pattern= re.compile(r'\(.*\)')
#         contains_any_alphabetic_characters = re.findall('[^A-Za-z]', command)
#         if len(contains_any_alphabetic_characters) > 3:
#             return None
#
#         if len(command) < 3 or len(command) > 15:
#             return None
#
#     return command
#
#
# def generic_visitor(current_node: TreeNode, vocabulary, visitor_function, depth=0, max_depth=10):
#     if depth > max_depth:
#         return
#
#     command = visitor_function(current_node)
#     parent = current_node.get_parent()
#     while parent and command is not None:
#         parent_command = visitor_function(parent)
#         if parent_command:
#             command = parent_command + " " + command
#             parent = parent.get_parent()
#     if command:
#         vocabulary.append(command)
#         for child in current_node.get_children().values():
#             generic_visitor(child, vocabulary, visitor_function, depth + 1)
#
#
# def removed_children_that_are_in_root(root: List[TreeNode]):
#     root_copy = root.copy()
#     for node in root_copy.values():
#         node_copy = node.get_children().copy()
#         for child in node_copy.values():
#             name = re.sub(r'[:/.,=><$@#]', '', child.get_name())
#             if name in root:
#                 root[node.get_name()].get_children().pop(child.get_name())
#
#
# def clean_command(command):
#     command = re.sub(r'[._]', ' ', command)
#     command = re.sub(r'[:"\']', '', command)
#     return command


def python_tokenizer(line:str) -> List[str]:
    # remove comments
    line = re.sub(r'#.*', '', line)
    line = re.sub(r'\n', '', line)

    # Split the incoming string on white spaces unless they are in quotes
    str_tokens = re.findall(r'(".+?"|\'.+?\')+', line)
    tokens = []
    for token in str_tokens:
        if len(token) < 10 and len(token.split()) < 2:
            tokens.append(token)
        line=line.replace(token, '')
        line=line.strip()
    tokens.extend([token[0] for token in re.findall(r'((\.|->)?[A-Za-z_][A-Za-z_0-9]+)', line)])

    return tokens

def terminal_tokenizer(line:str) -> List[str]:
    # remove comments
    line = re.sub(r'#.*', '', line)
    line = re.sub(r'\n', '', line)
    line = line.strip()
    if len(line) < 3 or len(line) > 45:
       return []
    return [line]

def extract_from_file(filepath: Path,
                      line_tokenizer)-> Dict[Any, Union[str, Any]]:
    # (Raw tokenized input, frequency)
    nodes = {}
    # Read and tokenize the file
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # split each line into tokens
            tokens = line_tokenizer(line)
            if len(tokens) == 0:
                continue
            for token in tokens:

                if token not in nodes:
                    nodes[token] = (token,0)
                else:
                    nodes[token] = (token,nodes[token][1]+1)


    spoken_to_insert={}

    # Split tokens on word boundaries such as _ for camel case or lower/upper case for camel
    # E.g. for the token "getMyName"
    # get -> get
    # get my -> getMy
    # get my name -> getMyName
    for idx,node in enumerate(nodes.values()):
        clean_name=node[0]

        # todo: detect ands handle paths differently
        raw=clean_name
        # sup tokenizes on the following characters
        clean_name= re.sub(r'(_|-|\[|\.)',' ', clean_name)
        clean_name=clean_name.lower()
        # split on camel cases without changing the indices of the strings
        clean_names=[(m.group(),(m.start(),m.end())) for m in re.finditer(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))|[a-z]+', clean_name)]

        for split in clean_names:
            assert len(clean_name)==len(raw)
            spoken=clean_name[0:split[1][1]+1]
            result=raw[0:split[1][1]+1]
            unwanted_characters = re.findall(r'[^a-zA-Z ]+', spoken)
            spoken=re.sub(r'[^a-zA-Z ]', '', spoken)
            longest=0
            for character in unwanted_characters:
                if len(character) > longest:
                    longest=len(character)
            if longest > 1:
                break
            spoken=spoken.strip()
            if clean_name not in spoken_to_insert:
                spoken_to_insert[spoken]=[(result,node[1],idx)]
            else:
                spoken_to_insert[spoken].append((result,node[1],idx))


    command_list = {}
    for key, node in spoken_to_insert.items():
        if len(key)< 5 or len(key) > 35:
            continue
        # Sort the list of tokens with the same clean name
        node.sort(key=lambda x:x[1],reverse=True)
        # Pick the most frequent realisation of the clean name
        mapping_string=node[0][0]

        command_list[key]=mapping_string
        split_key=key.split()
        if len(split_key)>1:
            command_list[split_key[0]]=split_key[0]

    return command_list


class Replace(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = mapping

    def visit_Assign(self, node: Assign) -> Any:
        print(ast.dump(node))
        if isinstance(node.targets[0], ast.Name) and \
                node.targets[0].id == 'automatically_generated_mapping':
            replacement = ast.Dict(keys=[ast.Str(key) for key in self.mapping.keys()],
                                   values=[ast.Str(value) for value in self.mapping.values()])
            node.value = ast.copy_location(replacement, node.value)
        return node

    def visit_Expression(self, node: Expression) -> Any:
        print(ast.dump(node))
        return super().visit_Expression(node)



class SupportedTypes(enum.Enum):
    python = 'python'
    terminal = 'terminal'
    auto = 'auto'

def main(file:Path,type:SupportedTypes):
    file=file.expanduser()
    if not file.expanduser().exists():
        raise FileNotFoundError(f'File {file} does not exist')
    file_type = file.suffix
    if type == SupportedTypes.auto:
        if file_type == '.py':
            file_type = SupportedTypes.python
        else:
            raise Exception(f'Could not determine file type of {file}')
    else:
        file_type = type

    tokenizer_map = {
        SupportedTypes.python: python_tokenizer,
        SupportedTypes.terminal: terminal_tokenizer
        
    }
    talon_dictionary = extract_from_file(file, tokenizer_map[file_type])

    with open(Path(f'~/.talon/user/core/auto_grammar_extractor/auto_{file_type.name}.py').expanduser(), 'r') as f:
        parsed = ast.parse(f.read())
        parsed = Replace(talon_dictionary).visit(parsed)
    with open(Path(f'~/.talon/user/core/auto_grammar_extractor/auto_{file_type.name}.py').expanduser(), 'w') as f:
        f.write(ast.unparse(parsed))

if __name__ == '__main__':
    # parse arguments with argparse
    parser = argparse.ArgumentParser(description='Extracts a list of commands from a python file')
    parser.add_argument('file', type=str, help='The file to extract commands from')
    # optional arguments
    parser.add_argument('-type', type=str, choices=['auto','python','terminal'],nargs= '?', default='auto', help='The file type to extract commands from. This will determine to which automatically generated file the commands will be added to.')

    args = parser.parse_args()
    file = Path(args.file).expanduser()
    main(file,SupportedTypes[args.type])




