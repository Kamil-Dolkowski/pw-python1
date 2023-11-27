import random
i=random.randint(1,10)
print(i)

fruits=["banan","jabłko","cytryna"]
choice=random.choice(fruits)
print(choice)

t=[1,2,3,4,5]
random.shuffle(t)
print(t)

# -------------------------------- time
import time
now = time.time()
print(now)


# --------------------------------- os
import os
for file in os.listdir():
    print(file)

file_path = "Readme.md"
if os.path.exists(file_path):
    print("Plik istnieje.")

print(os.listdir('Py 07.11.2023'))



with open("nowy_plik.txt", "w") as f:
    f.write("To jest nowy plik")


# -------------------------------- calendar
# import calendar
# print(calendar.calendar(theyear=2023, w=2, l=1, c=2, m=6))