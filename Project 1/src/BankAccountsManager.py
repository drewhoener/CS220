from BankAccount import BankAccount


class BankAccountsManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, par1_id, par2_name):
        account = BankAccount(par1_id, par2_name, 0.00)
        self.accounts.append(account)

    def get_account(self, par1_id):
        for account in self.accounts:
            if isinstance(account, BankAccount):
                if getattr(account, 'id') == par1_id:
                    return account
        return None

    def make_deposit(self, par1_id, par2_amount):
        account = self.get_account(par1_id)
        if account is None:
            raise Exception("Account Not Found!")
        else:
            getattr(account, 'deposit')(par2_amount)

    def make_withdrawl(self, par1_id, par2_amount):
        account = self.get_account(par1_id)
        if account is None:
            raise Exception("Account Not Found!")
        else:
            getattr(account, 'withdraw')(par2_amount)

    def get_balance(self, par1_id):
        account = self.get_account(par1_id)
        if account is None:
            raise Exception("Account Not Found!")
        else:
            return getattr(account, 'get_balance')

    def get_account_report(self, par1_id):
        account = self.get_account(par1_id)
        if account is None:
            raise Exception("Account Not Found!")
        else:
            acc_id = getattr(account, 'id')
            acc_name = getattr(account, 'name')
            acc_bal = getattr(account, 'balance')
            return "ID: %d\nName: %s\nBalance: %.2f\n" % (acc_id, acc_name, acc_bal)


if __name__ == '__main__':
    manager = BankAccountsManager()
    for i in range(0, 10):
        manager.add_account(i, "Test_Account")
    for i in range(0, 10):
        manager.make_deposit(i, 50)
        if i < 9:
            manager.make_withdrawl(i, 40.60)
            print(manager.get_account_report(i))
    manager.make_withdrawl(9, 20)
    print(manager.get_account_report(9))