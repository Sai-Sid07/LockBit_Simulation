import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

main_dir = os.getenv("CORE_DIR")

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)


encryptor=Encryptor()

mykey=encryptor.key_create()

encryptor.key_write(mykey, 'mykey.key')

loaded_key = encryptor.key_load('mykey.key')
for curdir, dirs, files in os.walk(main_dir):
    for filename in files:
        curfile = os.path.join(curdir, filename)
        encryptor.file_encrypt(loaded_key, curfile,curfile)
        with open("entropyCalculation.py") as f:
            exec(f.read())

# encryptor.file_decrypt(loaded_key, 'enc_testing.txt', 'dec_testing.txt')