import json
import os
class Account:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number":self.acc_number,
            "name": self.name,
            "balance": self.balance
        }
    @classmethod
    def from_dict(cls, data):
        return cls(data["account_number"], data["name"], data["balance"])
    
class Bank(Account):
    global file
    file = 'accounts.txt'
    def __init__(self):
        self.accounts = {}
        if os.path.exists(file):
            self.load_from_file()

    def load_from_file(self):
        if os.path.exists(file) and os.path.getsize(file) > 0:
            with open(file, 'r') as contents:
                try:
                    data = json.load(contents)  # Read and parse JSON
                    self.accounts = {int(num): Account.from_dict(acc) for num, acc in data.items()}
                    print(self.accounts)
                except json.JSONDecodeError: # incase the file is empty or there is some kindo f error
                    self.accounts = {}
       
    def save_to_file(self):
        with open(file, 'w') as filew: #file for 'w', writing
            json.dump({a:b.to_dict() for a, b in self.accounts.items()}, filew, indent = 1) #readable
                     
    def create_account(self, name, initial):
        try:
            acc_num = max(self.accounts.keys()) + 1 #new account number for new account ;)
        except ValueError:
            acc_num = 1000 #if no account is there, in case
        new_acc = Account(acc_num, name, initial)
        self.accounts[acc_num] = new_acc
        self.save_to_file()
        print("Account created!")

    def view_account(self, account_number):
        return self.accounts[account_number] if self.accounts.get(account_number) else "Account was not found :("

    def deposit(self, account_number, amount):
        if account_number in self.accounts.keys():
            self.accounts.get(account_number).balance += amount
            self.save_to_file()
            print("Deposit was completed successfully!")
        else:
            print("Sorry, your account was not found :(")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                self.save_to_file()
                print("Withdrawing process completed!")
            else:
                print("Insufficient funds, brokie ;)")
        else:
            print("Account is not found.")
        




new1 = Bank()
new1.create_account("Mr.Darcy", 10000)
new1.create_account("Hello", 0)
new1.withdraw(1000, 2000)
new1.deposit(1001, 2000)