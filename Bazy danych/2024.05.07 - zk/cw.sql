
--1. Procedura usuwająca klienta wraz z jego zamówieniami:
--	Stwórz procedurę, która usuwa klienta z bazy danych wraz ze wszystkimi powiązanymi zamówieniami znajdującymi się w tabeli Sales.SalesOrderHeader.

USE AdventureWorks2019;
GO

CREATE PROCEDURE UsunKlientaWrazZZamowieniami
	@KlientID INT
AS
BEGIN
	IF (SELECT PersonID FROM Sales.Customer WHERE  CustomerID = @KlientID ) is not NULL
		DELETE FROM Person.Person WHERE BusinessEntityID = (SELECT PersonID FROM Sales.Customer WHERE  CustomerID = @KlientID);
	DELETE FROM Sales.Customer WHERE  CustomerID = @KlientID;
	DELETE FROM Sales.SalesOrderHeader WHERE  CustomerID = @KlientID;
END;



--wywołanie:
EXEC UsunKlientaWrazZZamowieniami 11018;



----------------------------------------------------

SELECT * FROM Sales.Customer 
JOIN Person.Person p ON Sales.Customer.PersonID = p.BusinessEntityID
WHERE  CustomerID =11018

SELECT * FROM Sales.SalesOrderHeader WHERE  CustomerID =11018


SELECT * FROM Sales.Customer WHERE  CustomerID =11018


SELECT PersonID FROM Sales.Customer WHERE  CustomerID = 11018


--2. Procedura generująca raport o sprzedaży dla określonego okresu:
--	Stwórz procedurę, która generuje raport o sprzedaży dla określonego okresu czasu, zwracając sumę sprzedaży dla każdego produktu w danym okresie.

USE AdventureWorks2019;
GO

CREATE PROCEDURE Raport
	@BeginDate DATE,
	@EndDate DATE
AS
BEGIN
	SELECT SUM(sod.UnitPrice) suma, sod.ProductID produkty FROM Sales.SalesOrderDetail sod 
	JOIN Sales.SalesOrderHeader soh ON sod.SalesOrderID = soh.SalesOrderID
	WHERE soh.DueDate BETWEEN @BeginDate AND @EndDate
	GROUP BY sod.ProductID
END;



--wywołanie:
EXEC Raport '2010-01-01' , '2019-01-01';

-------------------------------------------------------

SELECT * FROM Sales.SalesOrderHeader --data

SELECT * FROM Sales.SalesOrderDetail --koszt, produkt


SELECT SUM(sod.UnitPrice) suma, sod.ProductID produkts FROM Sales.SalesOrderDetail sod 
JOIN Sales.SalesOrderHeader soh ON sod.SalesOrderID = soh.SalesOrderID
WHERE soh.DueDate BETWEEN '2010-01-01' AND '2014-01-01'
GROUP BY sod.ProductID


SELECT sod.ProductID produkts, soh.DueDate date FROM Sales.SalesOrderDetail sod 
JOIN Sales.SalesOrderHeader soh ON sod.SalesOrderID = soh.SalesOrderID
WHERE soh.DueDate BETWEEN '2010-01-01' AND '2019-01-01'


--3. Procedura aktualizująca stan magazynowy po dodaniu nowej dostawy:
--	Stwórz procedurę, która po dodaniu nowej dostawy aktualizuje stan magazynowy produktów tabeli Production.ProductInventory.

USE AdventureWorks2019;
GO

CREATE PROCEDURE AktualizujStanMagazynowy
	@ProduktID
	@LokacjaID
	@Ilosc
AS
BEGIN
	UPDATE FROM Production.ProductInventory WHERE ProductID = @ProduktID, 
END;



SELECT * FROM Production.ProductInventory


--Triggery:--------------------------------------------------------------------------------------------------------------

--4. Trigger automatycznie aktualizujący datę modyfikacji rekordu:
--	Stwórz trigger, który automatycznie aktualizuje datę modyfikacji rekordu w tabeli HumanResources.Employee za każdym razem, gdy zostanie zmieniony jakikolwiek rekord.





--5. Trigger sprawdzający poprawność danych podczas dodawania nowego produktu:
--	Stwórz trigger, który sprawdza poprawność danych podczas dodawania nowego produktu, np. czy cena produktu jest większa niż 0 i czy nazwa produktu jest unikalna.





