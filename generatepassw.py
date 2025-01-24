

import random
import string

def generate_password(length):
   
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    
    all_characters = upper + lower + digits + special

   
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

password_length = 12
random_password = generate_password(password_length)
print("Generated Password:", random_password)

