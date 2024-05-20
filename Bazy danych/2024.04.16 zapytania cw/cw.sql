USE AdventureWorks2019;
GO


--1. Wypisz wszystkich pracowników (FirstName, LastName) wraz z ich stanowiskiem (JobTitle) z tabeli HumanResources.Employee oraz Person.Person, gdzie data zatrudnienia (HireDate) jest późniejsza niż 1 stycznia 2007 r.

--mój
--SELECT FirstName, LastName, JobTitle 
--FROM Person.Person, HumanResources.Employee 
--WHERE HireDate > '2007-01-01';

--zobacz, co w tabelach
SELECT e.JobTitle, e.HireDate FROM HumanResources.Employee e WHERE e.HireDate > '2007-01-01'
SELECT p.FirstName, p.LastName FROM Person.Person p

--lepsza opcja
SELECT e.JobTitle, p.FirstName, p.LastName
FROM HumanResources.Employee e
INNER JOIN Person.Person p 
ON e.BusinessEntityID = p.BusinessEntityID AND e.HireDate > '2007-01-01';

--CREATE INDEX idx_HireDate ON HumanResources.Employee(HireDate)

--gorsza opcja
SELECT e.JobTitle, p.FirstName, p.LastName
FROM HumanResources.Employee e
INNER JOIN Person.Person p 
ON e.BusinessEntityID = p.BusinessEntityID 
WHERE e.HireDate > '2007-01-01';



--2. Znajdź średnią cenę produktów (ListPrice) dla każdej kategorii produktów (Name) z tabel Production.Product oraz Production.ProductCategory.

--zobacz
SELECT *
FROM Production.Product

--zobacz
SELECT *
FROM Production.ProductCategory;

--mój (źle)
SELECT AVG(p.ListPrice) AS Avg, pc.Name
FROM Production.Product p
RIGHT JOIN Production.ProductCategory pc ON p.ProductSubcategoryID = pc.ProductCategoryID
GROUP BY pc.Name

--dobrze
SELECT pc.Name AS Category, AVG(p.ListPrice) AS avgListPrice FROM Production.Product p
INNER JOIN Production.ProductSubcategory as ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID
INNER JOIN Production.ProductCategory pc ON pc.ProductCategoryID = ps.ProductCategoryID
GROUP BY pc.Name
ORDER BY 1


--3. Wypisz nazwy produktów, które nigdy nie zostały zamówione (wykorzystaj tabele Sales.SalesOrderDetail i Production.Product).

--część wspólna
SELECT * FROM Production.Product p, Sales.SalesOrderDetail sod
WHERE p.ProductID = sod.ProductID

--sposób1
SELECT p.Name FROM Production.Product p
WHERE p.ProductID NOT IN ( SELECT sod.ProductID FROM Sales.SalesOrderDetail sod)

--sposób2
SELECT p.Name FROM Production.Product p
WHERE NOT EXISTS ( SELECT 1 FROM Sales.SalesOrderDetail sod WHERE sod.ProductID = p.ProductID)

--sposób3
SELECT p.Name, sod.OrderQty FROM Production.Product p
LEFT JOIN Sales.SalesOrderDetail sod ON sod.ProductID = p.ProductID
WHERE sod.ProductID is null

--porównanie
SELECT count(1) FROM Production.Product p
LEFT JOIN Sales.SalesOrderDetail sod ON sod.ProductID = p.ProductID
WHERE sod.ProductID is null

SELECT count(1) FROM Production.Product p
LEFT JOIN Sales.SalesOrderDetail sod ON sod.ProductID = p.ProductID
AND sod.ProductID is null

--w Produktach nie ma usuniętych produktów, które są w Sprzedaży, dlatego wyświetla różne wartości



--4. Utwórz zapytanie indeks na kolumnie HireDate w tabeli HumanResources.Employee




--Znajdź wszystkie zamówienia dla klienta o CustomerID równym 1, które zawierają więcej niż 5 różnych produktów,. Użyj tabeli Sales.SalesOrderHeader i Sales.SalesOrderDetail.

SELECT * FROM Sales.SalesOrderHeader

SELECT * FROM Sales.SalesOrderDetail


--wszystkie zamówienia klienta
SELECT SalesOrderID 
FROM Sales.SalesOrderHeader
WHERE CustomerID = 29825

--?
SELECT soh.SalesOrderID
FROM Sales.SalesOrderHeader soh, Sales.SalesOrderDetail sod
WHERE soh.CustomerID = 29825 


--odp
SELECT h.SalesOrderID, COUNT(d.ProductID) ilosc_produktow
FROM Sales.SalesOrderHeader h
INNER JOIN Sales.SalesOrderDetail d ON h.SalesOrderID = d.SalesOrderID
WHERE h.CustomerID=1
GROUP BY h.SalesOrderID
HAVING COUNT(DISTINCT d.ProductID) > 5;