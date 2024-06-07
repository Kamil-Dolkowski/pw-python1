----------------------------------------------------------

b = add(b1, b2)

Binary add(Binary b1, binary b2) {
    Binary result;
    ...
    return result;
}

----------------------------------------------------------

Zawartość:

==b1:
idx 
sixe
*elements -> obszar w pamięci A

==b1 w add() (kopia)
idx 
sixe
*elements -> obszar w pamięci A (ten sam co dla b1 poza funkcją (co oryginał))


Problem 1:

Podczas kończenia funkcji add () uruchamia się destruktor, który oprócz usunięcia w kopii b1:
idx 
sixe
*elements
usuwa też dane, które mieszczą się w pamięci A, na którą wskazuje wskaźnik *elements,
zatem usuwa też oryginalne dane wskazujące przez wskaźnik *elements.

Problem 2:
Podobny błąd występuje w return result.

----------------------------------------------------------
----------------------------------------------------------

Rozwiązanie: Problem 1

Zawartość:

==b1:
idx 
sixe
*elements -> obszar w pamięci A

==b1 w add() (kopia)
idx 
sixe
*elements -> obszar w pamięci A' (kopia A)

----------------------------------------------------------

Rozwiązanie: Problem 2

==b:
idx 
sixe
*elements -> obszar w pamięci B


Po wykonaniu: b = add(b1, b2):

==b:
idx Newidx
sixe Newsize
*elements -> obszar w pamięci B', a B musi być zwolnione

B' - obszar pamięci wskazywany przez wskaźnik *elements zmiennej result w funkcji add()


----------------------------------------------------------
----------------------------------------------------------

p01.cpp -> rozwiązanie problemu 1,2
p02.cpp -> uporządkowanie programu i poprawa funkcji dodawania
p03.cpp -> mnożenie
p04.cpp -> zamiana liczby dwójkowej na dziesiętną, klasa Decimal, zaprzyjaźnienie
p05.cpp -> traktowanie Decimal i Binary jako rzeczy podobne, wspólna klasa Number, tablica Number numbers[] o różnych typach (Decimal, Binary)
p06.cpp -> ułamki - Fractional