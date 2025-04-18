import os
import rsa

def generate_keypair(bits=2048, save_path="."):
    public_key, private_key = rsa.newkeys(bits)
    
    pub_path = os.path.join(save_path, "public_key.pem")
    priv_path = os.path.join(save_path, "private_key.pem")

    with open(pub_path, "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1())
    with open(priv_path, "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1())

    print(f"Keys saved to:\n- Public: {pub_path}\n- Private: {priv_path}")

if __name__ == "__main__":
    folder = input("Enter the path to save RSA keys: ").strip()
    if os.path.isdir(folder):
        generate_keypair(save_path=folder)
    else:
        print("Invalid path.")
