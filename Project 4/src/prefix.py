import immdict


def new_prefix(first, second):
    return (first, second)


def shift_in(tup, word):
    return new_prefix(tup[1], word)
