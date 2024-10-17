--Zad.3
--Partycjonowanie poziome według regionu
--Cel: Podziel tabelę Sales.SalesOrderHeader na partycje według kolumny TerritoryID.
--Treść zadania:
--1. Utwórz schemat partycjonowania dla tabeli Sales.SalesOrderHeader według kolumny TerritoryID.
--2. Stwórz odpowiednią funkcję partycjonowania.
--3. Utwórz nową tabelę partycjonowaną, która będzie przechowywać dane z tabeli Sales.SalesOrderHeader.
--4. Przenieś dane z oryginalnej tabeli do nowej tabeli partycjonowanej.

use AdventureWorks2019;
GO

CREATE PARTITION FUNCTION SalesTerritoryID_PF (INT)					--RIGHT -> [x,y)
AS RANGE RIGHT FOR VALUES (2,4,6,8);	--TerritoryID [1-10]		--LEFT  -> (x,y]


CREATE PARTITION SCHEME SalesTerritoryID_PS
AS PARTITION SalesTerritoryID_PF
TO ([PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY]);


CREATE TABLE Sales.SalesOrderHeader_TerritoryID_Partitioned
(
	TerritoryID INT NOT NULL,
	SalesOrderID INT NOT NULL,
	OrderDate datetime NOT NULL,
	/* pozostałe kolumny */
	CONSTRAINT PK_SalesOrderHeader_TerritoryID_Partitioned PRIMARY KEY CLUSTERED (SalesOrderID, TerritoryID)
) ON SalesTerritoryID_PS(TerritoryID);

INSERT INTO Sales.SalesOrderHeader_TerritoryID_Partitioned
(TerritoryID, SalesOrderID, OrderDate /* pozostałe kolumny */)
SELECT TerritoryID, SalesOrderID, OrderDate /* pozostałe kolumny */
FROM Sales.SalesOrderHeader;





select * from Sales.SalesOrderHeader_TerritoryID_Partitioned 
select TerritoryID, SalesOrderID from Sales.SalesOrderHeader_TerritoryID_Partitioned 


--------------------------------------------------------------------------------------------------------------
--(cała tabela)

--Zad.3'
--Partycjonowanie poziome według regionu
--Cel: Podziel tabelę Sales.SalesOrderHeader na partycje według kolumny TerritoryID.
--Treść zadania:
--1. Utwórz schemat partycjonowania dla tabeli Sales.SalesOrderHeader według kolumny TerritoryID.
--2. Stwórz odpowiednią funkcję partycjonowania.
--3. Utwórz nową tabelę partycjonowaną, która będzie przechowywać dane z tabeli Sales.SalesOrderHeader.
--4. Przenieś dane z oryginalnej tabeli do nowej tabeli partycjonowanej.

use AdventureWorks2019;
GO

CREATE PARTITION FUNCTION SalesTerritoryID_PF (INT)					--RIGHT -> [x,y)
AS RANGE RIGHT FOR VALUES (2,4,6,8);	--TerritoryID [1-10]		--LEFT  -> (x,y]


CREATE PARTITION SCHEME SalesTerritoryID_PS
AS PARTITION SalesTerritoryID_PF
TO ([PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY]);


CREATE TABLE Sales.SalesOrderHeader_TerritoryID_Partitioned
(
	TerritoryID INT NOT NULL,
	SalesOrderID INT NOT NULL,
	[RevisionNumber] [tinyint] NOT NULL,
	[OrderDate] [datetime] NOT NULL,
	[DueDate] [datetime] NOT NULL,
	[ShipDate] [datetime] NULL,
	[Status] [tinyint] NOT NULL,
	[OnlineOrderFlag] [dbo].[Flag] NOT NULL,
	[SalesOrderNumber]  AS (isnull(N'SO'+CONVERT([nvarchar](23),[SalesOrderID]),N'*** ERROR ***')),
	[PurchaseOrderNumber] [dbo].[OrderNumber] NULL,
	[AccountNumber] [dbo].[AccountNumber] NULL,
	[CustomerID] [int] NOT NULL,
	[SalesPersonID] [int] NULL,
	[BillToAddressID] [int] NOT NULL,
	[ShipToAddressID] [int] NOT NULL,
	[ShipMethodID] [int] NOT NULL,
	[CreditCardID] [int] NULL,
	[CreditCardApprovalCode] [varchar](15) NULL,
	[CurrencyRateID] [int] NULL,
	[SubTotal] [money] NOT NULL,
	[TaxAmt] [money] NOT NULL,
	[Freight] [money] NOT NULL,
	[TotalDue]  AS (isnull(([SubTotal]+[TaxAmt])+[Freight],(0))),
	[Comment] [nvarchar](128) NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
	
	CONSTRAINT PK_SalesOrderHeader_TerritoryID_Partitioned PRIMARY KEY CLUSTERED (SalesOrderID, TerritoryID)
) ON SalesTerritoryID_PS(TerritoryID);

INSERT INTO Sales.SalesOrderHeader_TerritoryID_Partitioned
(TerritoryID, SalesOrderID, OrderDate ,[RevisionNumber], [DueDate], [ShipDate], [Status], [OnlineOrderFlag], [PurchaseOrderNumber], 
[AccountNumber], [CustomerID], [SalesPersonID], [BillToAddressID], [ShipToAddressID], [ShipMethodID], [CreditCardID], 
[CreditCardApprovalCode], [CurrencyRateID], [SubTotal], [TaxAmt], [Freight], [Comment], [rowguid], [ModifiedDate])
SELECT TerritoryID, SalesOrderID, OrderDate ,[RevisionNumber], [DueDate], [ShipDate], [Status], [OnlineOrderFlag], [PurchaseOrderNumber], 
[AccountNumber], [CustomerID], [SalesPersonID], [BillToAddressID], [ShipToAddressID], [ShipMethodID], [CreditCardID], 
[CreditCardApprovalCode], [CurrencyRateID], [SubTotal], [TaxAmt], [Freight], [Comment], [rowguid], [ModifiedDate]
FROM Sales.SalesOrderHeader;





select * from Sales.SalesOrderHeader_TerritoryID_Partitioned 
select TerritoryID, SalesOrderID from Sales.SalesOrderHeader_TerritoryID_Partitioned 


drop table Sales.SalesOrderHeader_TerritoryID_Partitioned
