DML - modyfikacja danych
DDL - definiowanie 
DCL - 
TCL - 


DDL (Data Definition Language)

#------------------------------------CREATE----------------------------------

CREATE - tworzenie nowych obiektów w bazie danych, np. tabele, widoki, indeksy, funkcje, triggery, schematy

#------------------------------------ALTER---------------------------------------

ALTER - modyfikowanie kolumn

ALTER TEBLE nazwa_tabeli ADD COLUMN nazwa_kolumny typ_danych  -  dodaje nową kolumnę
ALTER TABLE nazwa_tabeli DROP COLUMN nazwa_kolumy  - usuwa kolumnę

!! kolumny TYLKO dodają się na końcu

#-----------------------------------DROP--------------------------------------

DROP - usuwa obiekty (nieodwracalne)

DROP TABLE nazwa_tabeli  - usuwa tabelę z bazy danych
DROP DATABASE nazwa_bazy_danych  - usuwa bazę danych

#---------------------------------TRUNCATE-----------------------------------

TRUNCATE - usuwa wszystkie wiersze z tabeli bez usuwania tabeli

TRUNCATE TABLE nazwa_tabeli



TRUNCATE - polecenie DDL (minimalizuje ilość logowania transakcji) (nie aktywuje wyzwalaczy) (nie korzysta z kluczy)

DELETE - polecenie DML (obsługuje ROLLBACK) (czasochłonne, rejestruje każde usunięcie wiersza) (może aktywować wyzwalacze)

#----------------------------------COMMENT------------------------------------

COMMENT - dodawanie komentarzy

#----------------------------------RENAME--------------------------------------

RENAME - zmiana nazwy obiektu

EXEC sp_rename 'stara nazwa','nowa nazwa'  - zmiana nazwy tabeli

#------------------------------RODZAJE TABEL-----------------------------------

Tabele regularne (standardowe) - normalne tabele
Tabele tymczasowe - przechowywanie sesje, ruchy, transakcje, tymczasowo przechowywane dane
Tabele systemowe - metadane o tabelach, kolumnach, typach danych, relacjach
Tabele partycjonowane - podział tabeli na mniejsze, łatwiejsze do zarządzania fragmenty (partycje)
Tabele z widokami indeksowanymi - przechowują wyniki zapytań w strukturze, szybszy dostęp do widoków
Tabele historyczne - automatyczne śledzenie pełnej historii zmian
Tabele pamięci - przechowywanie danych z pamięci RAM, użyteczne w przetwarzaniu transakcji online (OLTP)

#------------------------------------------------------------------------------

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50),
    Email VARCHAR(100)
);

#------------------------------------------------------------------------------

CREATE TABLE MemoryOptimizedTable (
    ID INT PRIMA....
    ...
)

#---------------------------------IN MEMORY-----------------------------------

In memory:
-wysoka wydajność i niskie opóźnienia
-duże obciążenie zapytaniami
-dostęp do danych operacyjnych
-raportowanie i analiza ?

#------------------------------------------------------------------------------

CREATE PARTITION FUNCTION
YearPartitionFunction(INT)

AS RANGE LEFT FOR VALUES (2019,2020);





CREATE PARTITION SCHEME
YearPartitionScheme

AS PARTITION
...





CREATE TABLE PartitionedTable (
    ID INT,
    Year INT,
    --inne kolumny
)

ON YearPartitionScheme(Year)

#-------------------------------WIDOKI-------------------------------------

widoki - wirtualne tabele reprezentujące wyniki zapytań SQL
nie przechowują fizycznie danych


Standardowe widoki - podstawowe widoki, ukrycie złożoności baz danych
Widoki indeksowane (zmaterializowane) - fizyczne dane, szybsze
Widoki schematu - widoki związane ze schematem; nie można modyfikować obiektów, na których widok jest zależny, bez uprzedniego usunięcia tego związku (blocker)
Widoki partycjonowane - widoki, które łączą dane z różnych tabel, traktując je jako jedną całość
Widoki rekursywne - odwołują się do samych siebie

#--------------------------TWORZENIE TABELI-------------------------------

CREATE TEBLE nazwa_tabeli (
    kolumna1 typ_danych [ograniczenie]
    kolumna2 typ_danych [ograniczenie]
    kolumna3 typ_danych [ograniczenie]
    ...
);


[ograniczenie] - np. PRIMARY KEY, NOT NULL, UNIQUE, FOREIGN KEY

#------------------------------------------------------------------------------

CREATE TABLE Pracownicy (
    PracownikID INT PRIMARY KEY,
    Imie VARCHAR(50) NOT NULL,
    Nazwisko VARCHAR(50) NOT NULL,
    ...
    DataZatrudnienia DATETIME NOT NULL,
    ...
)

#------------------------------------------------------------------------------

Typy danych:
1.Numeryczne:
 -INT
 -DECIMAL, NUMERIC
 -FLOAT, REAL
2.Tekstowe:
 -CHAR - stała długość
 -VARCHAR - zmienna długość
 -TEXT
3.Data/Czas:
 -DATE
 -TIME
 -DATETMIE, TIMESTAMP
4.Logiczne:
 -BOOLEAN
#------------------------------------------------------------------------------

CREATE TYPE NazwaTypu FROM BazowyTypDancyh(Ograniczenia);



CREATE TYPE Telefon AS VARCHAR(15);

CREATE TABLE Pracownicy (
    Imie VARCHAR(50),
    Telefon Telefon
);

#------------------------------------------------------------------------------

CREATE VIEW nazwa_widoku AS
SELECT kolumna1, kolumna2, ...
FROM tabela
WHERE warunek;




CREATE VIEW Menedzerowie AS
SELECT Imie, Nazwisko
FROM Pracownicy
WHERE Stanowisko = 'Menedżer';


SELECT * FROM Menedzerowie;

#------------------------------------------------------------------------------

ALTER VIEW
DROP VIEW nazwa_widoku;

widoki są tylko do odczytu

#------------------------------------------------------------------------------

Klucze Obce:

CREATE TABLE Dzialy (
    DzialID INT PRIMARY KEY,
    Nazwa VARCHAR(100)
);

CREATE TABLE Pracownicy (
    PracownikID INT PRIMARY KEY,
    Imie VARCHAR(50),
    DzialID INT,
    FOREIGN KEY (DzialID) REFERENCES Dzialy(DzialID)
);

#------------------------------------------------------------------------------
Indeksy:

CREATE INDEX idx_DzialID ON Pracownicy(DzialID)

#------------------------------------------------------------------------------

Klucze obce:
-relacje między tabelami są zawsze spójne

indeksy - optymalizacja wydajno ści zapytań

#------------------------------------------------------------------------------