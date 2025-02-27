"""Write a Python program to create a class representing a bank. Include
 methods for managing customer accounts and transactions"""

class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited", amount, "into account", self.account_number, ". New balance:", self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew", amount, "from account", self.account_number, ". New balance:", self.balance)
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)
        print()


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance=0.0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, name, initial_balance)
            print("Account", account_number, "created successfully for", name, ".")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def display_all_accounts(self):
        if self.accounts:
            print("\nAccounts at", self.name, ":")
            for account in self.accounts.values():
                account.display_account_info()
        else:
            print("No accounts found.")



if __name__ == "__main__":
    bank = Bank("MyBank")

    bank.create_account("101", "abc", 500)
    bank.create_account("102", "xyz", 1000)

    account = bank.get_account("101")
    if account:
        account.deposit(200)
        account.withdraw(100)
        account.display_account_info()

    bank.display_all_accounts()

