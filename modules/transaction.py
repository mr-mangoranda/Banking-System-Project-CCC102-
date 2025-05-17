from utils.file_io import read_json, write_json
from datetime import datetime

def deposit(account_number):
    accounts = read_json("data/accounts.json")
    transactions = read_json("data/transactions.json")

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid input.")
        return

    accounts[account_number]["balance"] += amount

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transactions.setdefault(account_number, []).append({
        "type": "deposit",
        "amount": amount,
        "timestamp": timestamp
    })

    write_json("data/accounts.json", accounts)
    write_json("data/transactions.json", transactions)
    print(f"{amount} deposited successfully.")

def withdraw(account_number):
    accounts = read_json("data/accounts.json")
    transactions = read_json("data/transactions.json")

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid input.")
        return

    if accounts[account_number]["balance"] < amount:
        print("Insufficient funds.")
        return

    accounts[account_number]["balance"] -= amount

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transactions.setdefault(account_number, []).append({
        "type": "withdraw",
        "amount": amount,
        "timestamp": timestamp
    })

    write_json("data/accounts.json", accounts)
    write_json("data/transactions.json", transactions)
    print(f"{amount} withdrawn successfully.")

def check_balance(account_number):
    accounts = read_json("data/accounts.json")
    if account_number not in accounts:
        print("Account not found.")
        return

    balance = accounts[account_number]["balance"]
    print(f"Current balance for {account_number}: {balance}")
