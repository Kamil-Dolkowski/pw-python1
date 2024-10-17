
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
	@ProduktID INT,
	@LokacjaID INT,
	@Ilosc INT
AS
BEGIN
	UPDATE Production.ProductInventory 
	SET Quantity = @Ilosc
	WHERE ProductID = @ProduktID AND LocationID = @LokacjaID
END;



SELECT * FROM Production.ProductInventory


--Triggery:--------------------------------------------------------------------------------------------------------------

--4. Trigger automatycznie aktualizujący datę modyfikacji rekordu:
--	Stwórz trigger, który automatycznie aktualizuje datę modyfikacji rekordu w tabeli HumanResources.Employee za każdym razem, gdy zostanie zmieniony jakikolwiek rekord.

USE AdventureWorks2019;
GO

CREATE TRIGGER AktualizacjaDatyModyfikacjiRekordu
ON HumanResources.Employee
AFTER UPDATE, INSERT
AS
BEGIN
	UPDATE HumanResources.Employee 
	SET ModifiedDate = GETDATE()
	WHERE BusinessEntityID = (SELECT i.BusinessEntityID FROM inserted i)
END;




--------------------------------------

SELECT * FROM HumanResources.Employee

--zmiana rekordu
Update HumanResources.Employee
SET Gender = 'M'
WHERE BusinessEntityID = 1;



--??
--5. Trigger sprawdzający poprawność danych podczas dodawania nowego produktu:
--	Stwórz trigger, który sprawdza poprawność danych podczas dodawania nowego produktu, np. czy cena produktu jest większa niż 0 i czy nazwa produktu jest unikalna.


use AdventureWorks2019;
GO

CREATE TRIGGER SprawdzPoprawnoscDanych
ON Production.Product
AFTER INSERT
AS
BEGIN
	IF (SELECT i.StandardCost FROM inserted i) <= 0
	BEGIN
		ROLLBACK;
	END;
	IF (SELECT count(p.Name) FROM Production.Product p JOIN inserted i ON i.ProductID = p.ProductID WHERE p.Name = i.Name) > 1 
	BEGIN
		ROLLBACK;
	END;
END;



---------------------------------------------------------
SELECT * FROM Production.Product

SELECT count(p.Name) FROM Production.Product p 
WHERE p.Name = 'Blade'

SET IDENTITY_INSERT Production.Product ON;
insert into Production.Product (ProductID,Name,StandardCost,ProductNumber,SafetyStockLevel,ReorderPoint,ListPrice,DaysToManufacture,SellStartDate)
VALUES (1000,'Blade1',10,'AABA',1000,750,0,1,GETDATE())
SET IDENTITY_INSERT Production.Product OFF;

DELETE FROM Production.Product 
WHERE ProductID = 1000

