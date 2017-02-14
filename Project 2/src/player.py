class Player:
    def __init__(self, handle):
        self.handle = handle

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
        :param par3_list: The one card that the dealer has placed face-up
        :param par4_list: The cards that have already been revealed
        :return: True if the player wants a card, False otherwise
        """
        pass

    def use_ace_hi(self, par1_hand):
        pass


class DealerPlayer(Player):
    def make_bet(self, par1_bal):
        super().make_bet(par1_bal)

    def use_ace_hi(self, par1_hand):
        super().use_ace_hi(par1_hand)

    def want_card(self, par1_hand, par2_bank, par3_list, par4_list):
        super().want_card(par1_hand, par2_bank, par3_list, par4_list)

    def __init__(self, handle):
        super().__init__(handle)
