def spaces(line, text, bonus_spaces):
    total_spaces = len(line) - len(text) - bonus_spaces
    return " " * total_spaces