import hashlib
from utils.file_io import read_json, write_json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    users = read_json("data/users.json")

    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
        return

    password = input("Enter password: ")
    hashed_pw = hash_password(password)

    profile = {
        "password": hashed_pw,
        "address": input("Enter address: "),
        "phone": input("Enter phone number: "),
        "accounts": []  
    }

    users[username] = profile
    write_json("data/users.json", users)
    print("Registration successful.")

def login():
    users = read_json("data/users.json")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("User not found.")
        return None

    if users[username]["password"] != hash_password(password):
        print("Incorrect password.")
        return None

    print("Login successful.")
    return username

def update_profile(username):
    users = read_json("data/users.json")

    if username not in users:
        print("User not found.")
        return

    print("\nUpdate Profile:")
    address = input("Enter new address: ")
    phone = input("Enter new phone number: ")

    users[username]["address"] = address
    users[username]["phone"] = phone
    write_json("data/users.json", users)
    print("Profile updated.")

def create_account(username):
    users = read_json("data/users.json")
    accounts = read_json("data/accounts.json")

    if username not in users:
        print("User not found.")
        return

    account_number = input("Enter new account number: ")
    if account_number in accounts:
        print("Account number already exists.")
        return

    accounts[account_number] = {
        "owner": username,
        "balance": 0.0
    }

    users[username]["accounts"].append(account_number)

    write_json("data/accounts.json", accounts)
    write_json("data/users.json", users)

    print(f"Account {account_number} created successfully.")