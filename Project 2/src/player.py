import random


class Player:

    def make_bet(self, par1_bal):
        """
        :param par1_bal: The balance of the player
        :return: The bet placed
        """
        pass

    def want_card(self, par1_hand, par2_bank, par3_list, par4_list):
        """
        :param par1_hand: The player's hand from the dealer
        :param par2_bank: The player's bank from the dealer
        :param par3_list: The one card that the dealer has placed face-down
        :param par4_list: The cards that have already been revealed
        :return: True if the player wants a card, False otherwise
        """
        pass

    def use_ace_hi(self, par1_hand):
        pass


class DealerPlayer(Player):

    def make_bet(self, par1_bal):
        return 0

    def use_ace_hi(self, par1_hand):
        if par1_hand.score_hand(True) > 21:
            return False
        return True

    def want_card(self, par1_hand, par2_bank, par3_list, par4_list):
        par1_hand.score_hand(self.use_ace_hi(par1_hand))
        if par1_hand.get_score() < 17:
            return True
        return False


class RandomPlayer(Player):
    def use_ace_hi(self, par1_hand):
        random.randint(0, 1)

    def make_bet(self, par1_bal):
        return random.randint(1, par1_bal)

    def want_card(self, par1_hand, par2_bank, par3_list, par4_list):
        par1_hand.score_hand(self.use_ace_hi(par1_hand))
        if par1_hand.get_score() < 21:
            return True
        return False


class ConservativePlayer(Player):
    def make_bet(self, par1_bal):
        return par1_bal / 2

    def use_ace_hi(self, par1_hand):
        # Hey, he's a conservative dude, don't judge him
        return False

    def want_card(self, par1_hand, par2_bank, par3_list, par4_list):
        par1_hand.score_hand(self.use_ace_hi(par1_hand))
        if par1_hand.get_score() < 16:
            return True
        return False
