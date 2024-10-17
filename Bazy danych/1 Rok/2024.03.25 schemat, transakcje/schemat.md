# Normalizacja i projektowanie schematu bazy danych

#--------------------------------------------------------------------------------------------

Normalizacja - proces organizowania danych w bazdie danych

jak najmniej duplikatów
poprawa integralności danych


-zmniejszenie redundancji danych - eliminowanie duplikatów danych -> oszczędność miejsca na dysku
-unikanie anomalii danych - unikanie problemów z dodawaniem, usuwaniem i aktualizowaniem danych
-poprawa integralności danych

#--------------------------------------------------------------------------------------------

Pierwsza Forma Normalna (1NF)

#--------------------------------------------------------------------------------------------

Atomowość wartości: (każdy atrybut (kolumna) w rekordzie (wierszu) powinien reprezentować najmniejszą możliwą jednostkę informacji)
-integralność danych - czystość i precyzja danych
-unikanie kompleksowych struktur - eliminacja potrzeby sortowania złożonych struktur

#--------------------------------------------------------------------------------------------

Unikalność rekordów:
-identyfikalność
-integralność referencyjna

#--------------------------------------------------------------------------------------------

Druga Forma Normalna (2NF):
-integralność danych
-redukcja redundancji

#--------------------------------------------------------------------------------------------

Trzecia Forma Normalna (3NF):
-zwiększenie spójnosci danych
-ułatwienie aktualizacji

#--------------------------------------------------------------------------------------------

Zwiększenie wydajności odczytu:
-szybki dostęp do danych
-skalowalność

#--------------------------------------------------------------------------------------------

Strategie optymalizacji:
-indeksowanie - przyspieszony odczyt kosztem nieco wolniejszych zapisów i dodatkowej pamięci dyskowej
-denormalizacja - w pewnych przypadkach świadome wprowadzenie redundancji może zmniejszyć liczbę wymaganych operacji łącznia (join), co przyspiesza odczyt
-cache'owanie - szybsze pobieranie danych

#--------------------------------------------------------------------------------------------

Świadome wprowadzenie redundancji:
-poprawa wydajności 
-uproszczenie zapytań

#--------------------------------------------------------------------------------------------

Balans między normalizacją a denormalizacją:
-optymalizacja wydajności
-skalowalność

Strategie balansowania:
-analiza wzorców dostępu
-rozważanie wymagań aplikacji

#--------------------------------------------------------------------------------------------

Rozważanie wymagań aplikacji:
-dostoswowanie do potrzeb - wyższa wydajność, lepsza skalowalność i ogólna satysfakcja użytkowników
-zapewnienie integralności danych
