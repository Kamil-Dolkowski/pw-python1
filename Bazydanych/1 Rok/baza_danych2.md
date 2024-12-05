DML - Data Manipulation Language

SELECT - pobieranie danych z tabeli/widoku
INSERT - dodawanie nowych wierszy
UPDATE - aktualizuje istniejace wiersze
DELETE - usuwa wiersze z tabeli

#-----------------------------------SELECT--------------------------------------

SELECT - pobiera dane z tabeli lub widoku

SELECT kolumna1, kolumna2
FROM tabela;

#-----------------------------------INSERT-------------------------------------

INSERT - dodaje nowe wiersze do tabeli

INSERT INTO tabela (kolumna1, kolumna2)
VALUES (wartosc1, wartosc2);

#----------------------------------UPDATE---------------------------------------

UPDATE - aktualizuje istniejace wiersze w tabeli

UPDATE tabela
SET kolumna = nowa_wartosc
WHERE warunek;

#----------------------------------DELETE---------------------------------------

DELETE - usuwa wiersze z tabeli

DELETE FROM tabela
WHERE warunek;

#----------------------------------MERGE---------------------------------------

MERGE - łączy dane z tabeli źródłowej do tabeli docelowej na podstawie określonego warunku

MERGE INTO tabela_docelowa AS target
USING tabela_zrodlowa AS source
ON target.kolumna = source.kolumna
WHEN MATCHED THEN
    UPDATE SET target.kolumna = source.kolumna
WHEN NOT MATCHED THEN
    INSERT (kolumna) VALUES (source.kolumna);

#-------------------------------BULK INSERT------------------------------------

BULK INSERT - wstawia dane z pliku do tabeli

BULK INSERT tabela
FROM 'sciezka/do/pliku'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n'
);

#--------------------------------SELECT INTO----------------------------------

SELECT INTO - tworzy nową tabelę na podstawie wyniku zapytania SELECT

SELECT kolumna1, kolumna2
INTO nowa_tabela
FROM stara_tabela;

#-------------------------------TRUNCATE TABLE-------------------------------

TRUNCATE TABLE - usuwa wszystkie wiersze z tabeli

TRUNCATE TABLE tabela;

#---------------------------------REPLACE---------------------------------------

REPLACE - wstawia nowe wiersze lub ... ?

REPLACE INTO tabela (kolumna1, kolumna2)
VALUES (wartosc1, wartosc2);

#----------------------------------WRITETEXT------------------------------------

WRITETEXT - ?

WRITETEXT tabela.kolumna 'tekst do wstawienia';

#------------------------------------JOIN---------------------------------------

JOIN - łączenie tabel


#---------------INNER JOIN--------------

INNER JOIN - zwraca wiersze, które mają pasujące rekordy w obu tabelach

SELECT kolumna1, kolumna2
FROM tabela1
INNER JOIN tabela2 ON tabela1.klucz = tabela2.klucz;


#---------------LEFT JOIN--------------

LEFT JOIN - zwraca wszystkie wiersze z lewej tabeli i pasujące wiersze z prawej. Jeśli w prawej nie ma pasujących wierszy, to zostaną zwrócone wartości NULL

SELECT *
FROM tabelaA
LEFT JOIN tabelaB ON tabelaA.kolumna = tabelaB.kolumna;

#---LEFT JOIN EXCLUDING INNER JOIN----

SELECT *
FROM tabelaA
LEFT JOIN tabelaB ON tabelaA.kolumna = tabelaB.kolumna
WHERE tabelaB.kolumna IS NULL;


#-------------RIGHT JOIN--------------

SELECT *
FROM tabelaA
RIGHT JOIN tabelaB ON tabelaA.kolumna = tabelaB.kolumna;

#---RIGHT JOIN EXCLUDING INNER JOIN----

wszystkie rekordy, które nie są w tabeliA

SELECT *
FROM tabelaA
RIGHT JOIN tabelaB ON tabelaA.kolumna = tabelaB.kolumna
WHERE tabelaB.kolumna IS NULL;


#-------------FULL JOIN--------------

zwraca wszystkie wiersze z obu tabel, łącząc pasujące rekordy i wypełniając brakujące wartości NULL

SELECT *
FROM tabelaA
FULL JOIN tabelaB ON tabelaA.kolumna = tabelaB.kolumna;


#---FULL JOIN EXCLUDING INNER JOIN---

A + B, ale bez części wspólnej

SELECT *
FROM tabelaA
INNER JOIN tabelaB ON tabelaA.kolumna = tabelaB.kolumna;
WHERE NOT EXISTS (SELECT 1 FROM tabelaC WHERE tabelaC.kolumna = tabelaA.kolumna);

#--------------------------------------AGREGACJA DANYCH-----------------------------------------

