SCHEMA TABLE ??? PROCEDURE


SELECT    TOP (MSSQL), DISTINCT
FROM
WHERE     T1ID = T2ID
ORDER     BY
LIMIT

Funkcje agregujące:
-MAX
-MIN
-COUNT
-SUM
-AVG

HAVING (podobne do GROUP BY)


Języki SQL:
DDL     CREATE, DROP, ALTER, TRUNCATE 
DML     INSERT, UPDATE, DELETE
TCL     COMMIT, ROLLBACK, (SAFEPOINT ?)
DQL     SELECT
DCL     GRAND, REVOTE

#---------------------------------------------------------------------------------

Relacyjna baza danych (RDBMS)

klucz -unikatowy identyfikator rekordu

W relacyjnej bazie danych każdy wiersz tabeli jest rekordem z unikatowym identyfikatorem nazywanym kluczem.
Kolumny tabeli zawierają atrybuty danych,a każdy rekord zawiera zwykle ...


UUID (unikalne)

auto increment (kolejne)


ERD (Entity-Relationship Diagram) to graficzna reprezentacja struktury danych w systemie informatycznym. 
Diagram ERD przedstawia relacje między różnymi encjami (obiektami) w bazie danych.

Cele ERD:
-ułatwiają projektowanie i organizacje danych
-analiza relacji
-wykrywanie anomalii
-komunikacja z interesariuszami (klienci, menedżerowie, programiści)
-wsparcie dla programistów

Diagramy ERD:
-encje (entities) - reprezentują konkretne obiekty lub przedmioty,np. Klient,
-relacje
-atrybuty

Encja - pewnien wyodrębniony logicznie i jednoznacznie określony byt, rozpoznawalny w badanej rzeczywistości i pełniący w niej określoną rolę.
Atrybuty - cechy (własności) charakteryzujące daną encję. którym przypisywane są określone wartości

związki

liczebność związku - ile obiektów jednej encji może być powiązanych z obiektami drugiej encji za pomocą danego związku

Podstawowe typy liczebności związku:
-1:1 jeden do jeden
-1:N jeden do wielu
-N:N wiele do wielu

atrybuty - podst elem tabeli

atrybuty proste

base_type:
https://learn.microsoft.com/en-us/sql/t-sql/statements/create-type-transact-sql?view=sql-server-ver16


atrybuty złożone
-złożone wartości
-reprez przez struktury danych, np. tablice

atrybuty klucza:
-identyfikacja rekordów
-rodzaje (klucz główny, alternatywny, obcy, unikalny)
    główny - unikatowy identif każdego rekordu
    alternat - dodatkowy unik
    obcy - atrybut, który odwołuje się do klucza głównego w innej tabeli
    unikalny - atrybut, który nie może zawierać duplikatów

atrybuty nienullowe:
-nie mogą zawierać wartości null
-dana informacja jest zawsze wymagana

atrybuty null:
-mogą zawierać wartości null
-informacja opcjonalna

atrybuty domyślne:
-określają wartość domyślną dla atrybutu, jeśli nie zostanie podana


klucze:
#główny (Primary Key)
-unikatowy identyfikator każdego rekordu
-nie może zawierać wartości null
-w tabeli może być tylko 1 klucz główny

alternatywny (Alternate Key)
-dodatkowy unikalny identif rekordu
-może zawierać wartość null
-w tabeli może być wiele kluczy alternat

Klucz obcy (Foreign Key)
-atrybut w 1 tabeli, który odwołuje się do klucza głównego w innej tabeli

Klucz unikalny :

Klucz kandydacki (Candidate Key):

klucz złożony (Composite Key):
-2 lub więcej atrybutów

Klucz sztuczny (Artificial Key):

Klucz naturalny:



CASE - komputerowe wspomaganie projektowania

Miro:
https://miro.com/pl/

^ Zarejestrować się !!!
#-------------------------

Azimutt.app
drawio



#---------------------------------
W Miro:
Entity Relationship Diagram
#--------------------------------








Projekt Biblioteka Uczelniana
-gdzie książka się znajduje
-na ile można wypożyczyć
-ile wypożyczonych książek
-czy student jest aktywny   (widok) (kto, kierunek, rok, czy aktywny)
-zapotrzebowanie na książki
-informacje o książce (nazwa, autor, index, kod isbn, opisy, tematyka, komentarze, opinia (0-10), forma(cyfrowa, papierowa))