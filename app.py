from cryptography.fernet import Fernet

def encrypt_message(message: bytes) -> bytes:
    key = Fernet.generate_key()
    cipher = Fernet(key)
    return cipher.encrypt(message)

if __name__ == "__main__":
    encrypted = encrypt_message(b"RelixQ dependency scan test")
    print("Encryption completed")
