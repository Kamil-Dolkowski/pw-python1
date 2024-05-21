# Zad.1
# Wprowadzenie hasła i wyświetlenie hashu hasła.

#- - - - - - - - - - - - - - - - - - - - - - - - - 

# password = input("Wprowadź hasło: ")
# hashed_password = hash(password)
# print(f"Zahashowane hasło: {hashed_password}")

# password = input("Wprowadź hasło: ")
# hashed_password = hash(password)
# print(f"Zahashowane hasło: {hashed_password}")

#---------------------------------------------------------------------------------------------------------

# Zad.2
# Hash z solą.

#- - - - - - - - - - - - - - - - - - - - - - - - - 

# import hashlib
# import os

# # Generuje bezpieczną sól
# salt = os.urandom(16)

# def secure_password_hash(password, salt):
#     key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
#     return salt + key


# password = input("\nWprowadź hasło: ")
# hashed_password = secure_password_hash(password, salt)
# print(hashed_password)

# password = input("Wprowadź hasło: ")
# hashed_password = secure_password_hash(password, salt)
# print(hashed_password)


#---------------------------------------------------------------------------------------------------------

# Zad.3
# Hash z solą + wybór algorytmu hashującego.

#- - - - - - - - - - - - - - - - - - - - - - - - - 

import hashlib
import os

# Generuje bezpieczną sól
salt = os.urandom(16)

def secure_password_hash(password, salt, algorithm):
    key = hashlib.pbkdf2_hmac(algorithm, password.encode(), salt, 100000)
    return salt + key


algorithm = 'sha256'

password = input("\nWprowadź hasło: ")
hashed_password = secure_password_hash(password, salt, algorithm)
print(hashed_password)

# algorithm = 'md5'

password = input("Wprowadź hasło: ")
hashed_password = secure_password_hash(password, salt, algorithm)
print(hashed_password)

