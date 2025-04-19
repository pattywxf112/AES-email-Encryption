# emailsending.py

import smtplib
import os
import rsa
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Load .env file and retrieve email password
load_dotenv()
password = os.getenv("MY_SECRET_PASSWORD")

# Load public RSA key from PEM file
def load_public_key():
    with open("public_key.pem", "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())

# Encrypt the message using AES GCM mode
def encrypt_message_with_aes(message, aes_key):
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return cipher.nonce + tag + ciphertext  # Combine parts into one encrypted blob

# Encrypt AES key with RSA public key
def encrypt_aes_key(aes_key, public_key):
    return rsa.encrypt(aes_key, public_key)

# Send encrypted email with encrypted message + AES key
def send_encrypted_email():
    sender_email = "nagunsantisurntornkul@gmail.com"
    receiver_email = "nagunsantisurntornkul@gmail.com"
    email_text = "Wisdom of the Land"

    # Generate 256-bit AES key
    aes_key = get_random_bytes(32)

    # Encrypt the message with AES
    encrypted_message = encrypt_message_with_aes(email_text, aes_key)

    # Encrypt the AES key with RSA
    public_key = load_public_key()
    encrypted_aes_key = encrypt_aes_key(aes_key, public_key)

    # Base64-encode both for sending via email
    encrypted_aes_key_b64 = base64.b64encode(encrypted_aes_key).decode()
    encrypted_message_b64 = base64.b64encode(encrypted_message).decode()
    aes_key_b64 = base64.b64encode(aes_key).decode()  # Send AES key in plaintext for test

    # Compose email content
    subject = "Encrypted Email with RSA and AES"
    body = (
        f"Encrypted Message: {encrypted_message_b64}\n"
        f"AES Key (Base64): {aes_key_b64}\n\n"
        "Use this AES key and the private key to decrypt the message."
    )

    # Prepare MIME email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email using SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Encrypted email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Run when executed
if __name__ == "__main__":
    send_encrypted_email()
