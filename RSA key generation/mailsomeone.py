import smtplib
import os
import rsa
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, dotenv_values
import base64

load_dotenv()

with open("public_key.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

# Gmail Credentials 
# source: https://developers.google.com/gmail/imap/imap-smtp#:~:text=Incoming%20connections%20to%20the%20IMAP,port%20587%20(for%20TLS).
# Incoming connections to the IMAP server at imap.gmail.com:993 
# the POP server at pop.gmail.com:995 require SSL. 
# The outgoing SMTP server, smtp.gmail.com, supports TLS. If your client begins with plain text, before issuing the STARTTLS command, 
# use port 465 (for SSL), or port 587 (for TLS). <- we use port 465 for SSL
sender_email = "nagunsantisurntornkul@gmail.com"
receiver_email = "nagunsantisurntornkul@gmail.com"
password = os.getenv("MY_SECRET_PASSWORD")  # App Password, in google and not real password
# https://www.youtube.com/watch?v=8dlQ_nDE7dQ

# Message to encrypt
email_text = "Wisdom of Mahidol"
encrypted_message = rsa.encrypt(email_text.encode(), public_key) # Secret key for AES encryption
encrypted_message_base64 = base64.b64encode(encrypted_message).decode()
# new password will be public key and the receiver will use private key to decrypt.

# Create Email
subject = "Encrypted Email from Python"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(encrypted_message_base64, "plain"))

# Send Email using Gmail SMTP
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server: # we use SSL for ease of use, we are aware that it is not secured
         server.starttls()
         server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, message.as_string())
         print("Encrypted Email Sent!")
except Exception as e:
    print(f"Error: {e}")
