import re
from typing import List, Optional
from talon import Context, Module, actions
ctx = Context()
ctx.matches = '\napp: jetbrains\n'
mod = Module()
list_python_keywords = {'false': 'False', 'none': 'None', 'true': 'True', 'and': 'and', 'as': 'as', 'assert': 'assert', 'async': 'async', 'await': 'await', 'break': 'break', 'class': 'class', 'continue': 'continue', 'define': 'def', 'elif': 'elif', 'else': 'else', 'except': 'except', 'finally': 'finally', 'for': 'for', 'from': 'from', 'global': 'global', 'if': 'if', 'import': 'import', 'in': 'in', 'is': 'is', 'lambda': 'lambda', 'nonlocal': 'nonlocal', 'not': 'not', 'or': 'or', 'pass': 'pass', 'raise': 'raise', 'return': 'return', 'try': 'try', 'while': 'while', 'with': 'with', 'yield': 'yield', 'telephone': 'THIS IS TEST'}
mod.list('vocabulary', desc='additional vocabulary words')
automatically_generated_mapping = {'import': 'import', 'bisect': 'bisect', 'somerandomfunction': 'someRandomFunction', 'local': 'local', 'local variable': 'local_variable', 'return': 'return', 'smallestequivalentstring': 'smallestEquivalentString', 'basestr': 'baseStr', 'mappings': 'mappings', 'insort': '.insort', 'continue': 'continue', 'while': 'while', 'parker': '"parker"', 'morris': '"morris"', 'parser': '"parser"', 'print': 'print'}
mod.list('python_keywords', desc='Automatically extracted key words from python files')
ctx.lists['self.python_keywords'] = dict(automatically_generated_mapping, **list_python_keywords)
ctx.lists['user.vocabulary'] = dict(automatically_generated_mapping, **list_python_keywords)

@mod.capture(rule='{self.python_keywords}+')
def python_keywords(m) -> str:
    return ''.join(m.python_keywords_list)

@mod.capture(rule='add for <phrase>+ in {user.vocabulary}')
def add_for_loop(m) -> str:
    return 'for' + '_'.join(m.phrase_list) + ' in ' + m.vocabulary + ':'

@mod.action_class
class Actions:

    def dictation_peek_left() -> Optional[str]:
        """
        Tries to get some text before the cursor, ideally a word or two, for the
        purpose of auto-spacing & -capitalization. Results are not guaranteed;
        dictation_peek_left() may return None to indicate no information. (Note
        that returning the empty string "" indicates there is nothing before
        cursor, ie. we are at the beginning of the document.)

        dictation_peek_left() is intended for use before inserting text, so it
        may delete any currently selected text.
        """
        actions.insert(' ')
        actions.edit.extend_word_left()
        actions.edit.extend_word_left()
        text = actions.edit.selected_text()
        actions.edit.right()
        actions.key('backspace')
        return text[:-1]

    def str_list_to_snake(text: List[str]):
        """Inserts a list of keys"""
        return '_'.join(text).replace(' ', '_').lower()

    def context_awareinsert(text: str):
        """Inserts a list of keys"""
        left = actions.user.dictation_peek_left()
        left_most = left[-1]
        print(left)
        if left_most in 'class':
            actions.insert(' ')
            words = text.split(' ')
            text = words[0] + ''.join((w.title() for w in words[1:]))
            actions.insert(text)
        elif left_most in list_python_keywords:
            actions.insert(' ')
            actions.insert(text.replace(' ', '_').lower())
        elif re.match('[A-Za-z0-9]', left_most):
            actions.insert('.')
            actions.insert(text.replace(' ', '_').lower())
        elif re.match('/S+', left_most):
            actions.insert(' ')
            actions.insert(text.replace(' ', '_').lower())
        else:
            actions.insert(text)