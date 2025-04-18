import rsa

# Generate RSA key pair
def generate_keypair(bits=2048):
    public_key, private_key = rsa.newkeys(bits)
    
    # Save the keys to files (optional, for persistent use)
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1())
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1())
    
    return private_key, public_key

# Run key generation and check if it's successful
private_key, public_key = generate_keypair()  # Call the function to generate the keypair

print("Public Key:", public_key)
print("Private Key:", private_key)
