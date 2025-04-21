import os
import rsa

# Generate RSA key pair
def generate_keypair(bits=2048, save_path="."):
    public_key, private_key = rsa.newkeys(bits)

    pub_path = os.path.join(save_path, "public_key.pem")
    priv_path = os.path.join(save_path, "private_key.pem")

    with open(pub_path, "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1()) #returns the key in PKCS#1 format, a standard for encoding RSA keys.

    with open(priv_path, "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1()) #returns the key in PKCS#1 format, a standard for encoding RSA keys.

    print(f"\nRSA keys generated successfully:")
    print(f"Public Key: {pub_path}")
    print(f"Private Key: {priv_path}")

if __name__ == "__main__":
    folder = input("Enter the path to the folder to save RSA keys: ").strip()
    if os.path.isdir(folder):
        generate_keypair(save_path=folder)
    else:
        print("That folder does not exist.")

# import os
# import rsa

# def generate_keypair(bits=2048, save_path="."):
#     public_key, private_key = rsa.newkeys(bits)

#     pub_path = os.path.join(save_path, "public_key.pem")
#     priv_path = os.path.join(save_path, "private_key.pem")

#     with open(pub_path, "wb") as pub_file:
#         pub_file.write(public_key.save_pkcs1())

#     with open(priv_path, "wb") as priv_file:
#         priv_file.write(private_key.save_pkcs1())

#     print(f"\nRSA keys generated successfully:")
#     print(f"• Public Key: {pub_path}")
#     print(f"• Private Key: {priv_path}")

# if __name__ == "__main__":
#     try:
#         folder = input("Enter the path to the folder to save RSA keys: ").strip()

#         if os.path.isdir(folder):
#             generate_keypair(save_path=folder)
#         else:
#             print("That folder does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

#     # Keep the terminal open until user confirms
#     input("\nPress Enter to close this window...")