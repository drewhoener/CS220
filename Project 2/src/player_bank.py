class PlayerBank:
    def __init__(self, bal=0):
        self._balance = bal
        self._bets_placed = 0
        self._is_winner = False

    def pay_winner(self, amount):
        self._balance += amount
        self._is_winner = True

    def bust(self):
        self._is_winner = False

    def get_balance(self):
        return self._balance

    def get_wager(self):
        return self._bets_placed

    def enter_bet(self, amount):
        if amount > self._balance:
            raise RuntimeError("Bet is greater than Balance!")
        self._bets_placed = amount
        self._balance -= amount

    def __str__(self):
        state = "winner!" if self._is_winner else "bust."
        return "bet %.2f balance %.2f %s" % (self._bets_placed, self._balance, state)
