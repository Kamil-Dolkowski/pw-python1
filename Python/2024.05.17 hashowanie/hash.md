
# Hashowanie

#---------------------------------------------------------------------------

bezpieczeństwo danych, wyszukiwanie

proces hashowania przekształca dane wejściowe, niezależnie od ich rozmiaru, w skrócony, stały ciąg zanków, znany jako wartośc hash

#---------------------------------------------------------------------------

Wartość hash jest generowana przez funkcję hashującą

ważna cecha -> funkcje hashujące są jednokierunkowe, jest to proces nieodwracalny

#---------------------------------------------------------------------------

# Właściwości funkcji hashujących:
-determinizm - dla danej wartości wejściowej zawsze ta sama wartość wyjściowa
-szybkość obliczeń
-nietrwałość (pre-image resistance)
-odporność na kolizje
-bezpieczeństwo małych zmian (avalanche effect)

#---------------------------------------------------------------------------

# Zastosowania:
-bezpieczeństwo danych - hashowanie haseł przed ich zapisywaniem w bazie danych zapewnia, że oryginalne hasła nie są nigdzie przechowywane w jawnej formie
-weryfikacja integralności - sprawdzanie, czy dane nie zostały zmienionepodczas przechowywania lub transmisji
-systemy baz danych - szybkie porównywanie złożonych zapytań lub dużych objętości danych bez konieczności ich pełnego przeglądania
-kasze i tablice mieszające - efektywne przechowywanie i odnajdywanie elementów w strukturach danych

#---------------------------------------------------------------------------

Python
moduł hashlib - standardowa biblioteka
SHA-1, SHA-256, MD5


#- - - - - - - - - 

import hashlib

text_to_hash = "Hello, World!"
hash_object = hashlib.sha256(text_to_hash.encode())
hash_value = hash_object.hexdigest()
print(hash_value)

#- - - - - - - - - 

zmienna = 1
print(hash(zmienna))    // 1

zmienna = 1.0
print(hash(zmienna))    // 1

#- - - - - - - - - 

# Dynamiczne wybieranie algorytmu hashującego

import hashlib

hash_type = "sha1"
dynamic_hash = hashlib.new(hash_type)
dynamic_hash.update(b"Hello, World!")
print(dynamic_hash.hexdigest())

#- - - - - - - - -

class Product:
    name: ''
    quantity: 0


prod1 = Product()
prod2 = Product()

print(id(prod1))
print(id(prod2))

print(hash(prod1))
print(hash(prod2))

#- - - - - - - - -

# Hashowanie większych danych, np. plików

import hashlib

def hash_file(file_path):
    hash_obj = hashlib.sha256()
    with open(file_path, 'rb') as file:   # Otwórz plik w trybie binarnym
        for chunk in iter(lambda: file.read(4096), b""):    # Czytaj plik blokami po ...
            hash_obj.update(chunk)
    return hash_obj.hexdigest()



file_hash = hash_file('example.txt')
print(file_hash)

#- - - - - - - - -

# Bezpieczeństwo haseł
# hashlib jest często używany z soleniem i funkcją pbkdf2_hmac -> zwiększenie bezpieczeństwa haseł przechowywanych w systemach

import hashlib
import os

def secure_password_hash(password):
    salt = os.urandom(16)   # Generuje bezpieczną sól
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + key


password = "bezpieczneHaslo123"
hashed_password = secure_password_hash(password)
print(hashed_password)


#---------------------------------------------------------------------------

# Praktyczne zastosowania hashowania:

-Bezpieczeństwo haseł:
najpowszechniejsze zastosowanie -> przechowywanie haseł
zamiast przechowywać hasła w postaci jawnej, systemy bezpieczeństwa przechowują ich hashowaną wersję
zapobieganie wykradzeniu haseł 

-Weryfikacja integralności danych:

-Tablice hashujące:

-Cache'owanie:
szybki dostęp do często używanych zasobów

-Wykrywanie duplikatów:
identyfikacja i eliminacja duplikatów

#---------------------------------------------------------------------------

# Best practise:
-Wybieraj nowoczesne algorytmy (bezpieczne, sprawdzone: SHA-256) (przestarzałe i potancjalnie niebezpieczne: MD-5, SHA-1)
-Używaj salt 
-Ogranicz ryzyko kolizji
-Bezpieczne przechowywanie kluczy
-Testuj wydajność



ataki brute force

odszyfrowywanie hashy -> ?

#---------------------------------------------------------------------------

# Podstawowe zastosowania hashowania:
-zapewnienie integralności danych
zapewnienie, że dane nie zostały zmienione
-szybkie porównywanie dużych zestawów danych
-bezpieczne przechowywanie haseł
bezpieczne przechowywanie haseł w bazach danych
-moduł hashlib w pythonie
hashlib.new()
hashlib.algorithms_available
hashlib.guaranteed



import hashlib
sha1_hash = hashlib.sha1()
sha1_hash.update(b"Hello")
print(sha1_hash.hexdigest())

#---------------------------------------------------------------------------


