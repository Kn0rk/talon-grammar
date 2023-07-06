#provide both anchored and unachored commands via 'over'
<user.format_text>+$: user.insert_many(format_text_list)
say <user.text_with_vocab>+$: user.insert_many(text_with_vocab_list)


{user.prose_formatter} <user.prose>$:
   user.insert_formatted(prose, prose_formatter)
#{user.prose_formatter} <user.prose> over:
#    user.insert_formatted(prose, prose_formatter)
<user.format_text>+$: user.insert_many(format_text_list)
<user.format_text>+ over: user.insert_many(format_text_list)
<user.formatters> that: user.formatters_reformat_selection(user.formatters)
#word <user.word>: user.insert_with_history(user.word)

