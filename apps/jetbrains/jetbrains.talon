# Requires https://plugins.jetbrains.com/plugin/10504-voice-code-idea
app: jetbrains
-
tag(): user.line_commands
tag(): user.splits
tag(): user.tabs
tag(): user.find_and_replace
# multiple_cursors.py support end

# Auto complete
complete: key("ctrl-space")
actions: key("alt-enter")
fix: key("alt-enter")


# GIT
git pull: key("ctrl-ralt-q")
git fetch: key("ctrl-ralt-w")
git commit: key("ctrl-k")

# Panels
hide panel: key("shift-escape")
toggle project: key("alt-1")
toggle bookmarks: key("alt-2")
toogle find: key("alt-3")
toggle run: key("alt-4")
toggle debug: key("alt-5")
toggle problems: key("alt-6")
toggle structure: key("alt-7")
toggle services: key("alt-8")
toggle git: key("alt-9")

# Code folding
collapse: key("ctrl-minus")
collapse all: key("ctrl-shift-keypad_minus")
expand: key("ctrl-plus")
expand all: key("ctrl-shift-keypad_plus")
collapse to <number_small>:
    key("ctrl-keypad_multiply")
    sleep(500ms)
    key("keypad_{number_small}")
collapse all to <number_small>:
    key("ctrl-shift-keypad_multiply")
    sleep(500ms)
    key("keypad_{number_small}")

# Navigation
go to file: key('ctrl-shift-n')
go to class: key('ctrl-n')
go to symbol: key('ctrl-alt-shift-n')
go to symbols: key('ctrl-alt-shift-n')
go to actions: key('ctrl-shift-a')

# Execution
run debug:key('shift-f9')
run app: key('shift-f10')
stop app: key('ctrl-f2')
set breakpoint: key('ctrl-f8')
edit breakpoint: key(' shift-ctrl-f8')
continue running: key('f9')
step over [<number_small>]:
    number=number_small or 1
    number=number - 1
    key('f8')
    repeat(number)

# refactoring
rename: key('shift-f6')
restructure: key('ctrl-alt-l')
comment: key('ctrl-keypad_divide')























