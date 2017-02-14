from french_deck import Card


class Hand:
    def __init__(self):
        self._cards = []
        self._score = 0

    def add_card(self, card):
        self._cards.append(card)

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def has_ace(self):
        for card in self._cards:
            if card.rank == "A":
                return True
        return False

    def score_hand(self, high):
        score = 0
        for card in self._cards:
            if card.rank == "A":
                score += (11 if high else 1)
            elif list('JQK').__contains__(card.rank):
                score += 10
            else:
                score += card.rank
        return score

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        string = ""
        for card in self._cards:
            string += str(card) + " "
        return string
