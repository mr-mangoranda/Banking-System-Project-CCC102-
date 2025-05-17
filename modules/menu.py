from modules import auth, transaction, funds, loan, admin

def main_menu():
    while True:
        print("\n=== BANK SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Admin Login")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            auth.register_user()
        elif choice == "2":
            user = auth.login()
            if user:
                user_menu(user)
        elif choice == "3":
            admin_user = auth.admin_login()
            if admin_user:
                admin_menu()
        elif choice == "0":
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

def loan_menu(user):
    while True:
        print("\n=== Loan Menu ===")
        print("1. Apply for Loan")
        print("2. View Loan Status")
        print("3. Make Loan Payment")
        print("4. Back")

        choice = input("Choose an option: ")
        if choice == "1":
            loan.apply_for_loan(user)
        elif choice == "2":
            loan.view_loan_status(user)
        elif choice == "3":
            loan.make_loan_payment(user)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Approve Loans")
        print("2. View All Users")
        print("3. View All Accounts")
        print("4. View All Transactions")
        print("5. View All Loans")
        print("6. Back")

        choice = input("Choose an option: ")
        if choice == "1":
            admin.approve_loans()
        elif choice == "2":
            admin.view_all_users()
        elif choice == "3":
            admin.view_all_accounts()
        elif choice == "4":
            admin.view_all_transactions()
        elif choice == "5":
            admin.view_all_loans()
        elif choice == "6":
            break
        else:
            print("Invalid option.")
