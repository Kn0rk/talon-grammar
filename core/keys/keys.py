import os.path
import sys
from talon import Context, Module, actions, app
sys.path.append(os.path.expanduser('~')+"/.talon/user")
from shared_resources import getBasicModule, getBasicContext

mod= getBasicModule()
ctx =getBasicContext()

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
default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
ctx.lists["self.number_key"] = dict(zip(default_digits, numbers))
mod.list("number_key", desc="All number keys")

'''
Function keys
'''
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)
mod.list("function_key", desc="All function keys")
ctx.lists["self.function_key"] = {
    f"function {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


'''
Modifier keys
'''
modifier_keys = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "windows": "super",
}
mod.list("modifier_key", desc="All modifier keys")
ctx.lists["self.modifier_key"] = modifier_keys

punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things

    # Currencies
    "dollar sign": "$",
    "pound sign": "£",
}
mod.list("punctuation", desc="words for inserting punctuation into text")
ctx.lists["self.punctuation"] = punctuation_words

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
}
mod.list("symbol_key", desc="All symbols from the keyboard")
ctx.lists["self.symbol_key"] = symbol_key_words


special_keys = {
    "act":"escape",
    #"ace":"space",
    "space":"space",
    "ending":"end",
    "insert": "insert",

}
mod.list("special_key", desc="All symbols from the keyboard")
ctx.lists["self.special_key"] = special_keys


ctx.lists["self.movement"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
    "ending":"end",
    "home":"home",
    "west":"ctrl-left",
    "east":"ctrl-right",
    "page up": "pageup",
    "page down": "pagedown",
}

mod.list("movement", desc="All movement keys")
ctx.lists["self.movement"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
    "ending":"end",
    "home":"home",
    "west":"ctrl-left",
    "east":"ctrl-right",
    "page up": "pageup",
    "page down": "pagedown",
    "wipe": "backspace",
    "slap": "enter",
    "tabby": "tab",
    # 'junk': 'backspace',
    "delete": "delete",
}

mod.list("compound_movement", desc="All movement keys")
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


@mod.capture(rule="( {self.movement} | {self.compound_movement} )")
def movement(m) -> str:
    "One directional arrow key"
    return m[0]

@mod.capture(rule="( <self.movement> [<self.number_key>])+")
def movements(m) -> str:
    "One or more arrow keys separated by a space"
    keys=str(m).split()
    key_list=[]
    for key in keys:
        if key in numbers:
            num=int(key)-1
            if num >1:
                key_list.extend([key_list[-1] for i in range(num)])
        else:
            key_list.append(key)
    return " ".join(key_list)



@mod.capture(rule="[ <self.modifiers>+ ] (<self.movement> [<self.number_key>] )+")
def modified_movements(m) -> str:
    "One or more arrow keys separated by a space"
    keys=str(m).split()
    mods=None
    key_list=[]
    for key in keys:

        if key in modifier_keys:
            mods=mods+"-"+key if mods else key
        elif key in numbers:
            num=int(key)
            key_list.extend([key_list[-1] for i in range(num-1)])
        else:
            if mods:
                key_list.append(mods+"-"+key)
            else:
                key_list.append(key)
    return " ".join(key_list)

@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.movement> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key} <self.unmodified_key>+")
def key(m) -> str:
    "multi key with  modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join([mods + k for k in m.unmodified_key_list])

@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)
