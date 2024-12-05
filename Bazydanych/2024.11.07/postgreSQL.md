# Hierarchia obiektów

Podstawowe typy obiektów:

* bazy danych
* role
* przestrzenie tabel
* ustawienia
* języki szablonowe
* template-y bazy danych ?

# Bazy danych template
Podczas tworzenia nowej bazy jest ona domyślnie klonowana z bazy template o nazwie template1.

Baza template zawiera zestaw tabel, widoków i funkcji, które służą do moedelowania relacji między obiektami definiowanymi przez użytkownika.

Tabele, widoki i .. są częścią pg_config

# Schema

* służą do organizacji obiektów

W Postgres:

* template1
* template0

```\l```

## Template1

* domyślna baza, która jest klonowana
* można ją modyfikować (zmiany globalne dla wszystkich baz)

## Template0

* baza zabezpieczająca lub wersjonowana
* w przypadku uszkodzenia template1 przez użytkownika, template0 może posłużyć do naprawy template1
* przywracanie zrzutu bazy danych
* nie zawiera danych specyficznych do ..?

# Tworzenie bazy na podst szablonu

* przydatne do testowania, refaktoryzacji, planów wdrożeniowych
* przyspieszanie kopii roboczych ??

W klastrze bazy danych można mieć dowolną liczbę baz

Połączenie klienta -> dostęp tylko do danych w 1 bazie

Dane nie są współdzielone między bazami, chyba że użyte są rozszerzenia (foreign data wrapper lub dblink)

Każda baza w klastrze musi mieć właściciela oraz zestaw uprawnień.
```
<user>=<privilages>/granted by
```
# Wyświetlanie listy baz

```
\x
\l
```

# Uprawnienia do baz

* Create (-C) pozwala określonej roli tworzyć nowe schematy w bazie
* Connect (-c) sprawdza uprawnienia roli przy próbie połączenia z bazą
* Temporary (-T) pozwala określonej roli tworzyć tabele tymczaswoe, które są niszczone po zakończeniu sesji

rola PUBLIC -> template1

# Kodowanie znaków

jednobajtowe zestawy znaków () lub wielobajtowe (UTF-8)

# Inne funkcje

* maintenance (atrybut **datfrozenxid** - określa czy baza wymaga procesu odkurzania (vacuum) )
* zarządzanie przestrzenią dyskową (atrybut **dattablespace** - określa przestrzeń tabel dla bazy)
* równoczesność (atrybut **datconnlimit** - określa liczbę dozwolonych połączeń, -1 to brak ograniczeń)
* ochrona (atrybut **datallowconn** - wyłącza możliwość połączenia z bazą, głównie w celu ochrony template0 przed modyfikacjami)

```
\c template0
```

# Tabele katalogowe pg_catalog

* zwykłe tabele (SELECT, UPDATE, DELETE)
* nie zaleca się ręcznego modyfikowania
* przydatne do automatyzacji zadań

### Przykład: Zmiana datconnlimit z 1 na -1.

```
SELECT datconnlimit FROM pg_database WHERE datname='postgres';

ALTER DATABASE postgres CONNECTION LIMIT 1;

SELECT datconnlimit FROM pg_database WHERE datname='postgres';
```

lub

```
UPDATE pg_database SET datconnlimit=-1 WHERE datname='postgres';
```

&nbsp;

&nbsp;

# Role

Role w PostgreSQL należą do klastra serwera, a nie do konkretnej bazy.

Rola może być użytkownikiem bazy lub grupą użytkowników. Koncepcja roli łączy pojęcia użytkowników i grup z poprzednich wersji PostgreSQL.

Dla zachowania kompatybilności z wersją PostgreSQL8.1, nadal wspierane są polecenia CREATE USER i CREATE GROUP.

## Atrybuty ról: (po angielsku)
* create database
* connection limit
* super user
* login
* inherit
* settings
* password (encrypted lub validify)

## Atrybuty ról:
* superużytkownik (może pomijać wszystkie sprawdzenia uprawnień, z wyjątkiem atrybutu logowania)
* logowanie (łączenie z bazą)
* tworzenie bazy 
* inicjowanie replikacji (replikacja strumieniowa)
* hasło
* limit połączeń
* dziedziczenie(inherit) (rola dziedziczy wyższe uprawnienia)

