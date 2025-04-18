import rsa
from Crypto.Cipher import AES
import base64

# Load the private key
def load_private_key():
    with open("private_key.pem", "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())

# Decrypt AES key with RSA private key
def decrypt_aes_key(encrypted_aes_key, private_key):
    return rsa.decrypt(encrypted_aes_key, private_key)

# Decrypt the message with AES
def decrypt_message_with_aes(encrypted_message, aes_key):
    nonce, tag, ciphertext = encrypted_message[:16], encrypted_message[16:32], encrypted_message[32:]
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

# Receive and decrypt email
def receive_and_decrypt_email():
    # Simulating receiving the encrypted email and AES key
    encrypted_aes_key_base64 = input("Enter the encrypted AES key: ").strip()
    encrypted_message_base64 = input("Enter the encrypted message: ").strip()

    # Decode the base64-encoded strings
    encrypted_aes_key = base64.b64decode(encrypted_aes_key_base64.encode())
    encrypted_message = base64.b64decode(encrypted_message_base64.encode())

    # Decrypt AES key with RSA private key
    private_key = load_private_key()
    aes_key = decrypt_aes_key(encrypted_aes_key, private_key)

    # Decrypt the message with AES
    decrypted_message = decrypt_message_with_aes(encrypted_message, aes_key)

    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    receive_and_decrypt_email()
