import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """ This class models a French deck of 52 cards. The dealer managed the player's hands and bets.
        Player objects implement a specific player's strategy. The player should not modify its
        hand or bet.

        Attributes:
                 ranks (:obj: 'list' of obj: str): ranks 2-10, J, Q, K, A
                 suits(:obj: 'list' of obj: str): the four suits
                 _cards (:obj: 'list' of obj: 'Card'): list of the cards in the deck.
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self, seed=None):
        """Accepts a seed parameter for the random number generator for debugging."""
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        if seed is not None:
            random.seed(seed)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def remove_card(self):
        """Removes a card at random from the list of cards (the deck)."""
        if len(self._cards) == 0:
            raise RuntimeError
        pos = random.randint(0, len(self._cards) - 1)
        return self._cards.pop(pos)

    def __setitem__(self, key, value):
        self._cards[key] = value
