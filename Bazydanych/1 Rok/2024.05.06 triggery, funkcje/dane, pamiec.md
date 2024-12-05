# Przechowywanie danych i zarządzanie pamięcią

#---------------------------------------------------------------------

Hierarchia obiektów


baza jest składowana niezależnie, w przynajmniej 2 plikach (plik bazy danych i plik logów)

Databases -> properties -> files


Wszystkie obiekty bazodanowe muszą posiadać unikalną nazwę, w ramach bazy danych.
W pełni kwalifikowana nazwa obiektu jest 4-członowa:
<nazwa_serwera>.<nazwa_bazy>.<nawza_schematu>.<nazwa_obiektu>

Dzięki temu, jest jednoznacznie określona.

Minimalna zalecana nazwa, po której się odwołujemy jest 2-członowa: 
<nazwa_schematu>.<nazwa_obiektu>

#---------------------------------------------------------------------

# Schemat:
-niezależna warstwa, związana z zarządzaniem bezpieczeństwem
-kontener, w ramach którego tworzone są obiekty

select SCHEMA_NAME() as DefaultSchema;
use AdventureWorks2019
go 
select FirstName, LastName from Person

Msg 208, Level 16, State 1, Line 2
Invalid object name 'Person'

Poprawnie:
select * from Person.Person

#---------------------------------------------------------------------

# Tabela:
-podstawowe obiekty w bazie
-definicja pwenej klasy obiektów
-zbiór elementów opisany za pomocą atrybutów (kolumn)
-każdy atrybut jest określany typem danych
-mocna hierarchizacja

# Tabela:
-kolumny (atrybuty)
-klucze (relacje)
-ograniczenia (constrains)      [integralność danych]
-procedury wyzwalane (triggers)
-indeksy i statystyki

#---------------------------------------------------------------------

# Widoki (perspektywa - w ORACLE):
-zapisana kwerenda
-czasem nazywane wirtualnymi tabelami
-niezmaterializowane tabele wirtualne

#---------------------------------------------------------------------

# Synonimy:
-aliasy nazw obiektów
-pomocne przy migracjach lub modyfikacjach środowiska
-alternatywne nazwy obiektów ...

#---------------------------------------------------------------------

# Obiekty programistyczne

#---------------------------------------------------------------------

# Procedury składowane (Stored Procedures):
-niezależne jednostki, skrypty T-SQL, realizujące dowolne funkcje programistyczne
-mogą np. importować dane z pliku, dokonując przy okazji szeregu weryfikacji (czyszczenia)
-mogą przyjmować parametry, zwracać wyniki
-nie mogą być używane w kwerendach 

#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE PROCEDURE DodajNoweZamowienie
    @CustomerID INT,
    @OrderDate DATE,
    @ProductID INT,
    @Quantity INT
AS
BEGIN
    DECLARE @OrderID INT;

    INSERT INTO Sales.SalesOrderHeader (CustomerID, OrderDate)
    Values (@CustomerID, @OrderDate);

    SET @OrderID = SCOPE_IDENTITY();

    INSERT INTO Sales.SalesOrderDetail (SalesOrderID, ProductID, OrderQty)
    Values (@OrderID, @ProductID, @Quantity);
END;


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE PROCEDURE PobierzSzczegolyZamowienia
    @OrderID INT
AS
BEGIN
    SELECT sod.SalesOrderID, sod.ProductID, p.Name AS ProductName, sod.OrderQty, [???]
    FROM Sales.SalesOrderDetail sod
    INNER JOIN Production.Product p ON sod.ProductID = p.ProductID
    WHERE sod.SalesOrderID = @OrderID;
END;

#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE PROCEDURE AktualizujDaneKlienta
    @CustomerID INT,
    @NewName NVARCHAR(50),
    @NewEmail NVARCHAR(100)
AS
BEGIN
    UPDATE Sales.Customer
    SET Name = @NewName,
        Email = @NewEmail
    WHERE CustomerID = @CustomerID;
END;

#---------------------------------------------------------------------

# Assemblies:
-SQL Server umożliwia integrację środowiska CLR
-możemy tworzyć obiekty programistyczne w .NET i używać ich w ramach serwera bazy danych

#---------------------------------------------------------------------

# CLR:
-funkcja integracji środowiska uruchomieniowego języka wspólnego (CLR)
-domyślnie włączona w MSSQL


sp_configure 'clr enabled', 1
GO
RECONFIGURE
GO

#---------------------------------------------------------------------

# Triggery
-specjalny typ procedur wyzwalanych, wywoływane na skutek operacji DDL

#- - - - - - - - - - - - - - - - - -

CREATE TRIGGER nazwa_triggera
ON nazwa_tabeli
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    -- ciało triggera
END;

