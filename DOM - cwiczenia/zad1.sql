--Procedury składowane:---------------------------------------------------------------------------------------

--1. Procedura dodająca nowego pracownika:
--    Stwórz procedurę, która przyjmuje parametry (imię, nazwisko, data zatrudnienia, dział) i dodaje nowego pracownika do tabeli Person.Person.


???

USE AdventureWorks2019;
GO

CREATE PROCEDURE DodajPracownika
	@FirstName NVARCHAR(50),
	@LastName NVARCHAR(50),
	@HireDate DATE,
	@DepartmentID INT	--?
AS
BEGIN
	DECLARE @BusinessEntityID INT;
	SET @BusinessEntityID = SCOPE_IDENTITY();

	INSERT INTO Person.Person (BusinessEntityID, FirstName, LastName)
	VALUES (@BusinessEntityID, @FirstName, @LastName);

	INSERT INTO HumanResources.Employee (BusinessEntityID, HireDate)
	VALUES (@BusinessEntityID, @HireDate);

	INSERT INTO HumanResources.EmployeeDepartmentHistory (BusinessEntityID, DepartmentID)
	VALUES (@BusinessEntityID, @DepartmentID);

END;




INSERT INTO HumanResources.Employee (BusinessEntityID, HireDate, NationalIDNumber, LoginID, JobTitle, BirthDate, MaritalStatus, Gender)
	VALUES (291, '2024-01-01', '123456789', 'login', 'Boss', '1990-01-01', 'M', 'F');

    

--2. Procedura zmieniająca adres pracownika:
--    Stwórz procedurę, która przyjmuje ID pracownika i nowy adres, a następnie aktualizuje adres pracownika w tabeli HumanResources.EmployeeAddress.

USE AdventureWorks2019;
GO

CREATE PROCEDURE ZmienAdresPracownika
	@PracownikID INT,
	@AddressLine1 NVARCHAR(60),
	@City NVARCHAR(30),
	@StateProcinceID INT,
	@PostalCode NVARCHAR(15)
AS
BEGIN
	DECLARE @AddressID INT;
	SELECT @AddressID = bea.AddressID FROM Person.BusinessEntityAddress bea WHERE BusinessEntityID = @PracownikID;

	UPDATE Person.Address 
	SET AddressLine1 = @AddressLine1, City = @City, StateProvinceID = @StateProcinceID, PostalCode = @PostalCode
	WHERE AddressID = @AddressID;
END;


--Wywołanie:
EXEC ZmienAdresPracownika 111, 'ul. Łukasiewicza 17', 'Płock', 1, '09-400';


--3. Procedura wyliczająca roczne wynagrodzenie:
--    Stwórz procedurę, która przyjmuje ID pracownika i zwraca roczne wynagrodzenie pracownika na podstawie jego pensji miesięcznej.


???

BRAK PENSJI MIESIĘCZNEJ
HumanResources.EmployeePayHistory



--Funkcje skalarne:---------------------------------------------------------------------------------------

--4. Funkcja obliczająca wiek pracownika:
--    Stwórz funkcję, która przyjmuje datę urodzenia pracownika i zwraca jego wiek w latach.

USE AdventureWorks2019;
GO

CREATE FUNCTION ObliczWiekPracownika
(
	@DataUrodzenia DATE
)
RETURNS INT
AS
BEGIN
	DECLARE @Wiek INT;

	SELECT @Wiek = DATEDIFF(YEAR, @DataUrodzenia, GETDATE());

	RETURN @Wiek;
END;



--Wywołanie:
DECLARE @Wynik INT;
DECLARE @Data DATE = '2020-01-01';

EXEC @Wynik = ObliczWiekPracownika @Data;

SELECT @Wynik as Wiek_w_latach;


--5. Funkcja sprawdzająca dostępność produktu:
--    Stwórz funkcję, która przyjmuje ID produktu i zwraca 'Dostępny', jeśli produkt jest w magazynie, a 'Niedostępny', jeśli nie ma go w magazynie.

USE AdventureWorks2019;
GO

