# Procedury

* zarządzeni transakcjami
* wykonywanie operacji na danych, bez zwracania wyników
* przechowywanie złożonej logiki biznesowej bez potrzeby przenoszenia jej na poziom aplikacji

# Tworzenie procedur

```sql
CREATE OR REPLACE PROCEDURE procedure_name(parameters)
LANGUAGE plpgsql AS $$
BEGIN

END;
$$;
```

## Przykład:

```sql
CREATE OR REPLACE PROCEDURE insert_customer(customer_name TEXT, customer_email TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO customers(name, email) VALUES (customer_name, customer_email);
END;
$$;

CALL insert_customer('x','x');
```

## Transakcje w procedurach

* START TRANSACTION
* COMMIT 
* ROLLBACK

```sql
EXCEPTION WHEN OTHERS THEN
    ROLLBACK;
    RAISE;
```

## Instrukcje kontrolne

* instrukcje warunkowe
* pętle 
* wyjątki

## Wyzwalacze i procedury

procedury w triggerach

## Procedury a funkcje

funkcja - operacje SQL

## Best Practise

* unikać zagnieżdżonych transakcji
* walidacja danych
* obsługa błędów
* optymalizacja zapytań