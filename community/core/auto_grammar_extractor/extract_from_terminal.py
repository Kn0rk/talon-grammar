#!/usr/bin/python3.8




import os
import re
def split_line_with_quotes(line):
    tokens = []
    strings = []
    pattern = r'"([^"]+)"'
    matches = re.findall(pattern, line)
    line = re.sub(pattern, '', line)
    strings.extend(matches)
    pattern = r"'([^']+)'"
    matches = re.findall(pattern, line)
    line = re.sub(pattern, '', line)
    strings.extend(matches)

    tokens.extend(line.split())
    
    
    return tokens, strings

file_name = "/home/jan/.bash_history"
file_contents = None
with open(file_name, "r") as f:
    file_contents = f.readlines()

# regex to Remove new line character if it exists
regex = re.compile(r"(\n(\r)?)$")
file_contents = [regex.sub("", line) for line in file_contents]
# Remove comments
file_contents = [re.sub(r'#.*', '', line) for line in file_contents]
paths = []
commands = set()
for line in file_contents:
    # Split on whitespace unless it's within quotes
    tokens, strings = split_line_with_quotes(line)
    if len(tokens) == 0:
        continue
    current_command = tokens[0]
    contains_special = bool(re.search(r'[\x00-\x7F]',current_command))
    is_empty = len(current_command) == 0 or len(current_command)    >  50

    if is_empty \
            or not os.system(f"command -v {current_command}") == 0:
        continue
    commands.add(tokens[0])

    for token in tokens[1:]:
        # Split on whitespace unless it's within quotes
        
        token= token.strip()
        is_path = re.compile(r"^(./|/|~|.//|\W/)")
        is_option = re.compile(r"^(-|--)[a-zA-Z]")
        irrelevant = re.compile(r"^(..)|^[a-zA-Z0-9]+")
        is_url = re.compile(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")
        if is_path.match(token):
            paths.append(token)
        elif is_option.match(token):
            pass
        # elif irrelevant.match(token):
            # pass
        else:
            current_command += " "+token 
        if len(current_command) < 15 and len(current_command) > 3:
            commands.add(current_command.strip())
            


variable = 1


