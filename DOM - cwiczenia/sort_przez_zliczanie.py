# Sortowanie przez zliczanie (kubełkowe ?)

# Dane: zbiór liczb całkowitych o ograniczonym zakresie wartości

def sort_przez_zliczanie(arr):
    tl = []      # tablica liczników
    t = []       # tablica posortowana
    y_min = min(arr)
    y_max = max(arr)
    len_tl = y_max - y_min + 1

    for i in range(len_tl):
        tl.append(0)

    for liczba in arr:
        l1 = y_min
        for i in range(len_tl):
            if liczba == l1:
                tl[i] += 1
                break
            l1 += 1
    
    l1 = y_min
    for i in range(len_tl):
        x = tl[i]
        if x != 0:
            for j in range(x):
                t.append(l1)
        l1 += 1

    return t
    




t = [1,6,8,1,2,-2,4,7,2,1,0,3]
print("Zbiór przed posortowaniem: ")
print(t)
x = sort_przez_zliczanie(t)
print("\nZbiór po posortowaniu: ")
print(x)



# tl = [1,2,3,4,5,6,7,8,9]
#       ^               ^
#      min             max