import prefix
import suffix
from immdict import *
from functools import *

NONWORD = '\n'


def build(filename):
    return build_chain(add_to_chain, pairs_gen(filename, line_gen), ImmDict())


def build_chain(func, gen, chain_dict):
    return reduce(func, gen, chain_dict)


def add_to_chain(chain, pair):
    if pair[0] in chain.keys():
        new_suffix = suffix.add_word(chain.get(pair[0]), pair[1])
        return chain.put(pair[0], new_suffix)
    return chain.put(pair[0], suffix.add_word(suffix.empty_suffix(), pair[1]))


def pairs_gen(filename, line_func):
    lines = line_func(filename)

    pairs_str = ""
    for l in lines:
        pairs_str += l

    words = pairs_str.split(" ")

    return ((prefix.new_prefix(words[index], words[index + 1]), words[index + 2]) for index in range(len(words) - 3))


def line_gen(filename):
    with open(filename) as file:
        lines = []

        for line in file:
            lines.append(line)

        return (line for line in lines)
