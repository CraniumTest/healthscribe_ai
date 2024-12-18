import os
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self, key_path='data/secret.key'):
        self.key = self.load_key(key_path)

    def load_key(self, path):
        if os.path.exists(path):
            with open(path, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(path, 'wb') as file:
                file.write(key)
            return key

    def encrypt_data(self, data):
        f = Fernet(self.key)
        return f.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        f = Fernet(self.key)
        return f.decrypt(encrypted_data).decode()
