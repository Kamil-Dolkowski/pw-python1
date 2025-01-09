# PL/pgSQL Function

**PL/pgSQL (Procedural Language/PostgreSQL)** to proceduralny język programowania umożliwiający rozszerzenie funkcjonalności PostgreSQL poprzez tworzenie funkcji, procedur i wyzwalaczy (triggerów)

ściśle zintegrowany z PostgreSQL, co pozwala na efektywne zarządzanie bazami

* tworzenie funkcji i procedur z wykorzystaniem logiki proceduralnej 
* definiowanie zmiennych lokalnych
* obsługa wyjątków i błędów
* użycie kontrolnych struktur programowania, takich jak pętle i instrukcje warunkowe

PL/pgSQL jest domyślnie włączony

```sql
CREATE EXTENSION IF NOT EXISTS plpgsql;
```

## Podstawowe elementy funkcji:
* tworzenie funkcji
* określa typ zwracaniej wartości
* blok kodu, w którym jest umieszczona logika funicji
* instrukcja, która określa wartość zwracamą przez funkcję
* określa język, w którym jest napisana funkcja

```sql
CREATE OR REPLACE FUNCTION example_function() RETURNS TEXT AS $$
BEGIN
    RETURN 'Hello';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION example_function() RETURNS TEXT AS $BODY$
BEGIN
    RETURN 'Hello';
END;
$BODY$ LANGUAGE plpgsql;
```

Składnia:
```sql
CREATE OR REPLACE FUNCTION function_name(param_funct param_funct) 
RETURNS TEXT AS $$
???
```
&nbsp;

```sql
CREATE OR REPLACE FUNCTION add_numbers(a INT, b INT)
RETURNS INT AS $$
BEGIN
    RETURN a + b;
END;
$$ LANGUAGE plpgsql;

SELECT add_numbers(10, 20);
```

```sql
CREATE OR REPLACE FUNCTION get_all_users()
RETURNS TABLE(user_id INT, user_name TEXT) AS $$
BEGIN
    RETURN QUERY SELECT id, name FROM users;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_all_users();
```

```sql
CREATE OR REPLACE FUNCTION calculate_tax(price NUMERIC, tax_rate NUMERIC DEFAULT 23)
RETURNS NUMERIC AS $$
BEGIN
    RETURN price * tax_rate / 100;
END;
$$ LANGUAGE plpgsql;

SELECT calculate_tax(100);

SELECT calculate_tax(100,10);
```

## Funkcje z wyjątkami

```sql
CREATE OR REPLACE FUNCTION safe_divide(a NUMERIC, b NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    IF b = 0 THEN
        RETURN NULL;
    ELSE
        RETURN a / b;
    END IF;
END;
$$ LANGUAGE plpgsql;
```

## Best Practise
* dokładnie określaj typ danych parametrów i wartości zwracanej
* obsługuj wyjątki (blok EXCEPTION)
* unikaj ciężkich operacji w funkcjach (unikać długotrwałych pętli)
* testuj funkcje z różnymi zestawami danych wejściowych

## Na co uważać?:
* rekursja (problemy z wydajnością i błędy przekroczenia stosu)
* operacje zmieniające dane (INSERT, UPDATE, DELETE używane ostrożnie)
* nieefektywne zapytania w pętlach

&nbsp;

## Zad. 1

**Funkcja obliczająca powierzchnię prostokąta**

Napisz funkcję o nazwie calculate_rectangle_area, która przyjmuje 2 liczby: długość i szerokość prostokąta, a następnie zwraca jego powierzchnię.

```sql
CREATE OR REPLACE FUNCTION calculate_rectangle_area(length NUMERIC, width NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    RETURN length * width;
END;
$$ LANGUAGE plpgsql;

SELECT calculate_rectangle_area(2,10);
-- Wynik: 20
```

## Funkcja LENGTH

LENGTH(string)

```sql
SELECT LENGTH('PostgreSQL');
-- Wynik: 10

SELECT LENGTH('Hello, World!');
-- Wynik: 13
```

## Funkcja REPLACE

REPLACE(string, from_substring, to_substring)

## Zad. 2

Napisz funkcję count_character_occurrences, która przyjmuje tekst i pojedynczy znak, a następnie zwraca liczbę wystąpień tego znaku w tekście.

Mój sposób: (nie działa)

