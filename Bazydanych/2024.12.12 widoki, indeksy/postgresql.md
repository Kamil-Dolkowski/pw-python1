# Widoki

widok - nazwana kwerenda lub osłona wokół instrukcji SELECT

* jedne z podstawowych elementów relac. baz danych, które można porównywać do metdo w klasach UML
* upraszczają zapytania i zwiększają modularnośc kodu

### Zalety:
* uproszczenie złożonych zapytać i poprawa modularności kodu
* poprawa wydajności dzięki buforowaniu wyników widoków
* redukcja ilości kodu SQL
* integracja z językami obiektowymi dzięki widokom zaktualizowanym
* zastosowanie mechanizmów autoryzacji na poziomie wiersza
* implementacja warswty abstrakcji między bazą a aplikacjami
* łatwe wprowadzenie zmian bez konieczności wdrażania nowego oprogramowania

### Widoki różnią się od procedur składowanych
* widoki są bardziej wydajne
* optymalizacja widoków

modyfikacja widoku może być zabroniona z powodu ...

CREATE - tworzy nowy widok

OR REPLACE - zastępuje istniejący widok

TEMP lub TEMPORARY - tworzy widok tymczasowy

AS -definiuje zapytanie, które stanowi ...


```
CREATE VIEW account_information AS
SELECT
    account_id,
    first_name,
    last_name,
    email
FROM 
    account;
```

Utwórz tabelę

```
CREATE TABLE customers (
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    adres TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```
CREATE VIEW account_information (account_id, first_name, last_name, email) AS
SELECT
    account_id,
    first_name,
    last_name,
    email
FROM
    account;
```

## Tymczasowe widoki

```
CREATE TEMP VIEW temp_user_view AS
SELECT
    id,
    username,
    email
FROM
    account
WHERE 
    active = true;
```

## Widoki rekurencyjne
* obsługują rekurencję
* przydatne do pracy z hierarchicznymi danymi

```
CREATE RECURSIVE VIEW employee_hierarchy (employee_id, employee_name, manager_id) 
(
    -- Poziom bazowy: pracownicy bez przełożonych
    SELECT 
        id AS employee_id,
        name AS employee_name,
        manager_id,
        1 AS level
    FROM 
        employees
    WHERE
        manager_id IS NULL

        UNION ALL

    -- Poziom rekurencyjny: pracownicy podlegli przełożonym
    SELECT 
        e.id AS employee_id,
        e.name AS employee_name,
        e.manager_id,
        eh.level + 1
    FROM 
        employees e
    JOIN
        employee_hierarchy eh
    ON
        e.manager_id = eh.employee_id
);

-- Wyświetlenie hierarchii pracowników
SELECT * FROM employee_hierarchy ORDER BY level, employee_name;
```

## Widoki materializowane
* przechowują dane fizyczne w tabelach i mogą być okresowo odświeżane
* używane w przypadku dużych i  ??

```
CREATE MATERIALIZED VIEW nazwa_widoku
...
...

REFRESH MATERIALIZED VIEW nazwa_widoku;
```

```
CREATE MATERIALIZED VIEW account_search_history AS
SELECT
    regexp_split_to_table(search_key, '&') AS key,
    count(*) AS count
FROM 
...

```

### Usuwanie widoku z zależnościami:
```
DROP VIEW nazwa_widoku_zależnego;
DROP VIEW nazwa_widoku_pierwotnego;
lub ?
DROP VIEW nazwa_widoku CASCADE;
```

## Aktualizowane widoki
Warunki:
* widok musi być oparty na tabeli lub innym aktual widoku
* w definicji widoku nie mogą występować klauzule (DISTINCT, WITH, GROUP BY)
* lista kolumn widoku musi być bezpośrednio wzorowana na kolumnach tabeli ?
* ??

### Sprawdzanie, czy widok jest aktualizowany:
```-
SELECT table_name, is_insertable_into
FROM information_schema.tables
WHERE table_name = 'user_account';
```

# Indeksy
* obiekty fizyczne, które przyspieszają dostęp do danych
* optymalizacja wydajności zapytań
* weryfikacja ograniczeń, takich jak UNIQUE

## Indeks unikalny
```
CREATE UNIQUE INDEX account_history_idx ON account_history (account_id. search_key, search_date);
```

```
SELECT search_key
FROM account_history
WHERE account_id = 1000
GROUP BY search_key
ORDER BY MAX(search_date) LIMIT 10;
```

### Plan wykonania (query plan):
```
EXPLAIN SELECT search_key
...
```
# Typy indeksów:
## B-tree (domyślny tryb indeksu) (drzewo zrównoważone)
* operacje porównawcze
```
CREATE INDEX btree_index ON table_name(column_name);
```
## Hash index
* przeznaczone do obsługi równości (=)
* nie są transakcyjnie bezpieczne i nie są replikowane w węzłach slave podczas replikacji
* operacje równości (choć B-tree zwykle spełnia te same potrzeby)
```
CREATE INDEX hash_index ON table_name USING HASH (column_name);
```
## GIN (Generalized Inverted Index)
* gdy wiele wartości musi być mapowanych na jeden wiersz
* tablice, wyszukiwanie pełnotekstowe
```
CREATE INDEX gin_index ON table_name USING GIN (column_name);
```
## GiST (Generalized Search Tree)
* budowanie ogólnych zrównoważ struktur drzewiastych
* typy geometryczne, wyszukiwanie pełnotekstowe
```
CREATE INDEX gist_index ON table_name USING GiST (column_name);
```
## BRIN (Block Range Index)
* w przypadku bardzo dużych tabel, gdzie dane są uporządkowane, mniej miejsca niż B-tree, ale jest wolniejszy
* przechowywanie danych na dużą skalę
* dane liczone w terabajtach
```
CREATE INDEX brin_index ON tyable_name USING BRIN (column_name);
```
## Indeksy częściowe
* tylko podzbiór danych w tabeli, które spełniają określone warunki (WHERE)
* zmniejsza rozmiar ??
```
ALTER TABLE advertisement ADD COLUMN advertisement_deletion_date TIMESTAMP WITH TIME ZONE;

CREATE INDEX partial_index ON advertisement(advertisement_id) WHERE advertisement_deletion_date IS NOT NULL;
```
Taki index pozwala szybko wyszukiwać "martwe" reklamy bez konieczności indeksowania całej tabeli.

## Indeksy na wyrażeniach
* tworzone na wynikach wyrażeń i funkcji
```
INSERT INTO account VALUES (DEFAULT, 'foo');

SELECT * FROM account WHERE lower(first_name) = 'foo';
```

```
CREATE INDEX lower_first_name_idx ON account (lower(first_name));

SELECT * FROM account WHERE lower(first_name) = 'foo';
```

### Konwersja typów danych:

indeks może być użyty do porównania pól zapisanych w różnych formatach, np. porównianie dat w formacie wimestamp do date


```
CREATE INDEX birth_date_idx ON person_table (CAST(birth_timestamp AS date));
SELECT * FROM person_table WHERE CAST(birth_timestamp AS date) = '2000-01-01';
```

### Podsumowanie:
* B-tree: domyślny i najbardziej uniwersalny
* GIN, GiST: do danych struktualnych, jak tablice czy wyszukiwanie pełnotekstowe
* BRIN: do bardzo dużych tabel

indeksy częściowe pozwalają na zmniejszenie rozmiaru indeksu, co poprawia wydajność

indeksy na wyrażeniach umożliwiają optymalizację zapytań korzystających z funkcji








***
supabase
postgrest - API do postgreSQL
Thunder Client - API w Visual Studio