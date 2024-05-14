
--Zad.1
--Partycjonowanie poziome

--Cel: Partycjonowanie poziome polega na podziale tabeli na mniejsze podzbiory w oparciu o wartości pewnej kolumny
--Treść zadania:
--  Utwórz schemat partycjonowania dla tabeli Sales.SalesOrderHeader według kolumny OrderDate.
--  Stwórz odpowiednią funkcję partycjonowania.
--  Utwórz nową tabelę partycjonowaną, która będzie przechowywać dane z tabeli Sales.SalesOrderHeader.
--  Przenieś dane z oryginalnej tabeli do nowej tabeli partycjonowanej.

use AdventureWorks2019;
GO

CREATE PARTITION FUNCTION SalesOrderDatePF (datetime)
AS RANGE RIGHT FOR VALUES ('2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01');

--Krok 2: Utworzenie funkcji partycjonowania.
CREATE PARTITION SCHEME SalesOrderDatePS
AS PARTITION SalesOrderDatePF
TO ([PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY]);

--Krok 3: Utworzenie nowej tabeli partycjonowanej.
CREATE TABLE Sales.SalesOrderHeader_Partitioned
(
	SalesOrderID int NOT NULL,
	OrderDate datetime NOT NULL,
	-- (Pozostałe kolumny)
	CONSTRAINT PK_SalesOrderHeader_Partitioned PRIMARY KEY CLUSTERED (SalesOrderID, OrderDate)
) ON SalesOrderDatePS(OrderDate);

--Krok 4: Przeniesienie danych do nowej tabeli partycjonowanej
INSERT INTO Sales.SalesOrderHeader_Partitioned
(SalesOrderID, OrderDate/*,  pozostałe kolumny */)
SELECT SalesOrderID, OrderDate/*,  pozostałe kolumny */
FROM Sales.SalesOrderHeader;




SELECT * FROM Sales.SalesOrderHeader_Partitioned








--Zad.1'

use AdventureWorks2019;

ALTER DATABASE AdventureWorks2019
ADD FILEGROUP ROK2010
GO

CREATE PARTITION FUNCTION SalesOrderDatePF (datetime)
AS RANGE RIGHT FOR VALUES ('2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01');

--Krok 2: Utworzenie funkcji partycjonowania.
CREATE PARTITION SCHEME SalesOrderDatePS
AS PARTITION SalesOrderDatePF
TO ([ROK2010], [PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY]);

--Krok 3: Utworzenie nowej tabeli partycjonowanej.
CREATE TABLE Sales.SalesOrderHeader_Partitioned
(
	SalesOrderID int NOT NULL,
	OrderDate datetime NOT NULL,
	-- (Pozostałe kolumny)
	CONSTRAINT PK_SalesOrderHeader_Partitioned PRIMARY KEY CLUSTERED (SalesOrderID, OrderDate)
) ON SalesOrderDatePS(OrderDate);

--Krok 4: Przeniesienie danych do nowej tabeli partycjonowanej
INSERT INTO Sales.SalesOrderHeader_Partitioned
(SalesOrderID, OrderDate/*,  pozostałe kolumny */)
SELECT SalesOrderID, OrderDate/*,  pozostałe kolumny */
FROM Sales.SalesOrderHeader;




SELECT * FROM Sales.SalesOrderHeader_Partitioned







--Zad.2
--Partycjonowanie pionowe

--Cel: Partycjonowanie pionowe polega na podziale tabeli na mniejsze tabele w oparciu o grupy kolumn. W tym zadaniu podzielisz tabelę Person.Person na 2 tabele w oparciu o grupy kolumn.
--Treść zadania:
--  Utwórz 2 nowe tabele, Person.Person_Part1 i Person.Person_Part2, aby przechowywać różne grupy kolumn z tabeli Person.Person.
--  Przenieś odpowiednie dane z oryginalnej tabeli do nowych tabel partycjonowanych pionowo.
--  Utwórz widok Person.Person łączący oboe partycjonowane pionowo tabele.



--Krok 1: Utworzenie nowych tabel partycjonowanych pionowo.
use AdventureWorks2019;

CREATE TABLE Person.Person_Part1
(
	BusinessEntityID int NOT NULL,
	FirstName nvarchar(50) NOT NULL,
	LastName nvarchar(50) NOT NULL,
	-- inne kolumny związane z tożsamością
	CONSTRAINT PK_Person_Part1 PRIMARY KEY (BusinessEntityID)
);

CREATE TABLE Person.Person_Part2
(
	BusinessEntityID int NOT NULL,
	EmailAddress nvarchar(50) NOT NULL,
	PhoneNumber nvarchar(25) NOT NULL,
	-- inne kolumny kontaktowe
	CONSTRAINT PK_Person_Part2 PRIMARY KEY (BusinessEntityID),
	CONSTRAINT FK_Person_Part2 FOREIGN KEY (BusinessEntityID) REFERENCES Person.Person_Part1 (BusinessEntityID)
);

--Krok 2: Przeniesienie danych do nowych tabel partycjonowanych pionowo.
INSERT INTO Person.Person_Part1 (BusinessEntityID, FirstName, LastName /* inne kolumny */)
SELECT BusinessEntityID, FirstName, LastName /* inne kolumny */
FROM Person.Person;


INSERT INTO Person.Person_Part2 (BusinessEntityID, EmailAddress, PhoneNumber /* inne kolumny */)
SELECT BusinessEntityID, EmailAddress, PhoneNumber /* inne kolumny */
FROM Person.Person;

--Krok 3: Utworzenie widoku łączącego partycjonowane pionowo tabele.
CREATE VIEW Person.Person AS
SELECT
	p1.BusinessEntityID,
	p1.FirstName,
	p1.LastName,
	p2.EmailAddress,
	p2.PhoneNumber
	-- pozostałe kolumny
FROM Person.Person_Part1 p1
LEFT JOIN Person.Person_Part2 p2 ON p1.BusinessEntityID = p2.BusinessEntityID;




