# Algorytm przez wstawianie.

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr



arr = [8,4,3,5,2,1]

x = insert_sort(arr)
print(x)










import time
import random

arr = [8,4,3,5,2,1]
insert_sort(arr)
print("\nPosortowana lista: ", arr)
ile = 10000
arr = [random.randint(1,ile) for _ in range(ile)]
start_time = time.time()
insert_sort(arr)
end_time = time.time()
print("Czas wykonania sortowania przez wstawianie dla zbioru", ile, "to", end_time-start_time, "sekund.")