from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

# Function to generate a strong encryption key
def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to encrypt an email message
def encrypt_email(email_text: str, password: str):
    salt = os.urandom(16)  # Generate random salt
    key = generate_key(password, salt)  # Generate key
    iv = os.urandom(16)  # Initialization vector (IV)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding to make message a multiple of 16 bytes
    padded_text = email_text + " " * (16 - len(email_text) % 16)
    ciphertext = encryptor.update(padded_text.encode()) + encryptor.finalize()

    # Encode to Base64 for sending as text
    encrypted_message = base64.b64encode(salt + iv + ciphertext).decode()
    return encrypted_message

# Function to decrypt an email message
def decrypt_email(encrypted_email: str, password: str):
    encrypted_data = base64.b64decode(encrypted_email)

    salt = encrypted_data[:16]  # Extract salt
    iv = encrypted_data[16:32]  # Extract IV
    ciphertext = encrypted_data[32:]  # Extract encrypted text

    key = generate_key(password, salt)  # Regenerate key

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_text.decode().strip()  # Remove padding
