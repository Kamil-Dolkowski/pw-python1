use AdventureWorks2019;
GO

--Wypisz klientów z tabeli Sales.Customer, sortując ich nazwisko (LastName) w porządku malejącym.

--SELECT * 
--FROM Sales.Customer s
--RIGHT JOIN Person.Person p ON s.PersonID = p.BusinessEntityID 
--ORDER BY p.LastName DESC;



--SELECT p.LastName
--FROM Sales.Customer c
--JOIN Person.Person p ON p.BusinessEntityID = c.CustomerID
--ORDER BY p.LastName DESC




--Podaj średnią cenę (ListPrice) produktów dla każdej kategorii produktów z tabeli Production.Product.

--SELECT pc.Name, AVG(p.ListPrice)
--FROM Production.Product p
--JOIN Production.ProductSubcategory ps ON ps.ProductSubcategoryID = p.ProductSubcategoryID
--JOIN Production.ProductCategory pc ON pc.ProductCategoryID = ps.ProductSubcategoryID
--GROUP BY pc.Name





--Z tabeli Person.Person wybierz osoby, dla których FirstName zaczyna się na literę 'A', używając funkcji LEFT().

--SELECT p.FirstName
--FROM Person.Person p
--WHERE LEFT(p.FirstNAme, 1) = 'A'






--Wyświetl nazwiska (LastName) pracowników i nazwy działów (Name), w których pracują, korzystając z tabel HumanResources.Employee, Person.Person i HumanResources.Department.

--SELECT p.LastName, d.Name
--FROM HumanResources.Employee emp
--JOIN Person.Person p ON p.BusinessEntityID = emp.BusinessEntityID
--JOIN HumanResources.EmployeeDepartmentHistory edh ON edh.BusinessEntityID = emp.BusinessEntityID
--JOIN HumanResources.Department d ON d.DepartmentID = edh.DepartmentID






--Wybierz nazwy działów i liczbę pracowników w każdym dziale z tabeli HumanResources.Department i HumanResources.EmployeeDepartmentHistory, grupując wyniki po nazwie działu.

--SELECT d.Name, COUNT(edh.DepartmentID) AS employeeCount
--FROM HumanResources.Department d
--JOIN HumanResources.EmployeeDepartmentHistory edh ON edh.DepartmentID = d.DepartmentID
--GROUP BY d.Name
--ORDER BY employeeCount DESC








--Z tabeli Person.Person wybierz FirstName i LastName oraz utwórz nową kolumnę FullName, która będzie zawierać pełne imie i nazwisko, oddzielone spacją.

SELECT p.FirstName, p.LastName
FROM Person.person p
ALTER TABLE 






--Napisz zapytanie, które dodaje nowego pracownika do HumanResources.Employee, a następnie aktualizuje jego JobTitle, wszytstko w ramach jednej transakcji.

BEGIN TRANSACTION;
INSERT INTO Person.Person

INSERT INTO HumanResources.Employee

COMMIT TRANSACTION;