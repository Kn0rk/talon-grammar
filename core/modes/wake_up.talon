mode: sleep
-
^talon awaken from your slumber$:
    mode.disable("sleep")
    mode.enable("command")
