use AdventureWorks2019;
GO

--1. Wypisz klientów z tabeli Sales.Customer, sortując ich nazwisko (LastName) w porządku malejącym.

--SELECT * 
--FROM Sales.Customer s
--RIGHT JOIN Person.Person p ON s.PersonID = p.BusinessEntityID 
--ORDER BY p.LastName DESC;



--SELECT p.LastName
--FROM Sales.Customer c
--JOIN Person.Person p ON p.BusinessEntityID = c.CustomerID
--ORDER BY p.LastName DESC







--2. Podaj średnią cenę (ListPrice) produktów dla każdej kategorii produktów z tabeli Production.Product.

--SELECT pc.Name, AVG(p.ListPrice)
--FROM Production.Product p
--JOIN Production.ProductSubcategory ps ON ps.ProductSubcategoryID = p.ProductSubcategoryID
--JOIN Production.ProductCategory pc ON pc.ProductCategoryID = ps.ProductSubcategoryID
--GROUP BY pc.Name






--3. Z tabeli Person.Person wybierz osoby, dla których FirstName zaczyna się na literę 'A', używając funkcji LEFT().

--SELECT p.FirstName
--FROM Person.Person p
--WHERE LEFT(p.FirstNAme, 1) = 'A'






--4. Wyświetl nazwiska (LastName) pracowników i nazwy działów (Name), w których pracują, korzystając z tabel HumanResources.Employee, Person.Person i HumanResources.Department.

--SELECT p.LastName, d.Name
--FROM HumanResources.Employee emp
--JOIN Person.Person p ON p.BusinessEntityID = emp.BusinessEntityID
--JOIN HumanResources.EmployeeDepartmentHistory edh ON edh.BusinessEntityID = emp.BusinessEntityID
--JOIN HumanResources.Department d ON d.DepartmentID = edh.DepartmentID






--5. Wybierz nazwy działów i liczbę pracowników w każdym dziale z tabeli HumanResources.Department i HumanResources.EmployeeDepartmentHistory, grupując wyniki po nazwie działu.

--SELECT d.Name, COUNT(edh.DepartmentID) AS employeeCount
--FROM HumanResources.Department d
--JOIN HumanResources.EmployeeDepartmentHistory edh ON edh.DepartmentID = d.DepartmentID
--GROUP BY d.Name
--ORDER BY employeeCount DESC








--6. Z tabeli Person.Person wybierz FirstName i LastName oraz utwórz nową kolumnę FullName, która będzie zawierać pełne imie i nazwisko, oddzielone spacją.

----niezrobione
--SELECT p.FirstName, p.LastName
--FROM Person.Person p
--ALTER TABLE Person.Person
--ADD FullName varchar(50)



----odp
--SELECT FirstName, LastName, concat(FirstName, ' ', LastName) AS FullName FROM Person.Person;








--7. Napisz zapytanie, które dodaje nowego pracownika do HumanResources.Employee, a następnie aktualizuje jego JobTitle, wszytstko w ramach jednej transakcji.  [niedokończone]

--BEGIN TRANSACTION;
--INSERT INTO Person.Person

--INSERT INTO HumanResources.Employee

--COMMIT TRANSACTION;








--8. Wybierz ProductID i OrderQty z tabeli Sales.SalesOrderDetail dla SalesOrderID poniżej 1000 i zapisz wyniki w tabeli tymczasowej. Następnie wybierz wszytskie rekordy z tej samej tabeli tymczasowej.

--SELECT ProductID, OrderQty INTO #TempOrder
--FROM Sales.SalesOrderDetail
--WHERE SalesOrderID > 1000

--SELECT * FROM #TempOrder







--9. Napisz skrypt, który dynamicznie tworzy i wykonuje zapytanie SQL wybierające wszystkie kolumny z tabeli Person.Address i sortujące wyniki według City.

--DECLARE @query as NVARCHAR(MAX);
--SET @query= 'SELECT * FROM PERSON.Address ORDER BY City';
--EXEC sp_executesql @query





--10. Wybierz z tabeli Sales.SalesOrderHeader kolumny SalesOrderID i OrderDate. Użyj funkcji TRY_CONVERT do przekonwertowania OrderDate na format YYYY-MM-DD.		[?]

--SELECT sod.SalesOrderID, sod.OrderDate
--FROM Sales.SalesOrderHeader sod

----SELECT TRY_CONVERT(datetime, '2000-12-12');
--SELECT CONVERT (nvarchar(30), sod.OrderDate, 110) AS USdate;








--11. Wyświetl BusinessEntityID i liczbę dni, które upłynęły od daty zatrudnienia (HireDate) do dzisiaj dla każdego pracownika z tabeli HumanResources.Employee.

SELECT e.BusinessEntityID, DATEDIFF(day, e.HireDate, GETDATE()) as DaysNumber
FROM HumanResources.Employee e







--12. Wybierz OrderDate z tabeli Sales.SalesOrderHeader i sformatuj daty w formacie 'MM-dd-yyyy'.









--13. Z tabeli Person.Person wybierz BusinessEntityID, FirstName, LastName oraz kolnumę IsFemale, która będzie zawierała wartość TRUE, jeśli Gender = 'F', w przeciwnym razie FALSE.










--14. Znajdź wszystkie duplikaty EmailAddress w tabeli Person.Person.

--SELECT e.EmailAddress, COUNT(*)
--FROM Person.Person p
--JOIN Person.EmailAddress e ON e.BusinessEntityID = p.BusinessEntityID
--GROUP BY EmailAddress having COUNT(*) > 1;








--15. Utwórz widok V_EmployeeDepartment, który wyświetla imiona i nazwiska pracowników oraz nazwy ich działów z tabel HumanResources.Employee, preson.Person i humanResources.Department











--16. Optymalizuj zapytanie, które łączy tabele Sales.SalesOrderHearde, Sales.SalesOrderDetail, Production.Product i Person.Person, aby znaleźć wszystkie zamówienia zawierające więcej niż 1 produkt, wraz z informacjami o klientach.














--**
--Na json

--SELECT SalesOrderID, OrderDate
--FROM Sales.SalesOrdeHeader
--FOR JSON PATH;












SELECT * FROM sys.database_files 





SELECT f.name,
size/123 AS currentsizeMB,
f.growth/128 AS growthSizeMB
FROM sys.database_files f
WHERE f.type_desc='ROWS'






SELECT f.name,
size/123 AS currentsizeMB,
f.growth/128 AS growthSizeMB
size/128.0 CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS FreeSpaceMB
FROM sys.database_files f
WHERE f.type_desc='ROWS'