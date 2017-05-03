"""A RegEx represents one of the following possible regular expressions:

1. Epsilon                - the re that matches anything (empty string)
2. NullSet                - the re that matches nothing (null)
3. Character              - the re that matches a single character c
4. Sequence(re1,re2)      - the re that matches a sequence of re1 followed by re2
5. Alternative(re1 | re2) - the re that matches an alternative: re1 OR re2
6. Closure(re*)           - the re that matches 0 or more of re
"""


class Epsilon:
    """ the empty RE """

    def delta(self):
        return self

    def is_empty(self):
        return True

    def derive(self, char):
        return NullSet()

    def normalize(self):
        return self


class NullSet:
    def delta(self):
        return self

    def is_empty(self):
        return False

    def derive(self, char):
        return NullSet()

    def normalize(self):
        return self


class Character:
    def __init__(self, char):
        self.char = char

    def delta(self):
        return NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        return NullSet() if self.char != char else Epsilon()

    def normalize(self):
        return self


class Sequence:
    def __init__(self, re1, re2):
        self.re1 = re1
        self.re2 = re2

    def delta(self):
        return Epsilon() if self.re1.is_empty() and self.re2.is_empty() else NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        return Epsilon() if (self.re1.delta().is_empty() and self.re2.derive(char).is_empty()) or (
        self.re1.derive(char).is_empty() and self.re2.delta().is_empty()) \
            else \
            NullSet()

    def normalize(self):
        if self.re1 is NullSet or self.re2 is NullSet:
            return NullSet()
        if self.re2.is_empty():
            return self.re1.normalize()
        if self.re1.is_empty():
            return self.re2.normalize()
        return self if (self.re1.normalize() is self.re1) and (self.re2.normalize() is self.re2) else NullSet


class Alternation:
    def __init__(self, re1, re2):
        self.re1 = re1
        self.re2 = re2

    def delta(self):
        return Epsilon() if self.re1.is_empty() or self.re2.is_empty() else NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        return Epsilon() if (self.re1.derive(char).is_empty() or self.re2.derive(char).is_empty()) else NullSet()

    def normalize(self):
        if self.re1 is NullSet:
            return self.re2.normalize()
        if self.re2 is NullSet:
            return self.re1.normalize()
        if self.re1.is_empty():
            return self.re2.normalize()
        return self if (self.re1.normalize() is self.re1) or (self.re2.normalize() is self.re2) else NullSet


class Closure:
    def __init__(self, re1):
        self.re1 = re1

    def delta(self):
        return Epsilon()

    def is_empty(self):
        return True

    def derive(self, char):
        return Epsilon() \
            if \
            self.re1.derive(char).is_empty() \
            else \
            NullSet()

    def normalize(self):
        return self.re1.normalize()


def make_str(str_input):
    if not str_input:
        return Sequence(Epsilon(), Epsilon())
    if len(str_input) == 1:
        return Sequence(Character(str_input[0]), Epsilon())
    return Sequence(Character(str_input[0]), make_str(str_input[1:]))


def matches(regex, str):
    curr = regex

    if type(regex) is Sequence:
        curr = regex.re1

    if not str:
        return curr.delta().is_empty()
    if len(str) == 1 and type(curr) is not Closure:
        derivative = curr.derive(str[0])
        normalized = derivative.normalize()

        if type(regex) is Sequence and not regex.re2.is_empty():
            return False
        return normalized.is_empty()
    if len(str) == 1:
        derivative = curr.derive(str[0])
        normalized = derivative.normalize()

        if not normalized.is_empty() and type(regex) is Sequence and type(regex.re2) is not Epsilon:
            return matches(regex.re2, str)
        else:
            if type(regex) is Sequence and not regex.re2.is_empty():
                return False
            return normalized.is_empty()

    derivative = curr.derive(str[0])
    normalized = derivative.normalize()
    curr_match = normalized.is_empty()
    recur = str[1:]

    if type(regex) is Sequence and type(regex.re1) is Closure:
        if not curr_match:
            curr_match = True
            regex = regex.re2
            recur = str
    elif type(regex) is Sequence:
        regex = regex.re2
    elif type(regex) is not Closure:
        regex = NullSet()

    return curr_match and matches(regex, recur)


if __name__ == '__main__':
    regex = Character('x')
    str_to_match = 'x'
    result = matches(regex, str_to_match)
    print(result)
