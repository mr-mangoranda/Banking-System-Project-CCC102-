import hashlib
import re
from utils.file_io import read_json, write_json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_username(username):
    return bool(re.match(r'^\w{3,20}$', username))

def validate_phone(phone):
    return bool(re.match(r'^\d{10,15}$', phone))

def register_user():
    users = read_json("data/users.json")

    print("\n=== Register ===")
    username = input("Enter username (3-20 characters, no spaces): ")
    if not validate_username(username):
        print("Invalid username format.")
        return

    if username in users:
        print("Username already exists.")
        return

    password = input("Enter password: ")
    confirm = input("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return

    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    if not validate_phone(phone):
        print("Invalid phone number format. Use digits only.")
        return

    hashed_pw = hash_password(password)

    profile = {
        "password": hashed_pw,
        "address": address,
        "phone": phone,
        "accounts": []
    }

    users[username] = profile
    write_json("data/users.json", users)
    print("Registration successful!")

def login():
    users = read_json("data/users.json")

    print("\n=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("User not found.")
        return None

    if users[username]["password"] != hash_password(password):
        print("Incorrect password.")
        return None

    print(f"Welcome back, {username}!")
    return username

def update_profile(username):
    users = read_json("data/users.json")

    if username not in users:
        print("User not found.")
        return

    print("\n=== Update Profile ===")
    address = input("Enter new address: ")
    phone = input("Enter new phone number: ")
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return

    users[username]["address"] = address
    users[username]["phone"] = phone
    write_json("data/users.json", users)
    print("Profile updated successfully.")

def create_account(username):
    users = read_json("data/users.json")
    accounts = read_json("data/accounts.json")

    if username not in users:
        print("User not found.")
        return

    account_number = input("Enter new account number (must be unique): ")
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

    print(f"Account {account_number} created successfully for {username}.")
