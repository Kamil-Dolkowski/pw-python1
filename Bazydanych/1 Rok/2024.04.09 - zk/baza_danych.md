AdventureWorks

AdventureWorks2019.bak

daza danych -> restore database -> device -> [...] -> wybrać plik

#-------------OR / UNION---------------
(3,7s)
SELECT DISTINCT
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.ProductID = DETAIL.ProductID
OR PRODUCT.rowguid = DETAIL.rowguid;
GO



Clustered Index Scan
Estimeted Operator Cost
Object
Output List



SET STATISTICS IO ON


(0,028s)
SELECT 
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.ProductID = DETAIL.ProductID
UNION
SELECT 
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.rowguid = DETAIL.rowguid;

#----------------OR / IN----------------

SELECT 
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.ProductID = DETAIL.ProductID
WHERE PRODUCT.ProductID = DETAIL.ProductID in (709,710)




SELECT 
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.ProductID = DETAIL.ProductID
WHERE PRODUCT.ProductID = 709
OR PRODUCT.ProductID = 710



#-------------------------------------

(105 odczytów ?)
SELECT 
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
WHERE exists(SELECT 1 FROM Sales.SalesOrderDetail DETAIL WHERE PRODUCT.ProductID = DETAIL.ProductID)



(2 odczyty)
SELECT
    Person.BusinessEntityID,
    Person.Firstname,
    Person.Lastname,
    Person.Middlename,
FROM Pesron.Person
WHERE Person.LastName LIKE 'For%';



#-------------------------------------

SELECT ProductID, OrderQty FROM Sales.SalesOrderDetail WHERE ProductID > 1000;


(duża ilość ??)
SELECT * FROM Sales.SalesOrderHeader AS soh
INNER JOIN Sales.Customer AS c ON soh.CustomerID = c.CustomerID
INNER JOIN Sales.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID
INNER JOIN Production.Product AS p ON sod.ProductID = p.ProductID;



#--------------------------------------

(użycie funkcji wbudowaniej (niejawna konwersja))
SELECT SalesOrderID, YEAR(OrderDate) FROM Sales.SalesOrderHeader WHERE YEAR(OrderDate) = 2011;


SELECT SalesOrderID, YEAR(OrderDate) FROM Sales.SalesOrderHeader WHERE OrderDate >= '2021-01-01' AND OrderDate < '2022-01-01';



#----------BRAKUJĄCE INDEKSY-----------

Ze strony microsoftu:
https://learn.microsoft.com/en-us/sql/relational-databases/indexes/tune-nonclustered-missing-index-suggestions?view=sql-server-ver16


SELECT TOP 20
    CONVERT (varchar(30), getdate(), 126) AS runtime,
    CONVERT (decimal (28, 1), 
        migs.avg_total_user_cost * migs.avg_user_impact * (migs.user_seeks + migs.user_scans) 
        ) AS estimated_improvement,
    'CREATE INDEX missing_index_' + 
        CONVERT (varchar, mig.index_group_handle) + '_' + 
        CONVERT (varchar, mid.index_handle) + ' ON ' + 
        mid.statement + ' (' + ISNULL (mid.equality_columns, '') + 
        CASE
            WHEN mid.equality_columns IS NOT NULL
            AND mid.inequality_columns IS NOT NULL THEN ','
            ELSE ''
        END + ISNULL (mid.inequality_columns, '') + ')' + 
        ISNULL (' INCLUDE (' + mid.included_columns + ')', '') AS create_index_statement
FROM sys.dm_db_missing_index_groups mig
JOIN sys.dm_db_missing_index_group_stats migs ON 
    migs.group_handle = mig.index_group_handle
JOIN sys.dm_db_missing_index_details mid ON 
    mig.index_handle = mid.index_handle
ORDER BY estimated_improvement DESC;
GO



#--------------------------------------

we FROM dawać największą tabelę -> efektywność



SELECT soh.SalesOrderID, soh.TotalDue, c.AccountNumber
FROM Sales.SalesOrderHeader As soh
INNER JOIN Sales.Customer AS c ON soh.CustomerID = c.CustomerID
WHERE soh.TotalDue > 10000;



SELECT [SalesOrderID], OrderDate
FROM Sales.SalesOrderHeader
ORDER BY OrderDate ASC;     (rosnąco)



SELECT CustomerID, COUNT(*) FROM Sales.SalesOrderHeader
GROUP BY CustomerID HAVING COUNT(*) > 5;

SELECT CustomerID
FROM Sales.SalesOrderHeader
GROUP BY CustomerID
HAVING COUNT(*) >5;



#---------------ALIASY---------------

SELECT OrderID, Orders.CustomerID, OrderDate FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

SELECT o.OrderID, o.CustomerID, o.OrderDate FROM Orders o JOIN Customers c ON o.CustomerID = c.Customer;



#--------------------------------------

SELECT CustomerID, (SELECT COUNT(*) FROM Orders WHERE Orders.CustomerID = Customes.CustomerID) AS OrderCount FROM Customers;

SELECT c.CustomerID, COUNT(o.OrderID) AS OrderCount FROM Customers.c LEFT JOIN Orders o ON c.CustomerID = o.CustomerID GROUP BY c.CustomerID;


SELECT OrderID, CustomerID, OrderDate FROM Orders ORDER BY GETDATE() = OrderDate;


SELECT * FROM Products, Orders;
SELECT p.ProductID, o.OrderID FROM Products p INNER JOIN Orders o ON p.ProductID = o.ProductID;



SELECT c.CustomerID
FROM Sales.Customer AS c
LEFT JOIN Sales.SalesOrderHeader As soh ON c.CustomerID = soh.CustomerID
WHERE soh.SalesOrderID IS NULL;