```sql
CREATE OR REPLACE FUNCTION count_character_occurrences(input_text text, c char)
RETURNS INT AS $$
DECLARE
    length_before INT;
    length_after INT;
BEGIN
    length_before := LENGTH(input_text);

    REPLACE(input_text, c, '');

    length_after := LENGTH(input_text);

    RETURN length_before - length_after;
END;
$$ LANGUAGE plpgsql;

SELECT count_character_occurrences('hello world', 'l');
```

Pana sposób:

```sql
CREATE OR REPLACE FUNCTION count_character_occurrences(input_text text, c char)
RETURNS INT AS $$
BEGIN
    RETURN LENGTH(input_text) - LENGTH(REPLACE(input_text, c, ''));
END;
$$ LANGUAGE plpgsql;

SELECT count_character_occurrences('hello world', 'l');
```

# Języki

* SQL
* PL/pgSQL
* C
* PL/Python
* PL/Perl
* PL/Tcl
* PL/V8
* PL/R


## SQL
* łatwość użycia

## PL/pgSQL [plpgsql]
* bardziej zaawansowane funkcje

## C
* najlepsza wydajność
* niskopoziomowe funkcje

## PL/Python
* idealny do zaawansowanych obliczeń

## PL/Perl
* dobre wsparcie dla mnaipulacji tekstu
* elastyczność i szybkość

## PL/Tcl
* prosty i szybki do nauki

## PL/JavaScript (PL/V8) [plv8]
* użyteczny z JSON-em
* łatwy dla użytkowników JavaScript

## PL/R [plr]
* analityka danych
* pełne możliwości języka R

# pg_language

```sql
SELECT lanname AS language, lanpltrusted AS trusted
FROM pg_language;
```

**lanname** - nazwa języka

**lanpltrusted** - czy może być używany przez zwykłych użytkowników

## Jak zainstalować brakujące języki?:
```
CREATE EXTENSION plpgsql;
```
```
CREATE EXTENSIION plpython3u;
```

* trzeba być superuserem, aby dodać język
* niektóre języki wymagają kompilacji

# Zad. 3

Napisz funkcję longest_word ...

```sql
CREATE OR REPLACE FUNCTION longest_word(sentence TEXT)
RETURNS TEXT AS $$
DECLARE
    words TEXT[] := string_to_array(sentence, ' ');
    longest TEXT := '';
    word TEXT;
BEGIN
    FOREACH word IN ARRAY words LOOP
        IF LENGTH(word) > LENGTH(longest) THEN
            longest := word;
        END IF;
    END LOOP;
    RETURN longest;
END;
$$ LANGUAGE plpgsql;

SELECT longest_word('The quick brown fox jumps over the lazy dog');
-- Wynik: jumps
```

```sql
CREATE OR REPLACE FUNCTION longest_word(sentence TEXT)
RETURNS TEXT AS $$
DECLARE
    words TEXT[] := string_to_array(sentence, ' ');
    longest TEXT := '';
    word TEXT;
BEGIN
    FOREACH word IN ARRAY words LOOP
        IF LENGTH(word) > LENGTH(longest) THEN
            longest := word;
        ELSE IF LENGTH(word) == LENGTH(longest) THEN
            longest := longest || ', ' || word;
        END IF;
    END LOOP;
    RETURN longest;
END;
$$ LANGUAGE plpgsql;
```
^??

## Ciąg Fibonacciego

```sql
CREATE OR REPLACE FUNCTION generate_fibonacci(n INT)
RETURNS TEXT AS $$
DECLARE 
    a INT := 0;
    b INT := 1;
    temp INT;
    result TEXT := '0';
BEGIN
    FOR i IN 2..n LOOP
        temp := a + b;
        a := b;
        b := temp;
        result := result || ', ' || a;
    END LOOP;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

SELECT generate_fibonacci(10);
-- Wynik: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

## Dodanie nowego samochodu do bazy

```sql
CREATE OR REPLACE FUNCTION add_car(new_model VARCHAR, new_price NUMERIC)
RETURNS VOID AS $$
BEGIN
    INSERT INTO cars(model, price) VALUES (new_model, new_price);
END;
$$ LANGUAGE plpgsql;

SELECT add_car('Honda Civic', 25000);
```

## Aktualizacja ceny samochodu

```sql
CREATE OR REPLACE FUNCTION update_car_price(car_id INT, new_pirce NUMERIC)
RETURNS VOID AS $$
BEGIN
    UPDATE cars
    SET price = new_price
    WHERE id = car_id;
END;
$$ LANGUAGE plpgsql;

SELECT update_car_price(1, 27000);
```