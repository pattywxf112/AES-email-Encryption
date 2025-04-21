# AES email Encryption
 send encrypted email and generate key with AES

# required library installation for python
- pip install rsa 
- pip install pycryptodome
- pip install python-dotenv ( DONT FORGET TO CREATE .ENV FILE)

# Manual
- clone this repository to your computer
- prepare gmail account app assword and store in .env, NEVER USE YOUR OWN PERSONAL PASSWORD
- put sender email (the gmail account used with .env file), and receiver email which could also be sender email, and the message in emailsending.py
- take all run each programs with python, generate key pairs using genkey.py or coolergenkey.py (coolergenkey.py is easier to use)
- store your key pair in the root foulder once generated, you can generate key pair in root foulder path.
- run emailsending.py once you have key pairs in the root foulder. remove older key pair and generate new one if it does not work.
- open your mail box and input ann information you want into decryption.py, it would ask your AES key, RSA private key and encrypted cipher text you want to decrypt.
- the message is decrypted and it works like charms!


# Project requirement
1) Technology used e.g. software, programming language, algorithm, etc.  
2) Details of the design 
3) Demo showing the implementation 
4) References 

## Technologies Used:
- RSA (public-key encryption)
- AES (symmetric encryption)
- SMTP (sending emails)
- Base64 (encoding/decoding data)
- python-dotenv (environment variable management)
- smtplib (email sending)
- pycryptodome (AES encryption)
- rsa (RSA encryption and key generation)
- Python (programming language)

## References
# RSA (Rivest-Shamir-Adleman)
- lirary: https://pypi.org/project/rsa/
- Rivest, R. L., Shamir, A., & Adleman, L. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. Communications of the ACM, 21(2), 120-126. https://doi.org/10.1145/359340.359342

# AES (Advanced Encryption Standard)
- https://pypi.org/project/pycryptodome/
- Daemen, J., & Rijmen, V. (2002). The Design of Rijndael: AES - The Advanced Encryption Standard. Springer. DOI: 10.1007/3-540-45708-9

# SMTP (Simple Mail Transfer Protocol)
- https://docs.python.org/3/library/smtplib.html
- Klensin, J. (2008). RFC 5321 - Simple Mail Transfer Protocol. Internet Engineering Task Force (IETF). RFC 5321

# Base64 Encoding
- https://docs.python.org/3/library/base64.html
- Williams, S. (1994). RFC 2045 - Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies. Internet Engineering Task Force (IETF). RFC 2045

# Environment Variable Management
- https://pypi.org/project/python-dotenv/
- python-dotenv (Python library for managing environment variables).

# Python Programming Language
- https://docs.python.org/3/
- Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. Network Theory Ltd.