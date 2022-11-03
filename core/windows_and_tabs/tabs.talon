tag: user.tabs
-
tab (open | new): app.tab_open()
tab (last | previous) [<number_small>]:
    number=number_small or 1
    number=number - 1
    app.tab_previous()
    repeat(number)
tab next [<number_small>]:
    number=number_small or 1
    number=number - 1
    app.tab_next()
    repeat(number)
tab close: user.tab_close_wrapper()
tab (reopen | restore): app.tab_reopen()
go tab <number>: user.tab_jump(number)
go tab final: user.tab_final()
tab duplicate: user.tab_duplicate()