#- - - - - - - - - - - - - - - - - -

# Rodzaje triggerów:
-AFTER Triggers - wykonują się po zakończeniu operacji
-INSTEAD OF Triggers - wyświetlają się zamiast standardowej operacji


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE TRIGGER LogowanieZmianProduktow
ON Production.Product
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted) OR EXISTS (SELECT * FROM deleted)
    BEGIN
        INSERT INTO dbo.ProductChangeLog (ChangeDate, Action)
        VALUES (GETDATE(), 'Zmiana w tabeli Product');
    END;
END;


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE TRIGGER AktualizacjaStanuMagazynowego
ON Sales.SalesOrderDetail
AFTER INSERT
AS 
BEGIN
    UPDATE Production.ProductInventory
    SET Quantity = Quantity - i.OrderQty
    FROM Production.ProductInventory pi
    JOIN inserted i ON pi.ProductID = i.ProductID;
END;


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE TRIGGER SprawdzaniePoprawnosciDanych
ON Sales.SalesOrderDetail
AFTER DELETE
As
BEGIN
    IF EXISTS (SELECT * FROM Production.ProductInventory WHERE Quantity < 0)
    BEGIN
        RAISEERROR('Usuniecie zamówienia spowoduje ujemny stan magazynowy!', 16, 1);
        ROLLBACK TRANSACTION;
    END;
END;

#---------------------------------------------------------------------

# Funkcje systemowe:
-GETDATE
-LEN
-UPPER

# Funkcje skalarne:
-

#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE FUNCTION PobierzIloscZamowienKlienta
(
    @CustomerID INT
)
RETURNS INT
AS
BEGIN
    DECLARE @OrderCount INT;

    SELECT @OrderCount = COUNT(*)
    FROM Sales.SalesOrderHeader
    WHERE CustomerID = @CustomerID;

    RETURN @OrderCount;
END;


---------Wywołanie funkcji:---------
1.sposób:

DECLARE @CustomID INT = 11075;

DECLARE @Ordercount INT;

EXEC @OrderCount = PobierzIloscZamowienKlienta @CustomID;

SELECT @OrderCount


2.sposób:
SELECT dbo.PobierzIloscZamowienKlienta(11075)




#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE FUNCTION ObliczWartoscZamowienia
(
    @OrderID INT
)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalAmount MONEY;

    SELECT @TotalAmount = SUM(UnitPrice * OrderQty)
    FROM Sales.SalesOrderDetail
    WHERE SalesOrderID = @OrderID;

    RETURN @TotalAmount;
END;


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE FUNCTION KonwertujDate
(
    @DateIn INT
)
RETURNS DATE
AS
BEGIN
    DECLARE @DateOut DATE;

    SELECT @DateOut = CONVERT(DATE, CONVERT(VARCHAR(8), @DateIN), 112);

    RETRUN @DateOut;
END;


#---------------------------------------------------------------------

# Funkcje tabelaryczne:
-zwracają zbiór elementów
-we FROM, a nie w SELECT


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE FUNCTION PobierzProduktyZKategorii
(
    @CategoryID INT
)
RETURNS TABLE
AS
RETURN
(
    SELECT p.ProductID, p.Name AS ProductName, p.Color, p.ListPrice
    FROM Production.Product p
    INNER JOIN Production.ProductSubcategory ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID
    WHERE ps.ProductCategoryID = @CategoryID
);


#---------------------------------------------------------------------

# Types:
-pochodne istniejących typów
-customizacja parametrów
-łatwa definicja


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE TYPE AddressType AS TABLE
(
    AddressLine1 NVARCHAR(100),
    AddressLine2 NVARCHAR(100),
    City NVARCHAR(50),
    State NVARCHAR(50),
    ...
)


#- - - - - - - - - - - - - - - - - -

USE AdventureWorks2019;
GO

CREATE PROCEDURE InsertCustomerWithAddress
(
    @FirstName NVARCHAR(50),
    @LastName NVARCHAR(50),
    @Address AddressType READONLY
)
AS
BEGIN
    DECLARE @CustomerID INT;

    INSERT INTO Sales.Customer (FirstName, LastName)
    VALUES (@FirstName, @LastName);

    SET @CustomerID = SCOPE_IDENTITY();

    INSERT INTO Sales.CustomerAddress (CustomerID ...)

    ...



#- - - - - - - - - - - - - - - - - -


DECLARE @Address AddressTYpe;

INSERT INTO @Address (AddressLine1, City, State, PostalCode, Country)
...


#---------------------------------------------------------------------

Rules
(stare)


# Constrains:
-reguły, warunki narzucane na dane w tabelach w celu integralności danych
-spójność
-zapobiegają wprowadzenie nieprawidłowych danych


#---------------------------------------------------------------------
