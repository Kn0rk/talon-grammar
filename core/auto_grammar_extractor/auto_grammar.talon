


python <user.python_keywords>: "{python_keywords}"
extract terminal grammar: user.extract_grammar_from_terminal_history()


add for <phrase>+ in  <user.python_keywords>:
    variable=user.str_list_to_snake(phrase_list)
    "for {variable} in {python_keywords}:"

insert <user.python_keywords>:
    user.context_awareinsert(python_keywords)