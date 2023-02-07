# NOTE: If you want to use i3wm you must enable the tag settings.talon. ex: `tag(): user.i3wm`
os: linux
tag: user.i3wm
-
window <user.number_key>: key("super-{user.number_key}")
window move <user.number_key>: key("super-shift-{user.number_key}")
window move <user.movement>: key("super-shift-{user.movement}")



( window) (kill | murder | close): user.system_command("i3-msg kill")
( window) stacking: user.system_command("i3-msg layout stacking")
( window) default: user.system_command("i3-msg layout toggle split")
(full screen | scuba): user.system_command("i3-msg fullscreen")

# these rely on the user settings for the mod key. see i3wm.py Actions class
launch: user.i3wm_launch()
launch <user.text>:
    user.i3wm_launch()
    sleep(100ms)
    insert("{text}")
lock screen: user.i3wm_launch()
