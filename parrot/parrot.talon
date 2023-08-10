
parrot(tse):
	core.repeat_phrase(1)

#parrot(hiss):
#	print("hiss")

parrot(hiss):               user.noise_debounce("hiss", true)
parrot(hiss:stop):          user.noise_debounce("hiss", false)

#parrot(hiss): print("hiss")
#parrot(hiss:stop): print("hissing has stopped")


parrot(woosh):              user.noise_debounce("shush", true)
parrot(woosh:stop):         user.noise_debounce("shush", false)