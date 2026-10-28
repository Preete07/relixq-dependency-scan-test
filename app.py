//test code -2
from cryptography.fernet import Fernet
def encrypt_message(message: bytes) -> bytes:
    key = Fernet.generate_key()
    cipher = Fernet(key)
    return cipher.encrypt(message)
def decrypt_message(encrypted_message: bytes, key: bytes) -> bytes:
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message)
if __name__ == "__main__":
    key = Fernet.generate_key()
    cipher = Fernet(key)

    message = b"Testing RelixQ webhook-triggered scans"
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)
    print("Encryption completed")
    print("Decryption completed")
    print(decrypted.decode())
