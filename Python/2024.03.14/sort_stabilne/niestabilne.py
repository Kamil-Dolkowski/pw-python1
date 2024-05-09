# Sortowanie stabilne i niestabilne

# Różnica między stabilnym a niestabilnym sortowaniem leży w tym, jak te algorytmy traktują równoważne elementy w trakcie procesu sortowania.

#---------------------------------SORTOWANIE STABILNE------------------------------------------

# Sortowanie stabilne - otrzymujemy zawsze te same sekwencje na wyjściu

# Przykłady:
# -sortowanie przez scalanie (mergesort)
# -sortowanie przez wstawnianie (insertion sort)
# -sortowanie bąbelkowe (bubble sort)

#--------------------------------SORTOWANIE NIESTABILNE----------------------------------------

# Sortowanie niestabilne - nie gwarantuje zachowania wzajemnej kolejności równych elementów wejściowych w posortowanej sekwencji

# Przykłady:
# -sortowanie szybkie (quicksort)
# -sortowanie przez wybór (selection sort)
# -heap sort (sortowanie przez kopcowanie)

# stabilne sortowanie - tam gdzie kolejność ma znaczenie

#----------------------------------------------------------------------------------------------

dane = [{'id': 1, 'value': 5},
        {'id': 2, 'value': 3},
        {'id': 3, 'value': 5},
        {'id': 4, 'value': 8},
        {'id': 5, 'value': 3}]

#---------------SORTOWANIE NIESTABILNE------------------

# zastosować sortowanie niestabilne - (quicksort)


#---------------------------------
# def quicksort_dicts(arr, key):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivot = arr[-1]
#         mniejsze, rowne, wieksze = [], [pivot], []

#         for x in arr[:-1]:
#             if x[key] < pivot[key]:
#                 mniejsze.append(x)
#             elif x[key] > pivot[key]:
#                 wieksze.append(x)
#             else:
#                 rowne.append(x)

#         return quicksort_dicts(mniejsze, key) + rowne + quicksort_dicts(wieksze, key)



# posortowane = quicksort_dicts(dane, 'value')
# for item in posortowane:
#     print(f"ID: {item['id']}, Value: {item['value']}")
#---------------------------------


def quicksort_dicts(arr, key='value'):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x[key] <= pivot[key]]
    greater = [x for x in arr[1:] if x[key] > pivot[key]]
    return quicksort_dicts(lesser, key) + [pivot] + quicksort_dicts(greater, key)

# Sortowanie tablicy słowników
posortowane_dane = quicksort_dicts(dane)

# Wydrukowanie posortowanej tablicy
print("Posortowana lista według 'value': ")
for item in posortowane_dane:
    print(item)





#---------------SORTOWANIE STABILNE------------------

# zastosować sortowanie stabilne - (mergesort - przez scalanie)

# def merge_sort_dict(arr, key):    
#     a = []
#     b = []

#     l = int(len(arr)/2)
#     for i in range(l):
#        a.append(arr[i])
#     for i in range(l,len(arr)):
#        b.append(arr[i])
   
#     if len(a) == 1 and len(b) == 1:
#         if a[0] > b[0]:
#             return [b[0],a[0]]
#         return [a[0],b[0]]
    
#     if len(a) == 1 and len(b) == 2:
#         x = merge_sort(b)
#         b = []
#         for i in x:
#             b.append(i)
#         y = merge_sort_add(a,b)
#         return y
    
#     if len(a) != 1:
#         x,y = merge_sort(a), merge_sort(b)
#         return merge_sort_add(x,y)

# def merge_sort_add(a,b):  
#     t = []
#     end = len(a) + len(b) - 1
#     for i in range(end):
#         if len(a) == 0:
#             x = b.pop(0)
#         elif len(b) == 0:
#             x = a.pop(0)
#         elif a[0] < b[0]:
#             x = a.pop(0)
#         else:
#             x = b.pop(0)
#         t.append(x)

#     if len(a) == 1:
#         x = a.pop(0)
#     else:
#         x = b.pop(0)
#     t.append(x)
    
#     return t




# t = [2,1,6,3,3,9,0]

# x = merge_sort_dict(dane, 'Value')
# print(x)
    


#-----------------------------------QUIZ--------------------------------------
# projekt na zajęciach


# QUIZ
# -kto
# -które dobrze, które źle
# -czy był progres, czy nie (w kolejnych podejściach)
# -pytania, odpowiedzi, poprawne odpowiedzi
# -pula pytań i wybór kilku z nich
# -pytania i tematy w Bazie danych


# projekt w Miro -> python + baza danych
    





#---------------------------------- ! ! ! -------------------------------------
# Sortowanie przez zliczanie
# zrobić w domu !! 