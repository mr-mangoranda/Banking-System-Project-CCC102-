# modules/auth.py
import hashlib
import uuid
from utils.file_io import read_json, write_json

class Customer:
    def __init__(self, email, name, phone, address, password):
        self.email = email
        self.name = name
        self.phone = phone
        self.address = address
        self.password = self.hash_password(password)
        self.accounts = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        return {
            "password": self.password,
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "accounts": self.accounts
        }

def register_user():
    users = read_json("data/users.json")
    email = input("Enter your email: ").strip()

    if email in users:
        print("User already exists.")
        return

    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    customer = Customer(email, name, phone, address, password)
    users[email] = customer.to_dict()
    write_json("data/users.json", users)

    print("Registration successful!")

def login():
    users = read_json("data/users.json")
    email = input("Enter email: ").strip()
    password = input("Enter password: ")
    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    user = users.get(email)
    if user and user["password"] == hashed_input:
        print(f"Welcome back, {user['name']}!")
        return email  # Logged-in user email
    else:
        print("Invalid credentials.")
        return None

def update_profile(email):
    users = read_json("data/users.json")
    user = users.get(email)

    if not user:
        print("User not found.")
        return

    print("Update Profile:")
    user["phone"] = input("New phone: ")
    user["address"] = input("New address: ")

    users[email] = user
    write_json("data/users.json", users)
    print("Profile updated.")

def create_account(email):
    users = read_json("data/users.json")
    user = users[email]

    acc_type = input("Enter account type (checking/savings): ").lower()
    if acc_type in user["accounts"]:
        print(f"{acc_type.capitalize()} account already exists.")
        return

    acc_number = "ACC" + str(uuid.uuid4().int)[0:8]
    user["accounts"][acc_type] = acc_number
    users[email] = user
    write_json("data/users.json", users)

    accounts = read_json("data/accounts.json")
    accounts[acc_number] = {
        "balance": 0.0,
        "type": acc_type,
        "owner": email
    }
    write_json("data/accounts.json", accounts)

    print(f"{acc_type.capitalize()} account created: {acc_number}")
