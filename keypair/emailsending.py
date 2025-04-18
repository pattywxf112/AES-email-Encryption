import smtplib
import os
import rsa
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

load_dotenv()

# Load public key for encryption
def load_public_key():
    with open("public_key.pem", "rb") as f:
        return rsa.PublicKey.load_pkcs1(f.read())

# Encrypt the message using AES
def encrypt_message_with_aes(message, aes_key):
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return cipher.nonce + tag + ciphertext

# Encrypt AES key with the recipient's public RSA key
def encrypt_aes_key(aes_key, public_key):
    encrypted_aes_key = rsa.encrypt(aes_key, public_key)
    return encrypted_aes_key

# Send encrypted email
def send_encrypted_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = os.getenv("MY_SECRET_PASSWORD")

    # Email content
    email_text = "Wisdom of Mahidol"

    # Generate AES key
    aes_key = get_random_bytes(32)  # 256-bit AES key

    # Encrypt the message with AES
    encrypted_message = encrypt_message_with_aes(email_text, aes_key)

    # Encrypt the AES key using RSA
    public_key = load_public_key()
    encrypted_aes_key = encrypt_aes_key(aes_key, public_key)

    # Encode encrypted AES key and message for transmission
    encrypted_aes_key_base64 = base64.b64encode(encrypted_aes_key).decode()
    encrypted_message_base64 = base64.b64encode(encrypted_message).decode()

    # Prepare the email
    subject = "Encrypted Email with RSA and AES"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(f"Encrypted AES Key: {encrypted_aes_key_base64}\nEncrypted Message: {encrypted_message_base64}", "plain"))

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Encrypted Email Sent!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_encrypted_email()
