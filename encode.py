from cryptography.fernet import Fernet
import base64, hashlib
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename,"wb") as file:
        file.write(decrypted_data)
password = input("Enter password: ")
my_password = password.encode()
key = hashlib.md5(my_password).hexdigest()
key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))
file = "2Аф.txt"
# encrypt(file,key_64)
decrypt(file,key_64)

