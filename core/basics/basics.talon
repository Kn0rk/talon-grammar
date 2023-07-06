<user.modified_movements>: key(modified_movements)
[go] <user.movement> [<number_small>]:
    number=number_small or 1
    number=number-1
    key(movement)
    repeat(number)

press <user.alphasymbolic_key>+:
   user.key_list(alphasymbolic_key_list)
double <user.symbol_key>:
    key(symbol_key)
    key(symbol_key)

triple <user.symbol_key>:
    key(symbol_key)
    key(symbol_key)
    key(symbol_key)

