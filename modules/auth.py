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