#-------------GROUP BY-------------

grupowanie wierszy wg określonych kolumn i stosowanie agregatów do tych grup

-grupowanie danych  dzieli na unikatowe wartosci
-obliczanie agregatów (SUM, AVG, COUNT, MAX, MIN)
-wybieranie kolumn
-obliczanie statystyk


SELECT SUM(cena) AS suma_cen
FROM produkty;

SUM
AVG
COUNT        ( COUNT(1) lepiej niż COUNT(*) )
MIN
MAX

#-------------HAVING------------

SELECT kolumna1, SUM(kolumna2)
FROM tabela
GROUP BY kolumna1
HAVING SUM(kolumna2) > 1000

#-------------------------------PODZAPYTANIA I OPERACJE NA ZBIORACH-------------------------------

SELECT * FROM tabela WHERE kolumna = (SELECT MAX(kolumna) FROM inna_tabela);

SELECT * FROM (SELECT kolumna1, kolumna2 FROM tabela) AS temp WHERE kolumna1 > 100;

SELECT *, (SELECT MAX(kolumna) FROM inna_tabela) AS max_wartosc FROM tabela;

#-------------------------------------OPERACJE NA ZBIORACH-----------------------------------------

#--------------UNION--------------

UNION - łączy wyniki dwóch lub więcej zapytań, usuwając duplikaty
[liczba i typ kolumn muszą się zgadzać!]

SELECT kolumna FROM tabela1
UNION
SELECT kolumna FROM tabela2;

#-------------UNION ALL------------

UNION ALL - łączy wyniki dwóch lub więcej zapytań, zachowując duplikaty

SELECT kolumna FROM tabela1
UNION ALL
SELECT kolumna FROM tabela2;

#-----------INTERSECT------------

INTERSECT - ?

SELECT kolumna FROM tabela1
INTERSECT
SELECT kolumna FROM tabela2;

#------------EXCEPT-------------

EXCEPT - zwraca wiersze z pierwszego zapytania, które nie są obecne w drugim

SELECT kolumna FROM tabela1
EXCEPT
SELECT kolumna FROM tabela2;

#------------EXISTS-------------

SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);



#-------------------------------FUNKCJE STRINGOWE------------------------------------

#---------------LEN----------------

SELECT LEN(nazwa) AS dlugosc

#--------------LEFT----------------


#--------------RIGHT---------------


#---------------UPPER--------------


#---------------LOWER--------------


#-------------------------------FUNKCJE DATY I CZASU-----------------------------------

#------------GETDATE-------------

GETDATE - zwraca bieżącą datę i czas

SELECT GETDATE() AS aktualna_data_i_czas;

#-----------TIMESTAMP-------------

wartość intiger, unikalna, do wielu znaków po przecinku

#-------------DATEADD-------------

DATEADD - dodaje określoną wartość do daty

SELECT DATEADD(day, 7, data_zamowienia) AS data_dostawy
FROM zamowienia;

#------------DATEDIFF-------------

SELECT DATEDIFF(year, data_urodzenia, GETDATE()) AS wiek
FROM pracownicy;

#---------YEAR/MONTH/DAY---------

SELECT YEAR(data_zatrudnienia) AS rok_zatrudnienia
FROM pracownicy;

#-------MONTHNAME/DATENAME-------

MONTHNAME/DATENAME - pobiera nawzę miesiąca/dnia tygodnia z daty

SELECT DATENAME(month, data_zatrudnienia) AS nazwa_miesiaca
FROM pracownicy;

#-------------------------------FUNKCJE LOGICZNE-------------------------------

#--------------CASE--------------

SELECT nazwa,
    CASE WHEN cena > 100 THEN 'Drogi'
        ELSE 'Tani'
    END AS kategoria_ceny
FROM produkty;

#----------COALESCE-------------

zwraca pierwszą niepustą wartość z listy argumentów

SELECT nazwa,
    COALESCE(opis, 'Brak opisu') AS opis_produktu
FROM produkty;

#----------------------------------INNE FUNKCJE----------------------------------

#------------CAST/CONVERT------------

CAST/CONVERT - konwertuje wartość na określony typ danych

SELECT CAST('123' AS INT) AS liczba;
SELECT CONVERT(VARCHAR, data_zatrudnienia, 101) AS data_w_formacie_mm_dd_rrrr
FROM pracownicy;

#-----ROW_NUMBER/RANK/DENSE_RANK-----

ROW_NUMBER/RANK/DENSE_RANK - przypisuje numer porządkowy do wierszy wynikowych

SELECT nazwa,
    cena,
    ROW_NUMBER() OVER(ORDER BY cena DESC) AS ranking_cen
FROM produkty;

#--------------------------------



#--------------------------------



#--------------------------------



#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------

#----------------------------------