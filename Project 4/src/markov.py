import sys
import builder
import generator
import random


def randomizer(bound):
    return random.randint(1, bound)


if __name__ == '__main__':
    args = sys.argv
    usage = 'Usage: %s (<text-file-name> <num-words>)' % (args[0],)

    if (len(args) < 3):
        raise ValueError(usage)

    file_name = args[1]
    num_words = int(args[2])
    chain = builder.build(file_name)
    outstr = generator.generate(chain, randomizer, num_words, builder.NONWORD)
    print(outstr)
