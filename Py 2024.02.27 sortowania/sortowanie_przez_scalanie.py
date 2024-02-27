# Sortowanie przez scalanie.

def join_sort(a,b):
    t = []
    end = len(a) + len(b) - 1
    for i in range(end):
        if a[0] < b[0]:
            x = a.pop(0)
        else:
            x = b.pop(0)
        t.append(x)

    if len(a) == 1:
        x = a.pop(0)
    else:
        x = b.pop(0)
    t.append(x)

    return t





a = [1,3,5,8]
b = [2,4,6,7,9]

x =join_sort(a,b)
print(x)




import time
import random

ile = 100
ile1 = int(ile/2)
arr1 = [random.randint(1,ile1) for _ in range(ile1)]
arr2 = [random.randint(1,ile1) for _ in range(ile1)]
start_time = time.time()
join_sort(arr1, arr2)
end_time = time.time()
print("\nCzas wykonania sortowania przez scalanie dla zbioru", ile, "to", end_time-start_time, "sekund.")






# w domu: 

# 1 2 3 4 5 6

# 12  34  56

#   123456