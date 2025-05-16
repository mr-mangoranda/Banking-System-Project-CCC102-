import hashlib
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
            'email': self.email,
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'password': self.password,
            'accounts': self.accounts
        }
    
    def register_user():
        users = read_json('data/users.json')

        email = input("Enter your email: ").strip()
        if email in users:
            print("Users already registered.")
            return
        
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")

        new_customer = Customer(email, name, phone, address, password)
        users[email] = new_customer.to_dict()

        write_json('data/users.json', users)
        print("User registered successfully.")

    def login():
        users = read_json('data/users.json')

        email = input("Enter your email: ").strip()
        password = input("Enter your password: ")
        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        user = users.get(email)
        if user and user ['password'] == hashed_input:
            print(f"Welcome back, {user['name']}!")
            return email
        else:
            print("Invalid email or password.")
            return None
        
    def update_profile(email):
        users = read_json('data/users.json')
        user = users.get(email)

        if not user:
            print("User not found.")
            return
        
        print("Update Profile:")
        user['phone'] = input("New phone number: ")
        user['address'] = input("New address: ")

        users[email] = user 
        write_json('data/users.json', users)
        print("Profile updated successfully.")

    def create_account(email):
        users = read_json('data/users.json')
        user = users[email]

        acc_type = input("Enter account type (checking/savings): ").lower()
        if acc_type in user["accounts"]:
            print(f"{acc_type.capitalize()} account already exists.")
            return
        
        acc_number = "ACC" + str(uuid.uuid4().int)[0:8]
        user["accounts"][acc_type] = acc_number
        users[email] = user
        write_json('data/users.json', users)

        accounts = read_json('data/accounts.json')
        accounts[acc_number] = {
            "balance": 0.0,
            "type": acc_type,
            "owner": email
        }
        write_json('data/accounts.json', accounts)

        print(f"{acc_type.capitalize()} account created: {acc_number}")
        return acc_number
    
