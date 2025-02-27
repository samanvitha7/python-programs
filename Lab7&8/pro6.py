"""Create a class "BankAccount" with attributes account number and balance.
 Implement methods to deposit and withdraw funds, and a display method to
   show the account details"""
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_account_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Balance: {self.balance}")

account1 = BankAccount("123456789", 1000.0)
account1.display_account_details()
account1.deposit(500)
account1.withdraw(300)
account1.display_account_details()
