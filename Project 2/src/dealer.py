from player import DealerPlayer
from hand import Hand
import collections

PlayerAttr = collections.namedtuple('PlayerAttr', ['player', 'hand', 'bank'])


def resolve_player(handle, attr):
    return "Player: %s\nscore: %d\n%s\nPlayer assets:\n%s\n\n" % (
    handle, attr.hand.get_score(), str(attr.hand), str(attr.bank))


class Dealer:
    def __init__(self, deck):
        self._dealer = DealerPlayer()
        self._deck = deck
        self._dealer_hand = Hand()
        self._players = {}
        self.cards_dealt = []
        self._face_up = []

    def add_player(self, handle, player, bank):
        if self._players.__contains__(handle):
            raise RuntimeError("Player is already contained in this Dict!")
        self._players[handle] = PlayerAttr(player, Hand(), bank)

    def take_bets(self):
        for key, attr in self._players.items():
            bet = attr.player.make_bet(attr.bank.get_balance())
            attr.bank.enter_bet(bet)

    def deal_initial_hand(self):
        for handle, player in self._players.items():
            for i in range(0, 2):
                card = self._deck.remove_card()
                player.hand.add_card(card)
                self.cards_dealt.append(card)
        for i in range(0, 2):
            card = self._deck.remove_card()
            self._dealer_hand.add_card(card)
            if i < 1:
                self.cards_dealt.append(card)
            else:
                self._face_up.append(card)

    def deal_player_hands(self):
        for k, v in self._players.items():
            while v.player.want_card(v.hand, v.bank, self._face_up, self.cards_dealt):
                card = self._deck.remove_card()
                v.hand.add_card(card)
                self.cards_dealt.append(card)

    def deal_dealer_hand(self):
        # have to take card until >17
        # aces 11 until score is >21
        while self._dealer.want_card(self._dealer_hand, None, self._face_up, self.cards_dealt):
            card = self._deck.remove_card()
            self._dealer_hand.add_card(card)
            self.cards_dealt.append(card)

    def settle_bets(self):
        self._dealer_hand.score_hand(self._dealer.use_ace_hi(self._dealer_hand))
        for k, v in self._players.items():
            hand = v.hand
            bank = v.bank
            player = v.player
            if hand.score_hand(player.use_ace_hi(hand)) > 21:
                bank.bust()
            elif self._dealer_hand.get_score() > 21:
                bank.pay_winner(bank.get_wager() * 2)
            else:
                if hand.get_score() > self._dealer_hand.get_score():
                    bank.pay_winner(bank.get_wager() * 2)
                else:
                    bank.bust()

    def __str__(self):
        summary = "$$$$$$\tGame Summary\t$$$$$$\n"
        dealer_str = "Dealer: %s\nscore: %d\n%s\n\n" % ("", self._dealer_hand.get_score(), self._dealer_hand)
        players = ""
        for k, v in self._players.items():
            players += resolve_player(k, v)
        return summary + dealer_str + players.strip()
