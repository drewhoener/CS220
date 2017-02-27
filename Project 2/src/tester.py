from dealer import Dealer
from french_deck import FrenchDeck
from player import *
from player_bank import PlayerBank
import random

if __name__ == '__main__':
    dealer = Dealer(FrenchDeck(random.randint(10000, 99999)))
    dealer.add_player('lia9', ConservativePlayer(), PlayerBank(100))
    dealer.add_player('ned21', RandomPlayer(), PlayerBank(100))
    dealer.take_bets()
    dealer.deal_initial_hand()
    dealer.deal_player_hands()
    dealer.deal_dealer_hand()
    dealer.settle_bets()
    print(str(dealer))
