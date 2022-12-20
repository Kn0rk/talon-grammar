import os.path
import sys
from talon import Context, Module, actions, app


mod= Module()
ctx =Context()

'''
Alphabet
'''
default_alphabet = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sun Tiny Uniform Victor Whiskey Xray Yankee Zulu".split(
    " "
)
letters_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = dict(zip(default_alphabet, letters_string))
mod.list("letter", desc="The spoken phonetic alphabet")
ctx.lists["self.letter"] = alphabet

'''
Digits
'''
default_digits = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")
numbers = [str(i) for i in range(20)]
ctx.lists["self.number_key"] = dict(zip(default_digits, numbers))
mod.list("number_key", desc="All number basics")

'''
Function basics
'''
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)
mod.list("function_key", desc="All function basics")
ctx.lists["self.function_key"] = {
    f"function {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


'''
Modifier basics
'''
modifier_keys = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "window": "super",
    "windows": "super",
    #"win": "super",
}
mod.list("modifier_key", desc="All modifier basics")
ctx.lists["self.modifier_key"] = modifier_keys

symbol_key_words = {
    "back tick": "`",
    "grave": "`",
    "comma": ",",
    # Workaround for issue with conformer b-series; see #946
    "coma": ",",
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",

    "dot": ".",
    "point": ".",
    "quote": "'",
    "question": "?",
    "apostrophe": "'",
    "lope": "[",
    "left square": "[",
    "square": "[",
    "rope": "]",
    "right square": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "down score": "_",
    "underscore": "_",
    "paren": "(",
    "leap": "(",
    "left paren": "(",
    "reap": ")",
    "right paren": ")",
    "brace": "{",
    "lake": "{",
    "brack": "{",
    "bracket": "{",
    "rake": "{",
    "r brace": "}",
    "right brace": "}",
    "r brack": "}",
    "r bracket": "}",
    "right bracket": "}",
    "angle": "<",
    "lube": "<",
    "less than": "<",
    "rangle": ">",
    "rupe": ">",
    "right angle": ">",
    "greater than": ">",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "caret": "^",
    "amper": "&",
    "pipe": "|",
    "dubquote": '"',
    "double quote": '"',
    # Currencies
    "dollar": "$",
    "pound": "£",
    "act": "escape",
    "space": "space",
    "insert": "insert",
}
mod.list("symbol_key", desc="All symbols from the keyboard")
ctx.lists["self.symbol_key"] = symbol_key_words

mod.list("movement", desc="All movement basics")
ctx.lists["self.movement"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
    "ending":"end",
    "home":"home",
    "page up": "pageup",
    "page down": "pagedown",
    "wipe": "backspace",
    "slap": "enter",
    "tabby": "tab",
    "delete": "delete",
}

mod.list("compound_movement", desc="All movement basics")
ctx.lists["self.compound_movement"] = {
    "east": "ctrl-right",
    "west": "ctrl-left",
    "bump": "ctrl-delete",
    "pimp": "ctrl-backspace",

}

@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)
@mod.capture(rule="( {self.movement} | {self.compound_movement} | {self.letter})")
def movement(m) -> str:
    "One directional arrow key"
    return m[0]

@mod.capture(rule="[ {self.modifier_key}+ ] (<self.movement> [<self.number_key>] )+")
def modified_movements(m) -> str:
    "One or more arrow basics separated by a space"
    keys=str(m).split()
    mods=None
    key_list=[]
    for key in keys:
        if key in modifier_keys.values():
            mods=mods+"-"+key if mods else key
        elif key in numbers:
            num=int(key)
            key_list.extend([key_list[-1] for i in range(num-1)])
        else:
            if mods:
                key_list.append(mods+"-"+key)
            else:
                key_list.append(key)
    result=" ".join(key_list)
    return result

@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key

@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter

@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key




