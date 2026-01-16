# 1.
class BackAccount:
    def __init__(self, account_number ,balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created successfully")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Current balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current balance:", self.balance)

    def __del__(self):
        print("BankAccount object deleted")

account = BackAccount(123456789,150000)

account.deposit(20000)
account.withdraw(50000)
account.withdraw(20000)
