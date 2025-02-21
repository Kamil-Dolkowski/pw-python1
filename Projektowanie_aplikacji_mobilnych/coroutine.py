# Korutyny (coroutine)

def myFunct():
    yield "ala"
    yield "ma"
    yield "kota"
    
for x in myFunct():
    print(x)