class Account:
    interest = 0.02

    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

    def desport(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            assert 'No enghout'
        self.balance -= amount
        return self.balance


class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


class Bank:
    def __init__(self):
        self.person_account = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.desport(amount)
        self.person_account.append(account)
        return account

    def interest_add(self):
        for i in self.person_account:
            i.desport(i.balance * i.interest)


class SavingAccount(Account):
    desport_free = 2
    def desport(self, amount):
        return Account.desport(self, amount - self.desport_free)


class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    def __init__(self, holder):
        super().__init__(holder)
        self.holder = holder
        self.balance = 1

such_a_deal = AsSeenOnTVAccount("Mike")
print(such_a_deal.balance)