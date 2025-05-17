from utils.file_io import read_json, write_json
from datetime import datetime

def transfer_funds(sender_account):
    accounts = read_json("data/accounts.json")
    transactions = read_json("data/transactions.json")

    if sender_account not in accounts:
        print("Sender account not found.")
        return

    recipient_account = input("Enter recipient account number: ")
    if recipient_account not in accounts:
        print("Recipient account not found.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid input.")
        return

    if accounts[sender_account]["balance"] < amount:
        print("Insufficient funds.")
        return

    # Process transfer
    accounts[sender_account]["balance"] -= amount
    accounts[recipient_account]["balance"] += amount

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log sender transaction
    transactions.setdefault(sender_account, []).append({
        "type": "transfer_out",
        "amount": amount,
        "to": recipient_account,
        "timestamp": timestamp
    })

    # Log recipient transaction
    transactions.setdefault(recipient_account, []).append({
        "type": "transfer_in",
        "amount": amount,
        "from": sender_account,
        "timestamp": timestamp
    })

    write_json("data/accounts.json", accounts)
    write_json("data/transactions.json", transactions)
    print(f"Transferred {amount} from {sender_account} to {recipient_account}.")

def view_transaction_history(account_number):
    transactions = read_json("data/transactions.json")

    if account_number not in transactions:
        print("No transactions found for this account.")
        return

    print(f"\nTransaction History for {account_number}")
    for txn in transactions[account_number]:
        print(txn)

def filter_transactions(account_number):
    transactions = read_json("data/transactions.json")

    if account_number not in transactions:
        print("No transactions found.")
        return

    print("\n=== Filter Transactions ===")
    txn_type = input("Enter type to filter (deposit/withdraw/transfer_in/transfer_out or leave blank): ").lower()
    start_date = input("Start date (YYYY-MM-DD) or leave blank: ")
    end_date = input("End date (YYYY-MM-DD) or leave blank: ")

    filtered = []
    for txn in transactions[account_number]:
        if txn_type and txn["type"] != txn_type:
            continue
        if "timestamp" in txn:
            txn_date = txn["timestamp"][:10]
            if start_date and txn_date < start_date:
                continue
            if end_date and txn_date > end_date:
                continue
        filtered.append(txn)

    print(f"\nFiltered Transactions for {account_number}:")
    for txn in filtered:
        print(txn)

def generate_transaction_report(account_number):
    transactions = read_json("data/transactions.json")

    if account_number not in transactions:
        print("No transactions found.")
        return

    total_deposit = total_withdraw = total_transfer_in = total_transfer_out = 0

    for txn in transactions[account_number]:
        if txn["type"] == "deposit":
            total_deposit += txn["amount"]
        elif txn["type"] == "withdraw":
            total_withdraw += txn["amount"]
        elif txn["type"] == "transfer_in":
            total_transfer_in += txn["amount"]
        elif txn["type"] == "transfer_out":
            total_transfer_out += txn["amount"]

    print("\n=== Transaction Report ===")
    print(f"Total Deposits: {total_deposit}")
    print(f"Total Withdrawals: {total_withdraw}")
    print(f"Total Transfer In: {total_transfer_in}")
    print(f"Total Transfer Out: {total_transfer_out}")
    print(f"Net Balance Change: {total_deposit - total_withdraw - total_transfer_out + total_transfer_in}")