# Sortowanie przez scalanie.

def merge_sort(arr):    
    a = []
    b = []

    l = int(len(arr)/2)
    for i in range(l):
       a.append(arr[i])
    for i in range(l,len(arr)):
       b.append(arr[i])
   
    if len(a) == 1 and len(b) == 1:
        if a[0] > b[0]:
            return [b[0],a[0]]
        return [a[0],b[0]]
    
    if len(a) == 1 and len(b) == 2:
        x = merge_sort(b)
        b = []
        for i in x:
            b.append(i)
        y = merge_sort_add(a,b)
        return y
    
    if len(a) != 1:
        x,y = merge_sort(a), merge_sort(b)
        return merge_sort_add(x,y)
    


def merge_sort_add(a,b):  
    t = []
    end = len(a) + len(b) - 1
    for i in range(end):
        if len(a) == 0:
            x = b.pop(0)
        elif len(b) == 0:
            x = a.pop(0)
        elif a[0] < b[0]:
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




t = [2,1,6,3,3,9,0]

x = merge_sort(t)
print(x)