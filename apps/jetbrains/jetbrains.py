import os
import os.path
import tempfile
import time
from pathlib import Path
import requests
from talon import Context, Module, actions, clip, ui

extendCommands = []


ctx = Context()
mod = Module()

mod.apps.jetbrains = "app.name: /jetbrains/"
mod.apps.jetbrains = "app.name: CLion"
mod.apps.jetbrains = "app.name: IntelliJ IDEA"
mod.apps.jetbrains = "app.name: PyCharm"
mod.apps.jetbrains = "app.name: WebStorm"
mod.apps.jetbrains = "app.name: RubyMine"
mod.apps.jetbrains = "app.name: RubyMine-EAP"
mod.apps.jetbrains = "app.name: DataGrip"
mod.apps.jetbrains = """
os: mac
and app.bundle: com.google.android.studio
"""
# windows
mod.apps.jetbrains = "app.exe: idea64.exe"
mod.apps.jetbrains = "app.exe: PyCharm64.exe"
mod.apps.jetbrains = "app.exe: pycharm64.exe"
mod.apps.jetbrains = "app.exe: webstorm64.exe"
mod.apps.jetbrains = """
os: mac
and app.bundle: com.jetbrains.pycharm
"""
mod.apps.jetbrains = """
os: windows
and app.name: JetBrains Rider
os: windows
and app.exe: rider64.exe
"""



ctx.matches = r"""
app: jetbrains
"""


@ctx.action_class("app")
class AppActions:
    def tab_next():
        actions.key("alt-right")

    def tab_previous():
        actions.key("alt-left")

    def tab_close():
        actions.key("ctrl-alt-f4")




@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment():
        actions.key('ctrl-keypad_divide')


@ctx.action_class("edit")
class EditActions:
    # talon edit actions

    def jump_line(n: int):
        actions.key("ctrl-g")
        actions.insert(n)
        time.sleep(0.1)
        actions.key('enter')




@ctx.action_class("win")
class WinActions:
    def filename() -> str:
        title: str = actions.win.title()
        result = title.split()

        # iterate over reversed result
        # to support titles such as
        # Class.Library2 – a.js [.workspace]
        for word in reversed(result):
            if not word.startswith("[") and "." in word:
                return word

        return ""


@ctx.action_class("user")
class UserActions:

    def goto_next_character(text: str = "", num: int = 1):
        actions.user.goto_next(text ,num)

    def goto_next(text: str = "", num: int = 1):
        # actions.key("ctrl-right")
        actions.key("ctrl-f")
        time.sleep(0.35)
        actions.key(" ".join(text))
        time.sleep(0.2)
        actions.key("enter")
        actions.key("escape")
        # if len(text) == 1:
        #     num += 1
        for i in range(num - 1):
            actions.key("f3")
        actions.key("escape")

    def goto_prev_character(text: str = "", num: int = 1):
        actions.user.goto_prev(text, num)

    def goto_prev(text: str = "", num: int = 1):
        # actions.key("ctrl-left")
        actions.key("ctrl-f")
        time.sleep(0.35)
        actions.key(" ".join(text))
        time.sleep(0.2)
        actions.key("enter")

        actions.key("escape")

        for i in range(num + 1):
            actions.key("shift-f3")
        actions.key("escape")

    def tab_jump(number: int):
        # depends on plugin GoToTabs
        if number < 10:
            actions.user.idea(f"action GoToTab{number}")

    def select_range(line_start: int, line_end: int):
        actions.key("ctrl-g")
        actions.insert(line_start)
        time.sleep(0.1)
        actions.key('enter')
        for i in range(line_end-line_start):
            actions.key('shift-down')
        actions.key('shift-end')

