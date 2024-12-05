
#-----------------------------------------------------------------------------------------

# Constrains (ograniczenia)

ograniczenia, regułyi warunki narzucane na dane (zapewnienie integralności danych)

kontrolowanie typów danych, wartości, kluczy głównych, obsych

utzrymywanie spójności danych

# Rodzaje ograniczeń:
-ograniczenia unikalności
-ograniczenia klucza głównego
-ograniczenia klucza obcego
-ograniczenia check
-ograniczenia default

# Zastosowania:
-zapewnienie integralności danych
-zapewnienie unikalności
-zapewnienie spójności relacyjnej
-wykonywanie walidacji danych
-automatyzacja działań



ALTER TABLE Sales.Customer
ADD CONSTRAINT UQ_Customer_Email UNIQUE (EmailAddress)



ALTER TABLE Sales.SalesOrderDetail
ADD CONSTRAINT FK_SalesOrderDeatil_ProductID
FOREIGN KEY (xx)
...


ALTER TABLE xx
ADD CONTRAINT xx
CHECK (UnitPrice >= 0 AND UnitPrice <= 1000)



ALTER TABLE Production.Product
ADD CONSTRAINT CHK_Product_NameLength
CHECK (LEN(Name) <= 100);



ALTER TABLE
ADD CONSTRAINT
CHECK (PostalCode LIKE '[0-9]')

#---------------------------------------------

# Defaults

domyślne wartości
automatyzacja procesu wprowadzania danych zapewnienie spójności danych
przy INSERTCIE

# Zastosowania:
-wartości domyślne dal nowych rekordów
-ustawianie domyślnych wartości dla nowych kolumn
-ustawianie domyślnych wartości w zależności od warunków


ALTER TABLE Orders
ADD CONSTRAINT DF_xxxx DEFAULT 'Nowe' FOR Status;

#---------------------------------------------

# Sequence (sekwencje)

obiekty, które generują uniklalne numery lub wartości w określonym zakresie

generowanie kolejnych numerów identyfikacyjnych, numerów zamównień, numerów faktur lub innych unikalnych wartości
są niezależne od tabeli i mogą być współdzielone przez wiele tabel lub obiektów w bazie danych

# Zastosowania:
-generowanie unikalnych numerów identyf
-numerowanie zamówień i faktur
-generowanie numerów klientów i kont



CREATE SEQUENCE OrderNumber
    START WITH 1000
    INCREMENT BY 1;

INSERT INTO Orders (OrderID, OrderDate, CustomerID, )
VALUES (1, '2024-05-06', 100, NEXT VALUE FOR OrderNumber)



# Inne typy sekwencji:
-GUID
-UUID


# GUID:

CREATE TABLE MyTable (
    ID UNIQUEIDENTIFIER DEFAULT NEWID()
)


# UUID:

CREATE SEQUENCE MyUUIDSequence
    AS UUID;


Sekwencje dla innych typów danych
-daty, ciągi znaków

# Możliwości: (GUID, UUID)
-unikalność
-generowanie automatyczne
-uniwersalność
-bezpieczeństwo


# Zalety:
-unikalność
-automatyczne generowanie
-bezpieczeństwo
-uniwersalność

# Wady:
-wielkość
-trudność w odczycie
-złożoność
-kolizje

# Porównywanie wartości identyfikatora GUID:
możliwe operacje dla uniqueidentifier: 
(=,<>,>,<,<=,>=) i sprawdzanie wartości NULL (IS NULL, IS NOT NULL)

#---------------------------------------------

# Partycjonowanie danych

dane podzielone na partycje, którymi można zarządzać i uzyskiwać dostęp do nich oddzielnie
zwiększenie skalowalności, zmniejszenie stopnia rywalizacji o zasoby i optymalizacja wydajności
mechanizm dzielenia danych wg wzorca użycia
np. starsze dane można zarchiwizować w tańszym magazynie danych

# Cele:
-zwiększenie skalowalności
-zwiększenie wydajności 
-poprawa bezpieczeństwa (oddzielenie poufnych i niewrażliwych danych na różne partycje)
-zapewnienie elastyczności działania
-dostosowanie rodzaju magazynu dancych do sposobu użycia danych
-zwiększenie dostępności (w czasie awarii)

# Projektowanie partycji:
-partycjonowanie poziome (fragmentowanie)
-partycjonowanie pionowe (często używane dane)
-partycjonowanie funkcjonalne

# Partycjonowanie poziome:

            A - Z
          /       \
    A - G          H - Z

-wybór klucza fragmentowania (najważniejszy czynnik)
-fragmenty nie muszą być tego samego rozmiaru
-unikaj tworzenia "gorących" partycji (mających wpływ na wydajność)

# Partycjonowanie pionowe:
-zmniejszenie kosztu operacji wejścia/wyjścia i wydajności z wiązanych z pobieraniem często korzystanych elementów

Przykład:
jedna partycja - dane, do których uzyskuje się dostęp częściej (nazwa produktu, opis, cena)
inna partycja - (dane spisu: liczba akcji, data ostatniej kolejności)

podział na częściej i mniej używane wartości

Zalety:
-oddzielenie bardziej dynamicznych danych od wolno poruszających się
-poufne dane w oddzielnej partycji 

# Partycjonowanie funkcyjne:
-poprawa wydajności izolacji i dostępu do danych
-oddzielenie danych odczytu i zapisu od danych tylko do odczytu


# Projektowanie partycji pod kątem skalowalności:
-kluczowe jest zaplanowanie rozmiaru i obciążeń poszczególnych partycji
-przestrzeganie limitów skalowania poszczególnych magazynów partycji

-upewnij się, że każda partycja ma wystarczającą ilość zasobów, by obsłużyć wymagania dotyczące skalowalności
-monitoruj system, cyz dane są ...

# Projektowanie partycji pod kątem wydajności zapytań:
-mniejsze zbiory danych, zapytania równoległe
-nie używanie '*'

# Sprawdź wymagania i ...:
-użyj wymagań biznesowych, by określić krytyczne zapytania, które muszą działać szybko
-monitoruj system, aby znaleźć wszelkie zapytania wykonywane z niską wydfajnością
-znajdź, które zapytania są wykonywane najczęściej


# Podziel na partycje dane powodujące obniżenie wydajności zapytań:
-ogranicz rozmiar poszczególnych partycji tak, aby uzyskać oczekiwany czas odpowiedzi
-zwróć uwagę na lokizację partycji
-rozważ równoległe uruchamianie zapytań między partycjami, aby zwiększyć wydajność

# Projektowanie partycji pod kątem dostępności:
-wyeliminowanie pojedynczego punktu awarii ...



#---------------------------------------------

*
zasada 3,2,1 - 3 backupy, 2 ??, 1 ?? (backupy w różnych miejscach, np. w razie pożaru)


**
#------------- 
30MB - wi-fi
im wyższa częstotliwość, tym mniejsza odległość
13 kanałów wi-fi
6, 7 kanał - największy transfer
#-------------

#---------------------------------------------
