<user.modified_movements> : key(edit_movement)

find <user.text>: edit.find(text)
find <user.any_alphanumeric_key> : edit.find(any_alphanumeric_key_list)
find that: edit.find()

copy: edit.copy()
cut that: edit.cut()
paste: edit.paste()
undo: edit.undo()
redo: edit.redo()
line <number>: edit.jump_line(number)
