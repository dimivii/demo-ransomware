import random

# generate key
key = ''
encryption_level = 512 // 8
char_pool = ''
for i in range(0x00, 0xFF):
    char_pool += (chr(i))
for i in range(encryption_level):
    key += random.choice(char_pool)
    
print(key)