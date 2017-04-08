import prefix
import suffix


def get_word_list(chain, pref, randomizer, num, nonword):
    return tuple(helper(chain, pref, randomizer, num, nonword, []))


def helper(chain, pref, random, num, nonword, list):
    if num == 0:
        return list

    word = suffix.choose_word(chain, pref, random)
    if word == nonword:
        return list

    list.append(word)
    helper(chain, prefix.shift_in(pref, word), random, num - 1, nonword, list)
    return list


def generate(chain, rand, num, nonword):
    generated_tup = get_word_list(chain, chain.keys()[0], rand, num, nonword)
    return ' '.join(list(generated_tup))
