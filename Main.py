import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# Gmail Credentials 
# source: https://developers.google.com/gmail/imap/imap-smtp#:~:text=Incoming%20connections%20to%20the%20IMAP,port%20587%20(for%20TLS).
# Incoming connections to the IMAP server at imap.gmail.com:993 
# the POP server at pop.gmail.com:995 require SSL. 
# The outgoing SMTP server, smtp.gmail.com, supports TLS. If your client begins with plain text, before issuing the STARTTLS command, 
# use port 465 (for SSL), or port 587 (for TLS). <- we use port 465 for SSL
sender_email = "pattyworking04@gmail.com"
receiver_email = "napatara.wan@student.mahidol.edu"
password = os.getenv("MY_SECRET_PASSWORD")  # App Password, in google and not real password

# Message to encrypt
email_text = "Wisdom of Mahidol"
encryption_password = "strongpassword"  # Secret key for AES encryption (we should change this one, it is not a good password)
# new password will be public key and the receiver will use private key to decrypt.

# Encrypt the message
encrypted_message = encrypt_email(email_text, encryption_password) #use function from mail encryption.py

# Create Email
subject = "Encrypted Email from Python"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(encrypted_message, "plain"))

# Send Email using Gmail SMTP
try:
    with smtplib.SMTP("smtp.gmail.com", 465) as server: # we use SSL for ease of use, we are aware that it is not secured
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Encrypted Email Sent!")
except Exception as e:
    print(f"Error: {e}")
