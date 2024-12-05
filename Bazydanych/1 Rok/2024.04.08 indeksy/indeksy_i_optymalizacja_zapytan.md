# Indeksy i optymalizacja zapytań

#----------------------------------------------------------------------------------------------

indeksy klastrowe
indeksy -> cel: posortować, poukładać, by szybko coś znaleźć

#-----------------------------------INDEKSY KLASTROWE------------------------------------------

indeksy klastrowe lub nieklastrowe
kolejnośc wierszy na stronach danych odpowiada kolejności wierszy w indeksie
W tabeli może być tylko 1 indeks klastrowy, wiele indeksów nieklastrowych

Nie używamy (po usunięciu) jeszcze raz tego samego indeksu !!

węzeł liścia indeksu klastrowego odpowiada rzeczywistym danym, a nie wskaźnikiem do danych ?

zapisywane na dysku, rekordy są posortowane; są cashe'owane

kiedy używać:
-optymalizacja zzapytań z zakresami
-optymalizacja kluczowych operacji
-wysoka częstotliwość wstawiania (minimalizacja fragmentacji)

Plusy:
-wydajność zapytań
-optymalizacja sortowania
-zminimalizowana fragmentacja

Minusy:
-nadmierna fragmentacja
-wydajnośc wstawiania (wstawianie poza kolejnością może być wolniejsze - > reorganizacja danych na dysku)
-ograniczenie do jednego na tabelę (tylko 1 indeks klastrowy -> staranne planowanie)

Optymalnie zaprojektowany indeks klastrowy może znacząco przyspieszyć operacje na danych, ale nieprawidłowy wybór do degradacji wydajności

#----------------------------------INDEKSY NIEKLASTROWE----------------------------------------

Indeksy nieklastrowe

wiele, szybki dostęp do danych bez wpływu na kolejnośc na dysku, przechowują wskaźniki do danych
indeks nieklastrowy = klucz indeksu (1 lub więcej kolumn) + wskaźniki do danych

klucze indeksu są posortowane -> szybkie poszukiwanie
wskaźniki wskazują na miejsce przechowania danych tabeli

Kiedy używać:
-optymalizacja zapytań dla kolumn niebędących kluczem klastrowym
-tabele z istniejącym indeksem klastrowym
-zapewnienie unikalności (do wymuszenia unikalności wartości w określonych kolumnach, ...)

Różnice z ind klastrowymi:
-fizyczne przechowywanie danych
-liczba w tabeli
-wskaźniki do danych

Zastosowanie:
-wyszukiwanie
-sortowanie i grupowanie

Zalety:
-optymalizacja zapytań
-elastyczność
-minimalny wpływ na operacje wstawiania

Wady:
-dodatkowe zużycie zasobów
-koszt dostępu do danych

#-----------------------------INDEKSY PEŁNOTEKSTOWE I SEMANTYCZNE------------------------------

Indeksy pełnotekstowe:
-szybkie przeszukiwanie dużych ilości tekstu
-efektywne wyszukiwanie słów i fraz wewnątrz dużych bloków tekstowych

Implementacja:
tworzy katalog pełnotekstowy, który przechowuje indeksy
...

Przypadki uzycia:
-wyszukiwanie słów kluczowych
-analiza treści
-systemy zarządzania wiedzą


Indeksy semantyczne:
-rozszerzają ind pełnotekstowe
-analiza znaczenia (semantyki) tesktu, nie tylko jego struktury
-identyfikacja podobnych pojęć

Implementacja:
-katalog wyrazów bliskoznacznych

Przypadki użycia:
-analiza treści
-rekomendacje
-analiza sentymentu

#-----------------------------------INDEKSY PRZESTRZENNE---------------------------------------

specjalny rodzaj indeksów
efektywne przechowywanie, wyszukiwanie i zarządzanie danymi przestrzennymi (punkty, linie, poligony i inne figury geometryczne)

Jak działają:
wykorzystują struktury danych (drzewa quad, )

Zastosowanie:
-Systemy Informacji Geograficznej (GIS)
-mobilne aplikacje lokalizacyjne
-analiza przestrzenna
-zarządzanie zasobami naturalnymi
-logistyka i planowanie tras

Zalety:
-wydajność
-skalowalność
-dokładność

Google Maps

Wyzwania:
-kompleksowość
-zasoby 

#------------------------------------INDEKSY KOLUMNOWE-----------------------------------------

Indeksy kolumnowe -> indeksy wierszowe tylko w pionie

szybsze przetwarzanie zapytań dotyczących operacji na dużych zbiorach danych

Zalety:
-wydajność odczytu
-kompresja danych (zmniejsza zużycie przestrzeni dyskowej i poprawia wydajność odczytu)
-wydajność agregacji (szybsze operacje agregacji SUM, AVG, COUNT)


Kiedy stosować:
-zapytania analityczne (OLAP)
-bazy danych o dużej ilości odczytów
-przetwarzanie danych w czasie rzeczywistym
-duże zbiory danych

Rozważania:
-wydajność zapisu
-zastosowanie w środowiskach OLTP - Online Transaction Processing (duża ilość transakcji i operacji zapisu)

finanse

#------------------------------------------PORADY----------------------------------------------

Rozumienie twoich zapytań
-analiza zapytań (typy zapytań, efektywne indeksowanie)

Wybór kluczy indeksów:
-indeksuj kolumny używane w klauzulach WHERE
-indeksuj kolumny używane w JOINach
-unikaj nadmiernego indeksowania

Typy indeksów:
-wybierz odpowiedni typ indeksów

Utrzymmanie indeksów:
-regularna defragmentacja indeksów
-monitoruj wydajność i używanie indeksów

Optymalizacja indeksów:
-używaj indeksów częściowych
-kompresja indeksów

Testowanie i walidacja:
-testuj zmiany indeksów (testuj wpływ dodania lub usunięcia indeksu wna środowisku testowym przed wprowadzeniem zmian na produkcję, uniknięcie problemów wydajnościowych)

Indeksy o znormalizowane dane:
-balansuj między normalizacją a wydajnością indeksów
(bardzo znormalizowane schematy mogą wymagać większej liczby JOINów -> wpływ na wydajność)

#----------------------------------------------------------------------------------------------

Podstawy planu wykonania
mapa kroków jak zapytanie jest przetwarzane przez silnik bazodanowy
jakie operacje na danych zostaną wykonane, itp.

Optymalizacja zapytań:
plan wykonania pokazuje, jak efektywnie SQL Server ptrzetwarza zapytanie
analizując plan, można zidentyfikować potencjalne wąskie gardła i nieefektywne operacje

Koszt i statystyki:
SQL Server oszaczowuje koszty różnych operacji bazodanowych
"koszt" -> szacowana ilość zasobów potrzebnych do wykonania każdej operacji

Indeksowanie:
jak zapytanie korzysta z indeksów
pokazuje, czy zapytanie korzysta z indeksów w optymalny sposób

Wybór strategii wykonania:

Debugowanie i rozwiązywanie problemów:
problemy - np. nieoczekiwane blokady, długie operacje sortowania, nadmierne korzystanie z dysku tempdb

#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------

#-----------------

czwartek 12:00


W Windows Shell:

C:
cd Drivers
curl LINK




AdventureWorks