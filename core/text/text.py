
from talon import Context, Module, actions, grammar, ui
mod = Module()

@mod.capture(rule="<phrase> +")
def text(m) -> str:
    """A sequence of words, including user-defined vocabulary."""
    return m

@mod.capture(rule="({user.vocabulary} | <phrase>)+")
def text_with_vocab(m) -> str:
    """A sequence of words, including user-defined vocabulary."""
    return m