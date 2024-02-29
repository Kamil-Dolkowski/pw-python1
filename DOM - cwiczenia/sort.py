# Próby napisania sortowania przez scalanie.

def join_sort(arr):
    # a,b = join_sort_down(arr)
    # print("a", a,"b",b)
    # t = join_sort_up(a[0],a[1])
    # t1 = join_sort_up(b[0],b[1])
    # print("t",t,t1)

    a,b = join_sort_down(arr)
    print("a", a,"b",b)
    t = join_sort_up(a[0],a[1])
    t1 = join_sort_up(b[0],b[1])
    print("t",t,t1)

    return join_sort_up(t,t1)
    


def join_sort_down(arr: list):    # dzieli na 2
    a = []
    b = []
    print("arr",arr)
    l = int(len(arr)/2)
    for i in range(l):
       a.append(arr[i])
    for i in range(l,len(arr)):
       b.append(arr[i])
    #print("a1",a, "b1",b)

    


    if len(a) == 1 and len(b) == 1:

        if arr == [2,1]:
            print("!", a[0], b[0])

        if a[0] > b[0]:
            return [b[0],a[0]]
        return [a[0],b[0]]
    if len(a) == 1 and len(b) == 2:
        x = join_sort_down(b)
        b = []
        for i in x:
            b.append(i)
        y = join_sort_up(a,b)
        
        return y
    if len(a) != 1:
        
        return [join_sort_down(a), join_sort_down(b)]
    


def join_sort_up(a,b):  # 2 posortowane
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




t = [2,1,6,3,3,9,0,4,5,5]

x = join_sort(t)
print(x)