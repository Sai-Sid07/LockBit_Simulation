import os
import base64
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

load_dotenv()

user_directory = os.getenv("DIRECTORY")

filesData = os.walk(user_directory)

with open('mykey.key', 'rb') as mykey:
    encoded_key = mykey.read()

with open('iv.key', 'rb') as myIV:
    iv = myIV.read()

key = base64.urlsafe_b64decode(encoded_key)

f = Fernet(encoded_key)

# Create an AES256 cipher object with the key and IV
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

for root, directories, files in filesData:
    for file in files:
        if file.startswith("enc_"):
            encSourcePath = root + "\\" + file
            # Inorder to differentiate between the decrypted and base files, the decrypted files will have a 
            # dec_ prefix attached to them
            decSourcePath = root + "\\dec_" + file[4:] # This is done to remove enc prefix

            with open(encSourcePath, 'rb') as encrypted_file:
                encrypted = encrypted_file.read()

            # Decrypt the data using AES256-CBC mode
            decryptor = cipher.decryptor()
            decrypted_padded_data = decryptor.update(encrypted) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

            with open(decSourcePath, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)