# Triggery (wyzwalacze)

**Trigger** - mechanizm automatyzujący reakcje na zdarzenia w bazie danych

* **zdarzenia:** INSERT, UPDATE, DELETE, TRUNCATE
* **poziomy działania:** FOR EACH ROW lub FOR EACH STATEMENT
* **moment działania:** BEFORE, AFTER, INSTEAD OF

## Składnia
```sql
CREATE TRIGGER trigger_name
{ BEFORE | AFTER | INSTEAD OF } { INSERT | UPDATE, DELETE, TRUNCATE }
ON table_name
[ NOT DEFERRABLE | [ DEFERRABLE INITIALLY IMMEDIATE | INITIALLY DEFERRED ] ]
[...]
[...]
[...]
EXECUTE FUNCTION function_name (arguments);
```

Elementy:
* trigger_name - unikalna nazwa triggera
* BEFORE, AFTER, INSTEAD OF - określa moment działania
* INSERT, UPDATE, DELETE, TRUNCATE
* ...

## Tworzenie triggera

### 1. Tworzenie tabeli

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Dodatkowa tabela do logowania zmian:

```sql
CREATE TABLE users_logs (
    id SERIAL PRIMARY KEY,
    action VARCHAR(10) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    change_time TIMESTAMP 
);
```

### 2. Tworzenie funkcji triggera

```sql
CREATE OR REPLACE FUNCTION log_user_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO users_logs (action, username, email, change_time)
        VALUES ('INSERT', NEW.username, NEW.email, CURRENT_TIMESTAMP);
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO users_logs (action, username, email, change_time)
        VALUES ('UPDATE', NEW.username, NEW.email, CURRENT_TIMESTAMP);
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO users_logs (action, username, email, change_time)
        VALUES ('DELETE', OLD.username, OLD.email, CURRENT_TIMESTAMP);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### 3. Tworzenie triggera

```sql
CREATE TRIGGER user_change_trigger
AFTER INSERT OR UPDATE OR DELETE
ON users
FOR EACH ROW
EXECUTE FUNCTION log_user_changes();
```

## Rodzaje triggerów

Moment wykonania:
* BEFORE (można modyfikować dane)
* AFTER (do logowania i analiz)
* INSTEAD OF (głównie dla widoków)

Zdarzenia:
* ...

Poziom działania:
* ...

## Zaawansowane funkcje triggerów
### 1. Używanie warunku (WHEN)

```sql
CREATE TRIGGER log_email_changes
AFTER UPDATE OF email
ON users
FOR EACH ROW
WHEN (OLD.email IS DISTINCT FROM NEW.email)
EXECUTE FUNCTION log_users_changes();
```

### 2. Obsługa widoków (INSTEAD OF)

```sql
CREATE OR REPLACE VIEW user_view AS
SELECT id, username, email FROM users;

CREATE OR REPLACE FUNCTION handle_view_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO users (username, email) VALUES (NEW.username, NEW.email);
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER instead_of_trigger
INSTEAD OF INSERT
ON user_view
FOR EACH ROW
EXECUTE FUNCTION handle_view_changes();
```

### 3. Obsługa TRUNCATE

```sql
CREATE OR REPLACE FUNCTION log_truncate()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO users_logs (action, change_time)
    VALUES ('TRUNCATE', CURRENT_TIMESTAMP);
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER truncate_trigger
AFTER TRUNCATE
ON users
FOR EACH STATEMENT
EXECUTE FUNCTION log_trauncate();
```

## Zmienne

### NEW
* nowy stan wiersza (INSERT i UPDATE)
* `NEW.column_name`

### OLD
* poprzedni stan wiersza (UPDATE i DELETE)
* `OLD.column_name`

### TG_OP
* zwraca typ operacji wyzwalającej (INSERT, UPDATE, DELETE ,TRUNCATE)

### TG_NAME
* nazwa wyzwalacza

### TG_TABLE_NAME
* nazwa tabeli, do której jest przypisany trigger

### TG_WHEN
* zwraca moment wywołania triggera (BEFORE, AFTER, INSTEAD OF)

### TG_RELID
* zwraca (identyfikator tabeli)?


## Praktyczne przykłady

### 1. Automatyczne aktualizowanie znacznika czasu

### 2. Walidacja danych przed wstawieniem

## Best Practises
* minimalizuj logikę w triggerach
* debuguj i testuj
* unikaj cyklicznych triggerów
* dokumentuj triggery
* rozważ wydajność

## Zad. 1

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```sql
CREATE TABLE products_logs (
    id SERIAL PRIMARY KEY,
    action VARCHAR(10) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC NOT NULL,
    change_time TIMESTAMP
);
```

```sql
CREATE OR REPLACE FUNCTION logs_products()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO products_logs (action, product_name, price, change_time)
        VALUES ('INSERT', NEW.name, NEW.price, CURRENT_TIMESTAMP);
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO products_logs (action, product_name, price, change_time)
        VALUES ('UPDATE', NEW.name, NEW.price, CURRENT_TIMESTAMP);
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO products_logs (action, product_name, price, change_time)
        VALUES ('DELETE', OLD.name, OLD.price, CURRENT_TIMESTAMP);
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

```sql
CREATE OR REPLACE TRIGGER products_trigger
AFTER INSERT OR UPDATE OR DELETE
ON products
FOR EACH ROW
EXECUTE FUNCTION logs_products();
```