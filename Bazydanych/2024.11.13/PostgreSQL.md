# Interakcje na wysokim poziomie z obiektami

&nbsp;

# Główne elementy składowe serwera
* bazy danych
* role 
* przestrzenie tabel (tablespaces) - zarządzanie fizycznym przechowywaniem danych na dysku
* języki programowania - np. PL/pgSQL

# Tworzenie bazy

należy określić **właściciela** i **kodowanie znaków**

jeśli template1 nie odpowiada, to template0, który jest bardziej elastyczny

### Przykład
```
CREATE ROLE car_portal_role LOGIN;
CREATE DATABASE car_portal ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE;  ???
```

# Schematy

każda baza musi zawierać co najmniej 1 schemat

Schemat jest wykorzystywany do organizacji obiektów bazy w sposób podobny do przestrzeni nazw w językach programowania wysokiego poziomu.

public <- podstawowy schemat

nazwy obiektów w różnych schematach mogą się powtarzać bez konfliktów

schemat zawiera wszystkie nazwane obiekty bazy, w tym tabele, widoki, funkcje

#

public <- domyślny schemat

Przydatny w małych firmach, gdzie nie ma potrzeby wprowadzania skomplikowanej kontroli bezpieczeństwa

# Ostrzeżenie
```
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
```
# 
jeśli ustawienie ```search_path``` nie zawiera nazwy schematu:

```
SELECT * FROM pg_catalog.pg_database;
lub
TABLE pg_catalog.pg_database;
```

#

domyślna ścieżka to $user,public

błąd, jeśli nie zostanie odnaleniony:
```
SHOW searhc_path;
-------------
$user,public
```

# Wykorzystanie schematów
* kontrola autoryzacji (grupowanie obiektów na podstawie ról)
* organizacja obiektów bazy (obiekty bazy można organizować w grupy na podstawie logiki biznesowej)
* utrzymanie zewnętrznego kodu SQL (rozszerzenia dostępne w pakietach kontrybucji, mogą być używanie z wieloma aplikacjami)

### Przykład:

```
CREATE SCHEMA car_portal_app AUTHORIZATION car_portal_app;
-- Właścicielem schematu jest rola o tej samej nazwie, jeśli nie podano innej
CREATE SCHEMA AUTHORIZATION car_portal_app;
```

https://www.postgresql.org/docs/current/sql-createschema.html

CREATE SCHEMA IF NOT EXISTS - w automatyzacji

# Tabele

klonowanie tabel (przy refaktoryzacji, utworzenie skryptu deinstalacyjnego do wycofania zmian)

materializacja wyników zapytanie SELECT (zwiększenie wydajności lub tymczasowego przechowywanie danych do późniejszego użycia)

### Rodzaje tabel:

* **tabela trwała:** cykl życia tabeli trwa od momentu jej utworzenia do momentu jej usunięcia
* **tabela tymczasowa:** cykl życia tabeli to sesja użytkownika, często używane w językach proceduralnych do logiki biznesowej

* **tabela bez logowania (unlogged):** szybsze operacje niż tablice trwałe, dane nie są zapisywane do plików WAL (Write-Ahead-Log), odporne na awarie, nie mogą być replikowane na węzeł podrzędny, ponieważ replikacja strumieniowa opiera się na przesyłaniu plików dziennika
* **tabela podrzędna:** dziedziczy 1 lub więcej tabel, dziedziczenie często używane z wykluczaniem ograniczeń (constraint exclusion) w celu fizycznego partycjonowania danych na dysku twardym, co pozwala zwiększyć wydajność w przypadku pobierania podzbioru danych o określonej wartości

### CREATE TABLE:
* nazwa tabeli
* typ tabeli
* parametry przechowywania tabeli
* kolumny tabeli
* nazwa tabeli klonowanej oraz opcje klonowania

&nbsp;

Podczas projektowania, należy starannie dobrać odpowiedni typ danych.

Zmiana typu danych kolumny po wdrożeniu bazy do produkcji może być bardzo kosztowna, zwłaszcza dla tabel o dużym obciążeniu.

Koszt ten wynika z blokowania tabeli, a w niektórych przypadkach również z konieczności jej przypisania.

# Typy danych

### Wybierając typ danych, należy uwzględnić:
* rozszerzalność
* rozmiar typu danych

### Kategorie natywne typów danych:
* typy numeryczne
* typy znakowe
* typy daty i czasu

