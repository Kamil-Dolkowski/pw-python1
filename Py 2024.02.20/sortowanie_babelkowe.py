# Sortowanie bąbelkowe

# -wejscie: tablica (array)
# -wyjscie: tablica (array)


def bubble_sort(array):
    n = len(array)
    for j in range(n-1):
        for i in range(n-j-1):
            if array[i] > array[i+1]:
                # x = array[i]
                # array[i] = array[i+1]
                # array[i+1] = x
                array[i], array[i+1] = array[i+1], array[i]
    return array



t = [3,4,1,2,2,5,7,3,4,5,3,1,2,0,9]
print(t)

x = bubble_sort(t)
print(x)
