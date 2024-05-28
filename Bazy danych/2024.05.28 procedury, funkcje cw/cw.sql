--Zad.1
--Procedura do wyciągania informacji o sprzedaży produktu.

--Napisz procedurę, która przyjmuje identyfikator produktu jako parametr wejściowy i zwraca szczegółowe informacje o sprzedaży tego produktu, 
--takie jak liczba sprzedanych sztuk, całkowita wartość sprzedaży, średnia cena sprzedaży oraz data pierwszej i ostatniej sprzedaży.

USE AdventureWorks2019;
GO

CREATE PROCEDURE InformacjeOSprzedazy
	@ProductID INT
AS
BEGIN
	SELECT 
	SUM(sod.OrderQty) AS LiczbaSprzedanychSztuk, 
	SUM(sod.LineTotal) AS CalkowitaWartoscSprzedazy, 
	SUM(sod.LineTotal)/SUM(sod.OrderQty) AS SredniaCenaSprzedazy, 
	MIN(soh.DueDate) AS DataPierwszejSprzedazy, 
	MAX(soh.DueDate) AS DataOstatniejSprzedazy 
	FROM Sales.SalesOrderDetail sod
	JOIN Sales.SalesOrderHeader soh ON soh.SalesOrderID = sod.SalesOrderID
	WHERE sod.ProductID = @ProductID;
END;




-----wywołanie------

EXEC InformacjeOSprzedazy 870;



SELECT * FROM Sales.SalesOrderDetail
SELECT * FROM Sales.SalesOrderHeader
SELECT * FROM Production.Product



-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- Zad.1'  + nazwa produktu

USE AdventureWorks2019;
GO

CREATE PROCEDURE InformacjeOSprzedazy1
	@ProductID INT
AS
BEGIN
	SELECT 
    p.Name AS NazwaProduktu,
	SUM(sod.OrderQty) AS LiczbaSprzedanychSztuk, 
	SUM(sod.LineTotal) AS CalkowitaWartoscSprzedazy, 
	SUM(sod.LineTotal)/SUM(sod.OrderQty) AS SredniaCenaSprzedazy, 
	MIN(soh.DueDate) AS DataPierwszejSprzedazy, 
	MAX(soh.DueDate) AS DataOstatniejSprzedazy 
	FROM Sales.SalesOrderDetail sod
	JOIN Sales.SalesOrderHeader soh ON soh.SalesOrderID = sod.SalesOrderID
    JOIN Production.Product p ON sod.ProductID = p.ProductID
	WHERE sod.ProductID = @ProductID
    GROUP BY p.Name;
END;


----------------------------------------------------------------------------------------------------------------------------------------------------

--Zad.2
--Funkcja do obliczania wieku pracownika.

--Napisz funkcję, która przyjmuje identyfikator pracownika i zwraca jego wiek na podstawie daty urodzenia.

USE AdventureWorks2019;
GO

CREATE FUNCTION WiekPracownika
(
	@PracownikID INT
) 
RETURNS INT
AS
BEGIN
	DECLARE @Wiek INT;

	SELECT @Wiek = DATEDIFF(year, BirthDate, GETDATE())
	FROM HumanResources.Employee
	WHERE BusinessEntityID = @PracownikID;

	RETURN @Wiek
END;



-----wywołanie------

SELECT dbo.WiekPracownika(1)



SELECT * FROM HumanResources.Employee


----------------------------------------------------------------------------------------------------------------------------------------------------

--Zad.3
--Procedura do generowania raportu o stanie magazynowym.

--Napisz procedurę, która generuje raport o stanie magazynowym dla danego magazynu. Raport powinien zawierać informacje o
--nazwie produktu, dostępnej ilości, średniej cenie zakupu i całkowitej wartości zapasów.

USE AdventureWorks2019;
GO

CREATE PROCEDURE GenerujRaportMagazynowy
	@LocationID INT
AS
BEGIN
	SELECT p.Name AS NazwaProduktu, pi.Quantity AS DostepnaIlosc, p.ListPrice AS SredniaCena, pi.Quantity*p.ListPrice AS CalkowitaWartosc FROM Production.ProductInventory pi
	JOIN Production.Product p ON p.ProductID = pi.ProductID
	WHERE LocationID = @LocationID
	ORDER BY p.Name ASC
END;



-----wywołanie------

EXEC GenerujRaportMagazynowy 1;



SELECT * FROM Production.ProductInventory
SELECT * FROM Production.Product


----------------------------------------------------------------------------------------------------------------------------------------------------

--Zad.4
--Procedura do aktualizacji danych kontaktowych klienta.

--Napisz procedurę, która przyjmuje identyfikator klienta oraz nowe dane kontaktowe (adres e-mail i numer telefonu) i aktualizuje odpowiednie rekordy w bazie danych.

USE AdventureWorks2019;
GO

CREATE PROCEDURE AktualizujDaneKontaktoweKlienta
	@KlientID INT,
	@Email NVARCHAR(50),
	@NrTel NVARCHAR(25)
AS
BEGIN
	UPDATE Person.EmailAddress
	SET EmailAddress = @Email
	WHERE BusinessEntityID = @KlientID;

	UPDATE Person.PersonPhone
	SET PhoneNumber = @NrTel
	WHERE BusinessEntityID = @KlientID;
END;



-----wywołanie------

EXEC AktualizujDaneKontaktoweKlienta 1, 'klient@pw.edu.pl', '123-456-789';



SELECT * FROM Person.PersonPhone
SELECT * FROM Person.EmailAddress


----------------------------------------------------------------------------------------------------------------------------------------------------

--Zad.5
--Funkcja do obliczania liczby zamówień złożonych przez klienta w danym roku.

--Napisz funkcję, która przyjmuje identyfikator klienta oraz rok i zwraca liczbę zamówień złożonych przez tego klienta w danym roku.

USE AdventureWorks2019;
GO

CREATE FUNCTION LiczbaZamowienKlientaWRokuX
(
	@KlientID INT,
	@Rok INT
)
RETURNS INT
AS
BEGIN
	DECLARE @IloscZamowien INT;

	SELECT @IloscZamowien = COUNT(SalesOrderID) FROM Sales.SalesOrderHeader
	WHERE CustomerID = @KlientID AND YEAR(OrderDate) = @Rok;

	RETURN @IloscZamowien;
END;



-----wywołanie------

SELECT dbo.LiczbaZamowienKlientaWRokuX(29825,2011);



SELECT * FROM Sales.SalesOrderHeader;


----------------------------------------------------------------------------------------------------------------------------------------------------  [niedokończone]

--Zad.6
--Procedura do generowania raportu o wydajności sprzedaży przedstawiciela handlowego.

--Napisz procedurę, która przyjmuje identyfikator przedstawiciela handlowego (SalesPersonID) i zwraca raport o jego wydajności sprzedaży, 
--zawierający informacje o liczbie zamówień, łącznej wartości sprzedaży oraz średniej wartości zamówienia.

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

SELECT c.name, t.name, s.name
FROM sys.columns c
INNER JOIN sys.tables t ON c.object_id = t.object_id
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
WHERE c.name = 'SalesPersonID'

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

USE AdventureWorks2019;
GO

CREATE PROCEDURE GenerujRaportOWydajnosciPrzedstawicielaHandlowego

AS
BEGIN

END;