## Typy danych numerycznych:
|typ|rozmiar|info|
|:-:|-------|----|
| smallint          |(2 bajty) |(odpowiednik SQL: int2) |
| int               |(4 bajty) |(odpowiednik SQL: int4) |
| bigint            |(8 bajty) |(odpowiednik SQL: int8) |
| numeric/decimal   |(zmienny) | |
| real              |(4 bajty) |(wartości specjalne: Infinity, -Infinity, NaN) |
| double            |(8 bajty) | |
| precision         |(8 bajty) | |


------------------------------------

&nbsp;

smallint -> oszczędność miejsca na dysku

bigint -> ??

serial (smallserial, serial, bigserial) to opakowania dla smallint, int, bigint

serial jako klucze zastępcze

```
CREATE TABLE customer (
    customer_id SERIAL
);
```

```
CREATE SEQUENCE customer_customer_id_seq;
CREATE TABLE customer (
    customer_id integer NOT NULL DEFAULT nextval('customer_customer_id_seq')
);
ALTER SEQUENCE customer_customer_id_seq OWNED BY customer.customer_id;
```

**!!!!! odpowiednik sequence w MSSQL - na zaliczeniu !?**

### Serial:
* kolumna ma ograniczenie NOT NULL
* kolumna ma domyślną wartość nextval
* sekwencja zostanie usunięta, jeśli kolumna zostanie usunięta

```
SELECT CAST (5.9 AS INT) AS rounded_up, CAST(5.1 AS INTEGER) AS rounded_down, 5.5::INT AS another_syntax;
```

## Numeric i decimal

numeric i decimal -> wartości pieniężne

### 3 formy definiowania wartości typu numeric i decimal:
* numeric(precision,scale)
* numeric(precision)
* numeric

jeśli precyzja nie jest wymagana, nie należy używać typów numeric i decimal

operacje na tych typach są wolniejsze niż na typach float i double precision

## Typy znakowe
|typ|opis|maksymalna długość|
|:-----:|-----|------|
| "char"        |(odpowiednik char(1), wymaga cudzysłowu)                                                                   |1              |
| name          |(odpowiednik varchar(64), używany pzrze PostgreSQL do nazw obiektów)                                       |64             |
| char(n)       |(alias: character(n), stała długość znaków, wewnętrznie nazywany ```bpchar``` (blank padded character) )   |1 do 10485760  |
| varchar(n)    |(alias: character varying(n), zmienna długośc znaków,gdzie maksymalna długość to n)                        |1 do 10485760  |
| text          |(zmienna długość znaków)                                                                                   |nieograniczona |

&nbsp;

### Typy tekstowe:
* char(n) - spacje na końcu
* varchar(n) - brak spacji na końcu

```
SELECT 'a'::CHAR(2) = 'a '::CHAR(2);

SELECT length('a '::CHAR(10));
```

char(2) -> 'a' = 'a '

Jeśli ciąg zanków jest dłuższy niż maksymalna długość:
* insert lub update -> błąd
* casting -> znaki obcięte, bez zgłoszenia błędu

```
SELECT 'a '::VARCHAR(2) ='a '::text;

SELECT 'a '::CHAR(2) ='a '::text;

SELECT 'a '::CHAR(2) ='a '::VARCHAR(2);

SELECT length('a '::CHAR(2));
--1

SELECT length('a '::VARCHAR(2));
--2
```
maksymalny rozmiar tekstu -> 1 GB (maksymalny rozmiar kolumny)

dla ciągów o stałej długości chcracter i character varying -> ta sama ilość miejsca na dysku

```
CREATE TABLE emulate_varchar (
    text VARCHAR() --??
)
```

nie ma różnicy w wydajności między różnymi typami znakowymi

? zaleca się używanie typu text

## Typy daty i czasu:
```
* timestamp
* without time
* zone

* timestamp with
* time zone

* date

* time without
* time zone

* time with time
* zone

* interval
* [fields]
```

format UTC

### Praktyki:
* używanie timestamp without time zone i pozostawienie obsługi różnic po stronie klienta
* użycie timestamp with time zone

### datastyle ma 2 cele:
* określenie formatu
* interpretacja danych

SET timezone TO 'Asia/jerusalem';


SHOW timezone;SELECT now(), now() ... ADD TIME ZONE 'UTC' ??

Typ date jest zalecany, gdy nie ma potzreby określania czasu, np. data urodzenia.

12 bajtów (8 bajtów przechowuje czas i 4 bajty przechowuje strefę czasową)

Interval 