CREATE FUNCTION SprawdzDostepnoscProduktu
(
	@ProductID INT
)
RETURNS VARCHAR(11)
AS
BEGIN
	DECLARE @X INT;
	DECLARE @Wynik VARCHAR(11);
	SELECT @X = (SELECT count(ProductID) FROM Production.ProductInventory WHERE ProductID = @ProductID group by ProductID);

	IF @X > 0
		SELECT @Wynik = 'Dostępny';
	ELSE
		SELECT @Wynik = 'Niedostępny';

	RETURN @Wynik;
END;



--Wywołanie:
DECLARE @ProduktID INT = 2;
DECLARE @Wynik NVARCHAR(11);

EXEC @Wynik = SprawdzDostepnoscProduktu @ProduktID;

SELECT @Wynik AS Stan;


--Triggery:---------------------------------------------------------------------------------------

--6. Trigger sprawdzający maksymalną liczbę pracowników w dziale:
--    Stwórz trigger, który po próbie dodania nowego pracownika sprawdza, czy liczba pracowników w danym dziale nie przekracza ustalonej maksymalnej liczby.

?

USE AdventureWorks2019;
GO

CREATE TRIGGER MaksymalnaLiczbaPracownikowWDziale
ON HumanResources.Employee
AFTER INSERT
AS
BEGIN
	IF EXISTS (SELECT * FROM inserted)
	BEGIN
		DECLARE @DepartmentID INT;
		DECLARE @X INT;

		SELECT TOP 1 @DepartmentID = DepartmentID FROM HumanResources.EmployeeDepartmentHistory ORDER BY BusinessEntityID DESC
		SELECT @X = count(BusinessEntityID) FROM HumanResources.EmployeeDepartmentHistory WHERE DepartmentID = @DepartmentID group by DepartmentID 

		IF @X = 20		-- liczba osób w dziale
			SELECT 'Nie przekroczono liczby osób w dziale.'
		ELSE
			SELECT 'Za dużo osób w dziale!'
            ROLLBACK TRANSACTION;
	END;
END;


--7. Trigger aktualizujący stan magazynowy po zmianie zamówienia:
--    Stwórz trigger, który po zmianie zamówienia aktualizuje stan magazynowy produktów w tabeli Production.ProductInventory.


USE AdventureWorks2019;
GO

CREATE TRIGGER AktualizacjaStanuMagazynowego
ON Sales.SalesOrderDetail
AFTER UPDATE
AS
BEGIN
	IF (UPDATE(ProductID) OR UPDATE(OrderQty))
		BEGIN
			DECLARE @ProductID INT;
			SELECT @ProductID = i.ProductID FROM inserted i

			DECLARE @Roznica INT;

			DECLARE @X INT;
			DECLARE @Y INT;


			SELECT @X = d.OrderQty FROM deleted d WHERE ProductID = @ProductID
			SELECT @Y = i.OrderQty FROM inserted i WHERE ProductID = @ProductID

			SELECT @Roznica = @X - @Y;

			UPDATE Production.ProductInventory
			SET Quantity = Quantity + @Roznica
			WHERE ProductID = @ProductID
		END;
END;




--------------------------------------

UPDATE Sales.SalesOrderDetail
SET OrderQty = 4
WHERE SalesOrderID = 43659 and SalesOrderDetailID = 1

SELECT * FROM Sales.SalesOrderDetail
WHERE SalesOrderID = 43659 and SalesOrderDetailID = 1


SELECT * FROM Production.ProductInventory WHERE ProductID = 876


UPDATE Production.ProductInventory
SET Quantity = 10
WHERE ProductID = 876


--8. Trigger archiwizujący dane klientów:
--    Stwórz trigger, który po usunięciu rekordu klienta z tabeli Sales.Customer, przenosi ten rekord do tabeli Sales.ArchivedCustomers w celu archiwizacji.


???

USE AdventureWorks2019;
GO

CREATE TRIGGER ArchiwizacjaDanychKlientow
ON Sales.Customer
AFTER DELETE
AS
BEGIN
	INSERT INTO Sales.ArchivedCustomers ()
    VALUES ();
END;