##

```
CREATE ROLE janek WITH LOGIN PASSWORD 'haslo123';
```

CRETE GROUP = CREATE ROLE z opcją NOLOGIN:

```
CREATE ROLE programisci;
```

## Członkowstwo

rola może być członkiem innej roli

SQL GRANT i REVOKE

### Przykład:

```
GRANT programisci TO janek;

REVOKE programisci FROM janek;
```

## Uprawnienia ról

```
CREATE ROLE admin WITH CREATEDB LOGIN PASSWORD 'admin123';

GRANT SELECT, INSERT ON tabela_przykladowa TO janek;

CREATE ROLE superadmin WITH SUPERUSER LOGIN PASSWORD 'superhaslo';

CREATE ROLE limitowany_uzytkownik WITH LOGIN PASSWORD 'haslo' CONNECTION LIMIT 5;
```

&nbsp;

# Tablespace

przestrzeń dyskowa, gdzie dane są przechowywane

zdefiniowana przestrzeń magazynowa, przeznaczona do przechowywania danych

efektywne zarządzanie

## Utrzymanie i zarządzanie miejscem (maintenance):
* przenoszenie danych do innej lokalizacji, unikając problemów związanych z ograniczoną ilością miejsca na dysku

## Optymalizacja:
* przenoszenie danych do szybszych (lub wolniejszych) dysków

### Przykład:
```
CREATE TABLESPACE fast_storage LOCATION '/mnt/ssd_partition/';
```

```
CREATE TABLE moja_tabela (
    id SERIAL PRIMARY KEY,
    nazwa VARCHAR(255) NOT NULL
) TABLESPACE fast_storage;
```

## Podsumowanie:
* łatwe przenoszenie danych między partycjami
* optymalizacja wydajności

&nbsp;

&nbsp;

# Ustawnienia w Postgres

## Zakres działania:
* replikacja (Replication) - konfiguracja replikacji danych pomiędzy serwerami
* dzienniki Write-Ahead Logs (WAL) - zarządzanie logami, które pozwalają na odtwarzanie danych po awarii
* zużycie zasobów (Resource consumption) - kontrola nad zasobami sprzętowymi, takimi jak CPU czy RAM
* planowanie zapytań (Querry planning) - optymalizacja planów wykonywania zapytań -> lepsza wydajność
* logowanie (logging) - ustawnienia dotyczące zapisywania logów

### Szczegółowe ustawienia:

```
SELECT * FROM pg_settings;
```

## Parametry ustawień
* nazwy ustawień niezależne od wielkości

## Boolean
* wartości 0,,treu,false

## Integer
```
SET shared_buffers = '128MB';
```
## Enum
* ERROR lub WARNING

## Floating Point
```
SET cpu_operator_cost = 0.0025;
```
## String
```
SET hba_file = '/var/lib/postgresql/data/...';
```

# Ustawienia kontekstu

## Internal (wewnętrzny)
* nie można zmieniać bezpośrednio
* np. maksymalna długość identyfikatorów - 63

## Postmaster
* zmiana parametrów
* wymagany restart serwera

## SIghup
* niewymaga restartu serwera

## Backend
* niewymaga restartu

## Superuser
* komenda SET
* ustawienia zmieniane w pliku postgresql.conf

## User
* w trakcie działania bieżącej sesji

# Zmiana wartości ustawień
```
SET default_transaction_read_only To on;
SHOW default_transaction_read_only;
```

zmiana wartości w pliku postgres.conf ma efekt globalny

### Przykład

```
SET default_transaction_read_only To on; 

CREATE TABLE test_readonly AS SELECT 1;
-- ERROR:
```
## Przeładowanie konfiguracji

sygnał SIGHUP - bezpieczne

```
SELECT pg_reload_conf(); 
```

## Planowanie zmian

W przypadku pilnych zmian należy odpowiednio zaplanować przestój serwera i poinformować użytkowników.

## Kategorie ustawień ważne dla deweloperów
* domyślne ustawienia połączeń klienckich
* planownaie zapytań

&nbsp;

&nbsp;

&nbsp;

**swagger