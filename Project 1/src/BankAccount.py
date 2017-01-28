class BankAccount:
    def __init__(self, par1_id=-1, par2_name=None, par3_bal=0):
        self.id = par1_id
        self.name = par2_name
        self.balance = float(par3_bal)

    def has_id(self, par1_target):
        return par1_target == self.id

    def withdraw(self, par1_amount):
        if par1_amount > self.balance:
            raise Exception("No action: Amount greater than available balance.")
        self.balance -= par1_amount

    def deposit(self, par1_amount):
        self.balance += par1_amount

    def get_balance(self):
        return self.balance
