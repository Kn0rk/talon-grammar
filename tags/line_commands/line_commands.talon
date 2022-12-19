tag: user.line_commands
-
#this defines some common line commands. More may be defined that are ide-specific.
line <number>: edit.jump_line(number)
(select | cell | sell) [line] <number>: user.select_range(number, number)
(select | cell | sell) [from] <number> (until | to) <number>:
    user.select_range(number_1, number_2)
