from talon import Module

mod = Module()
mod.tag("find_and_replace", desc="Tag for enabling generic find and replace commands")


@mod.action_class
class Actions:
    def find(text: str):
        """Finds text in current editor"""

    def find_next():
        """Navigates to the next occurrence"""

    def find_previous():
        """Navigates to the previous occurrence"""

    def find_everywhere(text: str):
        """Finds text across project"""

    def replace(text: str):
        """Search and replace for text in the active editor"""

    def replace_everywhere(text: str):
        """Search and replaces for text in the entire project"""

    def replace_confirm():
        """Confirm replace at current position"""

    def replace_confirm_all():
        """Confirm replace all"""

    def select_previous_occurrence(text: str):
        """Selects the previous occurrence of the text, and suppresses any find/replace dialogs."""

    def select_next_occurrence(text: str):
        """Selects the next occurrence of the text, and suppresses any find/replace dialogs."""


    def goto_next_phrase(text: str, num: int):
        """find next occurance of a phrase and place cursor to the right"""
        pass

    def goto_previous_phrase(text: str, num: int):
        """find next occurance of a phrase and place cursor to the right"""
        pass

    def goto_next_character(text: str = "", num: int = 1):
        """find next occurance of a character and place cursor to the right"""
        pass

    def goto_previous_character(text: str = "", num: int = 1):
        """find next occurance of a character and place cursor to the right"""
        pass