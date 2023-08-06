import re
from itertools import chain


class LexerNode:
    def __init__(self, name, prefix=None, suffix=None):
        self.name = name
        self.prefix = prefix
        self.suffix = suffix
        # self.children = []
        # self.parent = parent
        # self.name = None
        # self.prefix = None
        # self.suffix = None
        # prefix_pattern='|'.join(map(re.escape,config.prefix))
        # first_prefix_pattern=f'^({prefix_pattern})(.*)'
        # next_prefix_pattern = f'(.*?)({prefix_pattern})'
        #
        #
        # prefix_match=re.match(first_prefix_pattern,raw_input)
        # if prefix_match:
        #     self.prefix=prefix_match.group(1)
        #     self.name=prefix_match.group(2)
        #     raw_input=raw_input[prefix_match.end(2):]
        #
        # next_prefix_match=re.match(next_prefix_pattern,raw_input)
        # if next_prefix_match:
        #     self.name=next_prefix_match.group(1)
        #     raw_input=raw_input[next_prefix_match.end(1):]
        #     if len(raw_input)>0:
        #         self.children.append(LexerNode(raw_input, config, self))
        #
        # suffix_pattern='|'.join(map(re.escape,config.suffix))
        # suffix_pattern=f'(.*?)({suffix_pattern})'
        # suffix_match=re.match(suffix_pattern,raw_input)
        # if len(self.children)==0 and suffix_match:
        #     self.name=suffix_match.group(1)
        #     self.suffix=suffix_match.group(2)
        #     raw_input=raw_input[suffix_match.end(2):]





    def _issingle(self):
        yield self

    def __iter__(self):
        yield self
        yield from self.children

    def __str__(self):
        return f"{self.prefix} {self.name}  {self.suffix}"

    def __repr__(self):
        return f"<{self.prefix} {self.name}  {self.suffix}>"


class PythonLexerConfig:
    def __init__(self):
        self.line_comment = ["#"]
        self.block_comment = ['"""', "'''"]
        self.delimiters = [" ", "\t", "\n", "\r", ","]
        self.assignments = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "**=", "//="]
        self.keywords = [
            "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "False", "finally",
            "for", "from", "global", "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"
        ]
        self.prefix = [
            "."
        ]
        self.suffix_start = [
            "(",  "[",  "{", "<",
            ]
        self.suffix_end = [
            ")",  "]",  "}", ">",
            ]


            #",", ".", ":", ";", "@", "=", "->", "+", "-", "*", "/", "%", "&", "|", "^",
        #     "~", "<", ">", "!", "==", "<=", ">=", "(", ")", "[", "]", "{", "}", ",", ":", ".", "=", ";", "+=", "-=",
        #     "*=", "@=", "/=", "%=", "&=", "|=", "^=", ">>=", "<<=", "**=", "//=", "->", "..."," ",
        # ]
        self.string_delimiters = ["'", '"']
        self.string_prefix = ["r", "u", "f", "b"]
        self.comment_delimiters = ["#", "'''", '"""']
        self.ignored_tokens = [" ", "\t", " "]


def parse(file):
    config=PythonLexerConfig()


    pattern_block_comment = '|'.join([ com+r"(.*?)"+com for com in map(re.escape, config.block_comment)])
    file=re.sub(pattern_block_comment, '', file, flags=re.DOTALL)

    pattern_string_prefix = "|".join(map(re.escape, config.string_delimiters))
    pattern_string = '|'.join([com + r"(.*?)" + com for com in map(re.escape, config.string_delimiters)])
    all_strings = []
    all_matches = re.findall(pattern_string, file, flags=re.DOTALL)
    for match in all_matches:
        all_strings.append(match[0])
    file = re.sub(pattern_string, '', file, flags=re.DOTALL)

    pattern_line_comment = '|'.join(map(re.escape, config.line_comment))
    file=re.sub(pattern_line_comment+r".*", '', file)
    pattern= '|'.join(map(re.escape,config.delimiters))

    pattern_delimiter= '|'.join(map(re.escape,config.delimiters))
    pattern_assignment = '|'.join(map(re.escape,config.assignments))
    pattern_delimiter = f"({pattern_delimiter})+|({pattern_assignment})"


    pattern_string_prefix = '|'.join([ f'({com})'+r"(.*?)" for com in map(re.escape, config.prefix)])
    nodes= []

    for line in file.splitlines():
        line=re.split(pattern_delimiter,  line)
        for token in line:
            if not token or len(token.strip())==0:
                continue

            prefix_pattern = '|'.join(map(re.escape, config.prefix))
            suffix_pattern_start = '|'.join(map(re.escape, config.suffix_start))
            suffix_pattern_end = '|'.join(map(re.escape, config.suffix_end))
#            prefix_pattern = f'({prefix_pattern})'

            start=0
            prefix=''
            suffix=''
            for index, character in enumerate(token):
                section=token[start:index+1]
                match= re.search(prefix_pattern,section)
                if match:
                    nodes.append(LexerNode(token[start:index],prefix,suffix))
                    prefix=match.group(0)
                    suffix=''
                    start=index+1
                match = re.search(suffix_pattern_start, section)
                if match:
                    nodes.append(LexerNode(token[start:index], prefix, match.group(0)))
                    prefix=''
                    suffix=''
                    start=index+1

                match = re.search(suffix_pattern_end, section)
                if match:
                    nodes.append(LexerNode(token[start:match.start(0)], prefix, suffix ))
                    prefix=''
                    suffix=''
                    start=index+1
            nodes.append(LexerNode(token[start:],prefix,suffix))

                



    print(nodes)



if __name__ == '__main__':
    with open("extract_grammar.py","r") as f:
        parse(f.read())