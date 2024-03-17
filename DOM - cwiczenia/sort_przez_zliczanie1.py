# Sortowanie przez zliczanie

# Dane: zbiór liczb całkowitych o ograniczonym zakresie wartości

def sort_przez_zliczanie(arr):
    tl = []      # tablica liczników
    t = []       # tablica posortowana
    y_min = min(arr)
    y_max = max(arr)
    len_tl = y_max - y_min + 1

    for i in range(len_tl):
        tl.append(0)

    for i in range(len(arr)):
        t.append(0)

    for liczba in arr:
        l1 = y_min
        for i in range(len_tl):
            if liczba == l1:
                tl[i] += 1
                break
            l1 += 1
    
    for i in range(1,len_tl):
        tl[i] += tl[i-1]

    for i in reversed(range(len(arr))):
        index = arr[i] - y_min            # index - index w tl, [y_min, y_max], y_min -> index=0
        t[tl[index]-1] = arr[i]
        tl[index] -= 1

    return t
    




t = [1,6,8,1,2,-2,4,7,2,1,0,3]
print("Zbiór przed posortowaniem: ")
print(t)
x = sort_przez_zliczanie(t)
print("\nZbiór po posortowaniu: ")
print(x)
