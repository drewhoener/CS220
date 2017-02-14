from player import DealerPlayer
from player_bank import PlayerBank
from french_deck import FrenchDeck
from hand import Hand
import collections

PlayerAttr = collections.namedtuple('PlayerAttr', ['player', 'hand', 'bank'])


class Dealer:
    def __init__(self, deck):
        self._dealer = DealerPlayer("dealer")
        self._deck = deck
        self._dealer_hand = Hand()
        self._players = {}
        self.cards_dealt = []

    def add_player(self, player, bank):
        if self._players.__contains__(player.handle):
            raise RuntimeError("Player is already contained in this Dict!")
        self._players[player.handle] = PlayerAttr(player, Hand(), bank)

    def take_bets(self):
        for key, attr in self._players:
            bet = attr.player.make_bet(attr.bank.get_balance())
            attr.bank.enter_bet(bet)

    def deal_inital_hand(self):
        pass
