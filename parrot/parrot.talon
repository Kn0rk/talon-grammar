
parrot(tse):
	core.repeat_phrase(1)

parrot(click):
	print("click")
	user.mouse_click("right")

#parrot(hiss):               user.mouse_click("right")
#parrot(hiss:stop):          user.noise_debounce("hiss", false)

#parrot(hiss): print("hiss")
#parrot(hiss:stop): print("higssing has stopped")


#parrot(woosh):              user.mouse_control_toggle()
#parrot(woosh:stop):         user.noise_debounce("shush", false)()