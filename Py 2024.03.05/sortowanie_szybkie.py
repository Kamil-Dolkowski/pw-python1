# Sortowanie szybkie (quick sort)

# pivot - liczba, która dzieli tablicę

import random
import time

def median(arr):
    return sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    # pivot = random.choice(arr)
    pivot = median(arr)

    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)





t = [9,3,6,2,8,5,5]


x = quick_sort(t)
print(x)




# Tablica z losowymi liczbami

ile = 10000
arr = [random.randint(1,ile) for _ in range(ile)]
start_time = time.time()
wynik = quick_sort(arr)
end_time = time.time()
print("Czas wykonania sortowania szybkiego dla zbioru", ile, "to", end_time-start_time, "sekund.\n")





# Posortowana tablica

# ile = 1000
# arr = list(range(ile))
# print(arr[:10])
# start_time = time.time()
# wynik = quick_sort(arr)
# end_time = time.time()
# print("Czas wykonania sortowania szybkiego dla zbioru", ile, "to", end_time-start_time, "sekund.\n")





# Tablica z tymi samymi wartościami

ile = 100
arr = [3] * ile
print(arr[:10])
start_time = time.time()
wynik = quick_sort(arr)
end_time = time.time()
print("Czas wykonania sortowania szybkiego dla zbioru", ile, "to", end_time-start_time, "sekund.\n")


