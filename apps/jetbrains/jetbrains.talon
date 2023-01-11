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
toggle services: key("alt-8")
toggle git: key("alt-9")


