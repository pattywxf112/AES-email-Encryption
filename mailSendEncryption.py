import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail Credentials
sender_email = "sender@gmail.com"
receiver_email = "recipient@gmail.com"
password = "your_app_password"  # Use Google App Password, NOT your real password

# Message to encrypt
email_text = "Wisdom of Mahidol"
encryption_password = "strongpassword"  # Secret key for AES encryption

# Encrypt the message
encrypted_message = encrypt_email(email_text, encryption_password)

# Create Email
subject = "Encrypted Email from Python"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(encrypted_message, "plain"))

# Send Email using Gmail SMTP
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Encrypted Email Sent!")
except Exception as e:
    print(f"Error: {e}")
