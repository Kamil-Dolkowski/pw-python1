# Transakcje i kontrola współbieżności

#--------------------------------------------------------------------------------------------

Transakcje i kontrola współbieżności zapewniają integralność i spójność danych

#--------------------------------------------------------------------------------------------

Transakcja - sekwencja operacji na danych, która jest traktowana jako jednostka

operacja wykonywane w sposób bezpieczny i spójny, nawet w  przypadku awarii systemu, czy błędów aplikacji
zarządzanie zmianami w bazie danych w sposób kontrolowany
Przykład: Przelew środków między kontami bankowymi, gdzie aktualizacja salda jednego konta i drugiego musi zostać ??

#--------------------------------------------------------------------------------------------

Właściwości transakcji: ACID
-Atomicity (Atomowość) - transakcja jest jednostką niepodzielną
-Consistency (Spójność)
-Isolation (Izolacja)
-Durability (Trwałość)

#--------------------------------------------------------------------------------------------

blokady i mechanizmy izolacji
-blokady - kontrolowanie dostępu do zasobów bazy
-poziomy izolacji - w jakim stopniu transakcja jest izolowana od działania innych transakcji

#--------------------------------------------------------------------------------------------

ACID oraz mechanizmy izloacji i blokad -> efektywne zarządzanie równoczesnym dostępem wielu użytkowników współdzielonych danych

#--------------------------------------------------------------------------------------------

Best practise:
-rozpoczynaj transakcje, tylko wtedy, gdy operacja wymaga wykonania kilku kroków jako jednostka
-Zamykaj transakcje (COMMIT) jak najszybciej, aby uniknąć długotrwałego blokowania zasobów

#--------------------------------------------------------------------------------------------

Poziomy izolacji transakcji:
-READ UNCOMMITTED - najniższy poziom izolacji; czytanie niezatwierdzonych danych (tzw. "brudne czytanie")
-READ COMMITTED - domyślny poziom izolacji; zapobiega czytaniu "brudnych danych"; blokuje czytanie danych, które są modyfikowane (mniejsze ryzyko brudnych danych, ale problem "non-repeatable reads")
-REPEATABLE READ
-SERIALIZABLE - izolacja tranzacji przez blokowanie zakresów danych

#------------------------------------READ UNCOMMITTED----------------------------------------

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
BEGIN TRANSACTION;
SELECT * FROM Tabela WHERE Kolumna = 'Wartość';
COMMIT;

#-------------------------------------READ COMMITTED-----------------------------------------

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
SELECT * FROM Tabela WHERE Kolumna = 'Wartość';
COMMIT;

#-------------------------------------REPEATABLE READ---------------------------------------

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRANSACTION;
SELECT * FROM Tabela WHERE Kolumna = 'Wartość';
-- Wykonaj inne operacje, wynik zapytania powyżej się nie zmieni
COMMIT;

#--------------------------------------SERIALIZABLE-----------------------------------------

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
SELECT * FROM Tabela WHERE Kolumna BETWEEN 'Wartość1' AND 'Wartość2';
-- Transakcja zapewnia, że żadne inne transakcje nie mogą dodać, usunąć lub zmienić
COMMIT;

#--------------------------------------------------------------------------------------------

Minimalizuj zakres blokad

#--------------------------------------------------------------------------------------------

Jak projektować zapytania?:
-ogranicz zakres zapytań
-unikaj długotrwałych transakcji
-wykorzystaj odpowiedni poziom izolacji
-optymalizuj zapytania

#--------------------------------------------------------------------------------------------

Unikaj deadlocków przez konsekwentne blokowanie
Zasada "Zawsze aplikuj blokady w tej samej kolejności ..."

#--------------------------------------------------------------------------------------------

Wykorzystuj mechanizmy zarządznia współbieżnością optymistyczną
OOC

#--------------------------------------------------------------------------------------------

-wersjonowanie danych - każy wiersz posiada wersję lub znacznik czasu
-przetwarzanie transakcji
-sprawdzanie przy zatwierdzaniu

#--------------------------------------------------------------------------------------------

Zalety i wyzwania:
-wysoka wydajność w środowiskach o niskim poziomie konfliktów
-zwiększona współbieżność

Wyzwania:
-potencjalnie wyższa ilość wycofań
-zarządzanie wersjami

#--------------------------------------------------------------------------------------------

BEGIN TRANSACTION;

-- sprawdzanie, czy ksiazka jest dostepna
DECLARE @Dostepna bit;
SELECT @Dostepna = CASE WHEN Status = 'Dostepna' THEN 1 Else 0 END
FROM Ksiazki
WHERE KsiazkaID = 123;

IF @Dostepna = 1
BEGIN
    -- aktualizacja stanu ksiazki
    UPDATE Ksiazki
    SET Status = 'Wypozyczona'
    WHERE KsiazkaID = 123;

    -- dodanie rekordu wypozyczenia
    INSERT INTO Wypozyczenia (KsiazkaID, UzytkownikID, DataWypozycvzenia,DataZwrotu)
    VALUES (123, 456, GETDATE(), DATEADD(day, 30, GETDATE()))

    COMMIT;
END
ELSE
BEGIN
    -- wycofanie transakcji, jeżli ksiazka nie jest dostepna
    ROLLBACK;
END;

#--------------------------------------------------------------------------------------------








SET IMPLICIT_TRANSACTIONS ON;

#-----------------------------------Poprawa BibliotekiPW-------------------------------------

Poprawa BibliotekiPW

status do oddzielnej tabeli
komentarze
widoki - łączenie tabel



CREATE TABLE review (
    review_ID int PRIMARY KEY IDENTITY(1,1),
    rating int NOT NULL CHECK (rating BETWEEN 1 AND 5),     <- check
    content varchar(300),
    username varchar(30) NOT NULL,
    hide bit,
);



CREATE TABLE localization (
    localization_ID int PRIMARY KEY IDENTITY(1,1),
    city varchar(30) NOT NULL,
    street varchar(30) NOT NULL,
    number int NOT NULL,                <- czego dotyczy ( nr domu, czy ulicy ? )
    post_code post_code NOT NULL,
    voivodeship varchar(19) NOT NULL,
);


CREATE TABLE account (
    account_ID int PRIMARY KEY IDENTITY(1,1),
    name varchar(15) NOT NULL,
    surname varchar(30) NOT NULL,
    status varchar(10) NOT NULL,
    login varchar(20) NOT NULL,
    password varchar(256) NOT NULL,      <- 20 na 256
    type varchar(20) NOT NULL,
    index_PW varchar(6),
    rentals int,
    phone_number phone_number NOT NULL,
    email varchar(256) NOT NULL,         <- 40 na 256, nadać nowy typ
);




md5, SHA-1, SHA-256, base64