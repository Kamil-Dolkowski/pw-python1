# import hashlib

# text_to_hash = "Hello, World!"
# hash_object = hashlib.sha256(text_to_hash.encode())
# hash_value = hash_object.hexdigest()
# print(hash_value)

#---------------------------------------------------

# zmienna = 1
# print(hash(zmienna))    # 1

# zmienna = 1.0
# print(hash(zmienna))    # 1

#---------------------------------------------------

# import hashlib

# # Dynamiczne wybieranie algorytmu hashującego
# hash_type = "sha1"
# dynamic_hash = hashlib.new(hash_type)
# dynamic_hash.update(b"Hello, World!")
# print(dynamic_hash.hexdigest())

#---------------------------------------------------

# class Product:
#     name: ''
#     quantity: 0


# prod1 = Product()
# prod2 = Product()

# print(id(prod1))
# print(id(prod2))

# print(hash(prod1))
# print(hash(prod2))

#---------------------------------------------------

# Hashowanie większych danych, np. plików

# import hashlib

# def hash_file(file_path):
#     hash_obj = hashlib.sha256()
#     with open(file_path, 'rb') as file:   # Otwórz plik w trybie binarnym
#         for chunk in iter(lambda: file.read(4096), b""):    # Czytaj plik blokami po ...
#             hash_obj.update(chunk)
#     return hash_obj.hexdigest()



# file_hash = hash_file('example.txt')
# print(file_hash)

#---------------------------------------------------

# Bezpieczeństwo haseł
# hashlib jest często używany z soleniem i funkcją pbkdf2_hmac -> zwiększenie bezpieczeństwa haseł przechowywanych w systemach

# import hashlib
# import os

# def secure_password_hash(password):
#     salt = os.urandom(16)   # Generuje bezpieczną sól
#     key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
#     return salt + key


# password = "bezpieczneHaslo123"
# hashed_password = secure_password_hash(password)
# print(hashed_password)

#---------------------------------------------------

# import hashlib
# sha1_hash = hashlib.sha1()
# sha1_hash.update(b"Hello")
# print(sha1_hash.hexdigest())

#---------------------------------------------------

# Zadanie
# System weryfikacji integralności pliku przy użyciu hashowania

# 1. Napisz funkcję w Pythonie, która oblicza hash SHA-256 dla pliku.
# 2. 
# 3.