import math
from math import sqrt

print(math.sqrt(10))


# pierw=math.sqrt(10)
# print(pierw)

# kwadr=pierw**2

# print(kwadr)






import random

# Generowanie losowej liczby całkowitej z zakresu: 1-100:
print(random.randint(1,100))

# Wybór losowego elementu z listy:
fruits=["apple","banana","orange"]
print(random.choice(fruits))

# Mieszanie listy:
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)







# Zwrócenie bieżącego czasu w sekundach:
import time
print(time.time())






# Zwrócenie bieżącej daty i godziny:
import datetime
now = datetime.datetime.now()
print(now)

# napisz program, który sprawdza, czy dany format daty jest prawidłowy
# 'dd-mm-yyyy'
todays_date = datetime.date.today()
print(todays_date)


    # %Y - year [0001,..., 2018,2019,..., 9999]
    # %m - month [01,02, ..., 11, 12]
    # %d - day [01,02, ..., 30, 31]
    # %H - hour
    #










# Napisz kod, który wypisze listę wszystkich plików w bieżącym katalogu:
import os
for file in os.listdir():
    print(file)

# Czy plik istnieje?:
file_path = "repo.py"
if os.path.exists(file_path):
    print('file already exists')

print(os.path.isfile(file_path))

print(os.listdir('Py 06.11.2023'))


# os.rename(file_path, file_path+"nowy_plik.txt")

# os.mkdir("utworz_katalog")
# os.rmdir("usun_katalog")


with open("nowy_plik.txt", "w") as f:
    f.write("To jest nowy plik")




