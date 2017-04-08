from immdict import ImmDict
import markov_main


def empty_suffix():
    return ImmDict()


def add_word(suffix, word):
    if word in suffix.keys():
        return suffix.put(word, suffix.get(word) + 1)
    return suffix.put(word, 1)


def choose_word(chain, prefix, random):
    list_total = [dic for dic in chain.get(prefix).keys() for _ in range(chain.get(prefix).get(dic))]
    # print(list_total)
    return list_total[random(len(list_total)) - 1]


keyOne = ("this", "is")
keyTwo = ("you", "suck")

immOne = ImmDict({"the": 2, "a": 3})
immTwo = ImmDict({"at": 2, "this": 3})
dicti = ImmDict({keyOne: immOne, keyTwo: immTwo})
print(choose_word(dicti, keyOne, markov_main.randomizer))
