from modules import auth, transaction, funds

def main_menu():
    while True:
        print("\n=== BANK SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            auth.register_user()
        elif choice == "2":
            user = auth.login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def user_menu(user):
    while True:
        print(f"\n--- Welcome, {user}! ---")
        print("1. Account Management")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Check Balance")
        print("5. Transfer / History")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            account_management_menu(user)
        elif choice == "2":
            acc_num = input("Enter your account number: ")
            transaction.deposit(acc_num)
        elif choice == "3":
            acc_num = input("Enter your account number: ")
            transaction.withdraw(acc_num)
        elif choice == "4":
            acc_num = input("Enter your account number: ")
            transaction.check_balance(acc_num)
        elif choice == "5":
            funds_menu(user)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid option.")

def account_management_menu(user):
    while True:
        print(f"\n--- Account Management for {user} ---")
        print("1. Update Profile")
        print("2. Create Account")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            auth.update_profile(user)
        elif choice == "2":
            auth.create_account(user)
        elif choice == "3":
            break
        else:
            print("Invalid option.")

def funds_menu(user):
    print(f"\n--- Funds & History for {user} ---")
    acc_num = input("Enter your account number: ")

    while True:
        print("\n1. Transfer Funds")
        print("2. View Transaction History")
        print("3. Filter Transactions")
        print("4. Generate Report")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            funds.transfer_funds(acc_num)
        elif choice == "2":
            funds.view_transaction_history(acc_num)
        elif choice == "3":
            funds.filter_transactions(acc_num)
        elif choice == "4":
            funds.generate_transaction_report(acc_num)
        elif choice == "5":
            break
        else:
            print("Invalid option.")