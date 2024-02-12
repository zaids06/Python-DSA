class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self):
        self.balance = 500

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds in the account.")
        else:
            self.balance -= amount
            print("Remaining:", self.balance, sep="")

try:
    amount = int(input())
    account = BankAccount()
    account.withdraw(amount)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except InsufficientFundsError as e:
    print(e)
