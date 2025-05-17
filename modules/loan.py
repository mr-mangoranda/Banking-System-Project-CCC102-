from utils.file_io import read_json, write_json
from datetime import datetime

def apply_for_loan(username):
    loans = read_json("data/loans.json")
    amount = float(input("Enter loan amount: "))
    term = int(input("Enter loan term in months: "))
    interest_rate = 0.05

    loan = {
        "amount": amount,
        "term": term,
        "interest_rate": interest_rate,
        "status": "pending",
        "remaining": amount + (amount * interest_rate),
        "payments": [],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    loans.setdefault(username, []).append(loan)
    write_json("data/loans.json", loans)
    print("Loan application submitted. Await admin approval.")

def view_loan_status(username):
    loans = read_json("data/loans.json")

    if username not in loans:
        print("No loans found.")
        return

    for idx, loan in enumerate(loans[username], 1):
        print(f"\nLoan {idx}")
        print(f"Amount: {loan['amount']}")
        print(f"Term: {loan['term']} months")
        print(f"Interest Rate: {loan['interest_rate']}")
        print(f"Status: {loan['status']}")
        print(f"Remaining: {loan['remaining']}")
        print(f"Payments: {loan['payments']}")

def make_loan_payment(username):
    loans = read_json("data/loans.json")

    if username not in loans:
        print("No loans found.")
        return

    for i, loan in enumerate(loans[username]):
        if loan["status"] != "approved" or loan["remaining"] <= 0:
            continue

        print(f"\nLoan {i+1}: Remaining balance = {loan['remaining']}")
        try:
            amount = float(input("Enter payment amount: "))
            if amount <= 0:
                print("Invalid amount.")
                return
        except ValueError:
            print("Invalid input.")
            return

        loan["remaining"] -= amount
        loan["payments"].append({
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if loan["remaining"] <= 0:
            loan["status"] = "paid"

        write_json("data/loans.json", loans)
        print("Payment successful.")
        return

    print("No active approved loans available.")

