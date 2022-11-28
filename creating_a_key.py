from cryptography.fernet import Fernet
import os

# we need a key to encrypt and decrypt files
key = ''
c = Fernet.generate_key()
print(c)