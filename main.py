from modules import auth

def menu():
    logged_in = None

    while True:
        print("\n=== BANK SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Update Profile")
        print("4. Create Account")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            auth.register_user()
        elif choice == "2":
            logged_in = auth.login()
        elif choice == "3":
            if logged_in:
                auth.update_profile(logged_in)
            else:
                print("You must login first.")
        elif choice == "4":
            if logged_in:
                auth.create_account(logged_in)
            else:
                print("You must login first.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()