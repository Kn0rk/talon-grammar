mode: dictation
mode: command
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
^mixed mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
^talon sleep [<phrase>]$:
    mode.disable("command")
    mode.disable("dictation")
    mode.enable("sleep")

