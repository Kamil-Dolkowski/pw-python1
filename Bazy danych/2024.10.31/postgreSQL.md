## LLM-y: (duży model językowy)

* 4o1 preview
* CoPilot
* MidJourney
* SudoAI
* ViduAI
* Bielik AI
* Plume / Ploom ?

&nbsp; 

&nbsp; 

# PSQL

```psql``` to interaktywny terminal dla PostGreSQL, który umożliwia zarządzanie bazami banych, wykonywanie zapytań SQL oraz administrację serwerem

# Logowanie do bazy

```
psql -U nazwa_użytkownika -d nazwa_bazy -h host -p port
```

-U: nazwa użytkownika PostgreSQL

-d: nazwa bazy

-h: adres hosta (domyślnie localhost)

-p: numer portu (domyślnie 5432)

**Przykład:**

psql -U postgres -d mojabaza

# Komendy

```
\h - help
\? - help
```
\h SELECT

```
\l - lista wszystkich baz

\c - informacja o zalogowanym użytkowniku i bazie

\c nazwa_bazy - przełącza do innej bazy 

\dt - wyświetla listę tabel

\d nazwa_tabeli - wyświetla strukturę tabeli
```

\dt

\d users

# Zarządzanie bazami

Tworzenie nowej bazy
```
CREATE DATABASE nazwa_bazy;
```
Usuwanie bazy:
```
DROP DATABASE nazwa_bazy;
```
Tworzenie nowego użytkownika:
```
CREATE USER nazwa_użytkownika WITH PASSWORD 'hasło';
```
Nadawanie uprawnień:
```
GRANT ALL PRIVILEGES ON DATABASE nazwa_bazy TO nazwa_użytkownika;
```
Włączenie trybu pomiaru czasu:
```
\timing
```
Tryb rozszerzonego wyświetlania:
```
\x
SELECT * FROM emplyees;
```
Ustawianie zmiennych:
```
\set min_salary 50000
SELECT * FROM employees WHERE salary > :min_salary;
```
Wyświetlanie zmiennych:
```
\echo  ????
```
Wykonywanie skryptu z pliku:
```
\i '/ścieżka/do/schema.sql'
```
Przekierowanie wyników do pliku:
```
\o 'ścieżka'
SELECT
\0
```
Kopiowanie danych między tabelą a plikiem:
```
\copy employees TO 'ścieżka' WITH (FORMAT css, HEADER)
```
Zmiana hasła użytkownika:
```
\password
```
Edycja polecenia w edytorze:
```
\e
```
Informacje o połączeniu:
```
\conninfo
\c     (skrót)
```
Ustawienie kodowania znaków:
```
\encoding UTF8
```
Wykonanie bieżącego polecenia:
```
\g
```
Powtarzanie polecenia w interwałach:
```
SELECT count(*) FROM pg_stat_activity;
\watch 10
```
Historia poleceń
```
\s
```


&nbsp; 

Na zajęciach:

```
CREATE DATABASE pw_4_psql

CREATE USER kamil WITH PASSWORD 'kamil';

GRANT ALL PRIVILEGES ON DATABASE pw_4_psql TO kamil;
```

&nbsp; 

# Plik konfiguracji .psqlrc

```
\set PROMPT1 '%n@%/%R%# '
\pset linestyle unicode
\pset border 2
\pset null '[NULL]'
```

**Przykład:**

postgres-# \pset border 2

# Aliasy

```
\alias ll \! ?????

```

# Polecenia (w terminalu)

dropdb mydatabase

createdb newdatabase

dropuser username

createuser username

reindexdb mydatabase

&nbsp;

# Zajęcia

```
\c pw_4_psql

pw_4_psql-# CREATE TABLE klienci (
pw_4_psql(# id SERIAL PRIMARY KEY,
pw_4_psql(# imie VARCHAR(50) NOT NULL,
pw_4_psql(# nazwisko VARCHAR(50) NOT NULL,
pw_4_psql(# email VARCHAR(100) UNIQUE NOT NULL,
pw_4_psql(# data_rejestracji DATE DEFAULT CURRENT_DATE
pw_4_psql(# );

\dt

\d klienci

\du

\dn

\ds

postgres@pw_4_psql=# INSERT INTO klienci (imie, nazwisko, email, data_rejestracji) VALUES
pw_4_psql-# ('Jan', 'Kowalski', 'jak.kowalski@example.com', '2024-10-01'),
pw_4_psql-# ('Marcin', 'Michalski', 'marcin.michalski@example.com', '2024-10-10');

SELECT * FROM klienci;

\timing

SELECT * FROM klienci;


SELECT * FROM klienci_id_seq;

SELECT last_value FROM klienci_id_seq;

SELECT nextval('klienci_id_seq');


\x
SELECT * FROM klienci;


```

&nbsp;

last_value - zawsze to samo (przy dodawaniu w tym samym czasie w to samo miejsce -> błąd)

nextval - zmienia na następną wartość (przy dodawaniu w tym samym czasie w to samo miejsce -> OK)

&nbsp;

wtyczka pgvector



&nbsp;

# Narzędzia w PostgreSQL:

* pg_config

* pg_isready

* vacuumdb

