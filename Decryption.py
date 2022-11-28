from cryptography.fernet import Fernet
import os

# we need a key to encrypt and decrypt files
key = 'tNJGmI_IDZDCN6YbohxKy3p_OQqeg2rsk0_1Squ7j8A='
c = Fernet.generate_key()
#print(c)
    
def Encrypt(file_name):
    lock = Fernet(key)
    with open(file_name, 'rb') as file:
        data = file.read()
    protected = lock.encrypt(data)
    with open(file_name, 'wb') as file:
        file.write(protected)
         
def Decrypt(file_name):
    unlock = Fernet(key)
    with open(file_name, 'rb') as file:
        data = file.read()
    decoded = unlock.decrypt(data)
    with open(file_name, 'wb') as file:
        file.write(decoded)
        
Raw_Files = os.listdir()
Files = list()

for File in Raw_Files:
    if File.endswith('.txt',): #getting all txt files
        Files.append(File)

function = Decrypt
        
for File in Files:
    function(File)