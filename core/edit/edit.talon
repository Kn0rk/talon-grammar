#<user.modified_movements> : key(edit_movement)


copy: edit.copy()
cut that: edit.cut()
paste: edit.paste()
undo [<number_small>]:
    number=number_small or 1
    number=number - 1
    edit.undo()
    repeat(number)
redo [<number_small>]:
    number=number_small or 1
    number=number - 1
    edit.redo()
    repeat(number)


