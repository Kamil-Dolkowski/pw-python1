# Problemy optymalizacyjne.

punkt startowy i końcowy
problemy optymalizacyjne - znalezienie najlepszego (optymalnego) rozwiązania

logistyka, finanse, produkcja, informatyka

Ważność problemów optymalizacyjnych wynika z ich uniwersalności i szerokiego zakresu zastosowań.


Przykład:
Optymalizacja tras dostaw

algorytm problemu komiwojażera (TSP) lub jego warianty
algorytm szuka najkrótszej możliwej ścieżki, która odwiedza wszystkie punkty dostawy dokładnie raz i waraca do punktu wyjścia.

# Algorytmy zachłanne
algorytmy zachłanne - klasa algorytmów, które podejmują lokalnie optymalne wybory na każdym etapie z nadzieją znalezienia globalnego rozwiązania optymalnego dla całego problemu.
idąc krok po kroku wybiera najlepsze możliwe rozw w danym momencie bez uwzględniania konsekwencji w przyszłości

prostota, szybkość, najniższa złożoność


# Przykłady:
-algorytm Dijkstry - znajdowanie najkrótszej ścieżki z jednego wierzchołka do wszystkich innych wierzchołków w grafie ważonym bez wag ujemnych
-algorytm Kruskala - znajdowanie minimalnego drzewa rozpinającego dla połączonego, ważonego grafu
-algorytm Prima - znajdowanie minimalnego drzewa rozpinającego, która rozpoczyna się od pojedynczego wierzchołka ....


# Złożoność obliczeniowa algorytmu:
ilość zasobów obliczeniowych - czas, pamięć 
wyrażana jako funkcja od wielkości danych wejściowych, notacja "O" -> pozwala na oszacowanie czasu wykonania i zużycia pamięci


# Złożoność pamięciowa:
ilość pamięci wymaganej przez algorytm


# Czasowa złożoność
...

# Brak gwarancji optymalności:
algorytmy zachłanne nie zawsze prowadzą do rozw globalnie optymalnego, algorytm może "utknąć" w suboptymalnym rozw


#----------------------------algorytm Dijkstry------------------------------

Najkrótsza ścieżka - algorytm Dijkstry

                A -> E

        A*      B       C       D       E
Trasa   0       2       inf     4     inf
Dokąd   -       A               A

inf - nieskończoność


        A*      B*      C       D       E
Trasa   0       2       5       4/5     inf
Dokąd   -       A       B       A


        A*      B*      C*      D       E
Trasa   0       2       5/7     4/5     inf
Dokąd   -       A       B/D     A/A


        A*      B*      C*      D*      E
Trasa   0       2       5/7     4/5     inf
Dokąd   -       A       B/D     A/A


        A*      B*      C*      D*      E*
Trasa   0       2       5/7     4/5     7/8
Dokąd   -       A       B/D     A/A     C/D


A -> B -> C -> E   , 7


#----------------------------algorytm Kruskala--------------------------------

Algorytm Kruskala - minimalne drzewo rozpinające

O----------O
          /
         /
        /
       O
      / \
     /   \
    /     \
   O       O

   