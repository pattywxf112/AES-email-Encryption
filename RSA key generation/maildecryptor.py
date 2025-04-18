import rsa
import base64

# Load your private key
with open("private_key.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Get the encrypted message
encrypted_input = input("Enter the encrypted email content: ")

# Decode and decrypt
try:
    encrypted_bytes = base64.b64decode(encrypted_input.encode())
    decrypted_message = rsa.decrypt(encrypted_bytes, private_key).decode()
    print("Decrypted Message:", decrypted_message)
except Exception as e:
    print("Decryption failed:", e)
