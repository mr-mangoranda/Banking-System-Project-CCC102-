# modules/transaction.py
from utils.file_io import read_json, write_json
from datetime import datetime

class Transaction:
    def __init__(self, account_number, txn_type, amount):
        self.account_number = account_number
        self.txn_type = txn_type
        self.amount = amount
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "type": self.txn_type,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

def deposit(account_number):
    accounts = read_json("data/accounts.json")
    transactions = read_json("data/transactions.json")

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount.")
        return

    accounts[account_number]["balance"] += amount
    write_json("data/accounts.json", accounts)

    txn = Transaction(account_number, "deposit", amount)
    transactions.append(txn.to_dict())
    write_json("data/transactions.json", transactions)

    print(f"Deposited ${amount:.2f} to {account_number}")

def withdraw(account_number):
    accounts = read_json("data/accounts.json")
    transactions = read_json("data/transactions.json")

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount.")
        return

    balance = accounts[account_number]["balance"]
    if amount > balance:
        print("Insufficient funds.")
        return

    accounts[account_number]["balance"] -= amount
    write_json("data/accounts.json", accounts)

    txn = Transaction(account_number, "withdraw", amount)
    transactions.append(txn.to_dict())
    write_json("data/transactions.json", transactions)

    print(f"Withdrew ${amount:.2f} from {account_number}")

def check_balance(account_number):
    accounts = read_json("data/accounts.json")

    if account_number not in accounts:
        print("Account not found.")
        return

    balance = accounts[account_number]["balance"]
    print(f"Account {account_number} balance: ${balance:.2f}")
