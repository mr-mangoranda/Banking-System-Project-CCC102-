from utils.file_io import read_json, write_json

def approve_loans():
    loans = read_json("data/loans.json")

    for user, user_loans in loans.items():
        for loan in user_loans:
            if loan["status"] == "pending":
                print(f"\nUser: {user}")
                print(f"Amount: {loan['amount']}, Term: {loan['term']}, Interest: {loan['interest_rate']}")
                decision = input("Approve this loan? (y/n): ").lower()
                if decision == "y":
                    loan["status"] = "approved"
                elif decision == "n":
                    loan["status"] = "rejected"

    write_json("data/loans.json", loans)
    print("Loan approval process completed.")

def view_all_users():
    users = read_json("data/users.json")
    print("\n=== All Users ===")
    for user, info in users.items():
        print(f"User: {user}, Name: {info['name']}, Phone: {info['phone']}")

def view_all_accounts():
    accounts = read_json("data/accounts.json")
    print("\n=== All Accounts ===")
    for acc, info in accounts.items():
        print(f"Account: {acc}, Owner: {info['owner']}, Balance: {info['balance']}")

def view_all_transactions():
    transactions = read_json("data/transactions.json")
    print("\n=== All Transactions ===")
    for acc, txns in transactions.items():
        print(f"\nAccount: {acc}")
        for txn in txns:
            print(txn)

def view_all_loans():
    loans = read_json("data/loans.json")
    print("\n=== All Loans ===")
    for user, user_loans in loans.items():
        print(f"\nUser: {user}")
        for loan in user_loans:
            print(loan)
