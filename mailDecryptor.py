# This file receive and decrype email
# Example: Decrypt the received email
received_encrypted_email = input("Enter the encrypted email content: ")
decryption_password = "strongpassword"  # Must match sender's encryption password

# Decrypt the message
decrypted_message = decrypt_email(received_encrypted_email, decryption_password)
print("Decrypted Email Content:", decrypted_message)
