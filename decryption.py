import rsa
from Crypto.Cipher import AES
import base64

# Load the private key from a file path
def load_private_key(path):
    with open(path, "rb") as f:
        return rsa.PrivateKey.load_pkcs1(f.read())

# Decrypt the AES key using the RSA private key
def decrypt_aes_key(encrypted_aes_key, private_key):
    return rsa.decrypt(encrypted_aes_key, private_key)

# Decrypt the message using AES GCM mode
def decrypt_message_with_aes(encrypted_message, aes_key):
    # GCM format: nonce (16 bytes) + tag (16 bytes) + ciphertext
    nonce = encrypted_message[:16]
    tag = encrypted_message[16:32]
    ciphertext = encrypted_message[32:]
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

# Decrypt flow with user input
def receive_and_decrypt_email():
    print("Paste base64-encoded encrypted message and AES key below:\n")
    encrypted_message_b64 = input("Encrypted Message: ").strip()
    aes_key_b64 = input("AES Key (Base64): ").strip()
    private_key_path = input("Path to private key file (e.g., private_key.pem): ").strip()

    try:
        # Decode from base64
        encrypted_message = base64.b64decode(encrypted_message_b64.encode())
        aes_key = base64.b64decode(aes_key_b64.encode())

        # Load private key (even though we don’t use it for AES in this test version)
        private_key = load_private_key(private_key_path)

        # Decrypt the message
        decrypted_message = decrypt_message_with_aes(encrypted_message, aes_key)

        print("\nDecrypted Message:")
        print(decrypted_message)

    except Exception as e:
        print(f"\nDecryption failed: {e}")

# Run when executed
if __name__ == "__main__":
    receive_and_decrypt_email()
