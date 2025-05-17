import bcrypt
import re
import os
import logging
from utils.file_io import read_json, write_json

# Setup logger
logger = logging.getLogger('banking_system_auth')
if not logger.hasHandlers():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def validate_username(username):
    return bool(re.match(r'^\w{3,20}$', username))

def validate_phone(phone):
    return bool(re.match(r'^\d{10,15}$', phone))

def validate_password_strength(password):
    # Password must be at least 8 characters, contain uppercase, lowercase, digit, and special char
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def sanitize_input(user_input):
    # Basic sanitization to strip leading/trailing spaces
    return user_input.strip()

def register_user():
    try:
        users = read_json("data/users.json")
    except Exception as e:
        logger.error(f"Failed to read users.json: {e}")
        users = {}

    print("\n=== Register ===")
    username = sanitize_input(input("Enter username: "))
    if not validate_username(username):
        print("Invalid username format.")
        return

    if username in users:
        print("Username already exists.")
        return

    password = input("Enter password: ")
    if not validate_password_strength(password):
        print("Password too weak. Must be at least 8 characters and include uppercase, lowercase, digit, and special character.")
        return

    confirm = input("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return

    address = sanitize_input(input("Enter address: "))
    phone = sanitize_input(input("Enter phone number: "))
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
    try:
        write_json("data/users.json", users)
        logger.info(f"User registered: {username}")
        print("Registration successful!")
    except Exception as e:
        logger.error(f"Failed to write users.json: {e}")
        print("Failed to save user data.")

def login():
    try:
        users = read_json("data/users.json")
    except Exception as e:
        logger.error(f"Failed to read users.json: {e}")
        print("Failed to load user data.")
        return None

    print("\n=== Login ===")
    username = sanitize_input(input("Enter username: "))
    password = input("Enter password: ")

    if username not in users:
        print("User not found.")
        return None

    if not verify_password(password, users[username]["password"]):
        print("Incorrect password.")
        return None

    logger.info(f"User logged in: {username}")
    print(f"Welcome back, {username}!")
    return username

def admin_login():
    print("\n=== Admin Login ===")
    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")

    username = sanitize_input(input("Enter admin username: "))
    password = input("Enter admin password: ")

    if username == admin_username and password == admin_password:
        logger.info("Admin login successful")
        print("Admin login successful!")
        return True
    else:
        logger.warning("Invalid admin login attempt")
        print("Invalid credentials.")
        return False

def update_profile(username):
    try:
        users = read_json("data/users.json")
    except Exception as e:
        logger.error(f"Failed to read users.json: {e}")
        print("Failed to load user data.")
        return

    if username not in users:
        print("User not found.")
        return

    print("\n=== Update Profile ===")
    address = sanitize_input(input("Enter new address: "))
    phone = sanitize_input(input("Enter new phone number: "))
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return

    users[username]["address"] = address
    users[username]["phone"] = phone
    try:
        write_json("data/users.json", users)
        logger.info(f"Profile updated for user: {username}")
        print("Profile updated successfully.")
    except Exception as e:
        logger.error(f"Failed to write users.json: {e}")
        print("Failed to save profile data.")

def create_account(username):
    try:
        users = read_json("data/users.json")
        accounts = read_json("data/accounts.json")
    except Exception as e:
        logger.error(f"Failed to read data files: {e}")
        print("Failed to load data.")
        return

    if username not in users:
        print("User not found.")
        return

    account_number = sanitize_input(input("Enter new account number (must be unique): "))
    if account_number in accounts:
        print("Account number already exists.")
        return

    print("Select account type:")
    print("1. Saving")
    print("2. Checking")
    account_type_choice = sanitize_input(input("Enter choice (1 or 2): "))
    if account_type_choice == "1":
        account_type = "Saving"
    elif account_type_choice == "2":
        account_type = "Checking"
    else:
        print("Invalid account type choice.")
        return

    accounts[account_number] = {
        "owner": username,
        "balance": 0.0,
        "type": account_type
    }

    users[username]["accounts"].append(account_number)

    try:
        write_json("data/accounts.json", accounts)
        write_json("data/users.json", users)
        logger.info(f"Account {account_number} ({account_type}) created for user: {username}")
        print(f"Account {account_number} ({account_type}) created successfully for {username}.")
    except Exception as e:
        logger.error(f"Failed to write data files: {e}")
        print("Failed to save account data.")
