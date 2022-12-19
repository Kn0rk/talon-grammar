tag: user.find_and_replace
-
find <user.text>: edit.find(text)
find <user.any_alphanumeric_key> : edit.find(any_alphanumeric_key_list)
find that: edit.find()

next <user.any_alphanumeric_key> [<number_small>]: user.goto_next_character(any_alphanumeric_key,number_small or 1)
next <user.text> [<number_small>]: user.goto_next(text,number_small or 1)
last <user.any_alphanumeric_key> [<number_small>]: user.goto_prev_character(any_alphanumeric_key,numbers_small or 1)
last <user.text> [<number_small>]: user.goto_prev(text,number_small or 1)