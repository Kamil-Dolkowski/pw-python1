# Zad. 1

Utwórz w tabele, widok i procedurę.

Utwórz system do zarządzania projektami, który zawiera:
* tabelę do przechowywania danych o projektach
* tabelę do przechowywania danych o zadaniach w projektach
* widok pokazujący podsumowanie projektów z liczbą zadań w każdym projekcie
* procedurę, która pozwala na dodanie nowego projektu z zadaniami

## Tabela 1

```sql
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Tabela 2

status (np. TODO, IN_PROGRESS, DONE)

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INT NOT NULL REFERENCES projects(id),
    task_name VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL
);
```

## Widok

```sql
CREATE OR REPLACE VIEW project_summary AS
SELECT 
    p.id, 
    p.name, 
    count(t.project_id) AS number_of_tasks, 
    SUM(CASE WHEN t.status = 'DONE' THEN 1 ELSE 0 END) AS done_tasks
FROM projects p
JOIN tasks t ON t.project_id = p.id
GROUP BY p.id
ORDER BY p.id;
```

## Procedura

* przyjmuje (nazwa projektu, lista zadań)
* dodaje projekt i przypisuje do niego zadania

```sql
CREATE OR REPLACE PROCEDURE add_project_with_tasks(project_name VARCHAR(50), task_list VARCHAR(50)[])
LANGUAGE plpgsql AS $$
DECLARE
    project_id INT;
    task_name VARCHAR(50);
BEGIN
    INSERT INTO projects(name) VALUES (project_name) RETURNING id INTO project_id;

    FOREACH task_name IN ARRAY task_list LOOP
        INSERT INTO tasks(project_id, task_name, status) VALUES (project_id, task_name, 'TODO');
    END LOOP;
END;
$$;

CALL add_project_with_tasks('Projekt 1', ARRAY['Zadanie 1', 'Zadanie 2']);
```

## Dane:

```sql
INSERT INTO projects (name) VALUES 
('biblioteka'),
('wypożyczalnia samochodów');

INSERT INTO tasks (project_id, task_name, status) VALUES 
(1,'książki do wypożyczenia','TODO'),
(1,'użytkownicy','IN_PROGRESS'),
(2,'obsługa klientów','IN_PROGRESS'),
(1,'pracownicy','DONE'),
(2,'pracownicy','DONE'),
(1,'nowe książki','DONE');
```


&nbsp;

&nbsp;

&nbsp;

# Zad 2

Zarządzanie magazynem

## Tabela 1

stock - ilość w magazynie

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0),
    price NUMERIC NOT NULL
);
```

## Tabela 2

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(id),
    quantity INT NOT NULL,
    order_date TIMESTAMP NOT NULL
);
```

## Widok

```sql
CREATE OR REPLACE VIEW inventory_status AS
SELECT id, name, stock, stock * price AS total_value
FROM products;
```

## Funkcja

Funkcja, która sprawdza, czy zamówiona ilość produktu jest dostępna w magazynie:

```sql
CREATE OR REPLACE FUNCTION check_availability(product_id INT, quantity INT)
RETURNS BOOLEAN AS $$
DECLARE
    prod_quantity INT;
BEGIN
    SELECT stock FROM products WHERE id = product_id INTO prod_quantity;

    IF quantity <= prod_quantity THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;
```

## Procedura

Procedura, która:
* sprawdza dostępność produktu
* dodaje zamówienie do orders
* aktualizuje ilość stock

```sql
CREATE OR REPLACE PROCEDURE place_order(product_id INT, quantity INT)
LANGUAGE plpgsql AS $$
DECLARE
    available BOOLEAN;
BEGIN
    SELECT * FROM check_availability(product_id, quantity) INTO available;

    -- IF NOT check_availability(product_id, quantity) THEN
    --     RAISE EXCEPTION 'Not enough stock';
    -- END IF;

    IF available = TRUE THEN
        INSERT INTO orders (product_id, quantity, order_date) VALUES 
        (product_id, quantity, CURRENT_TIMESTAMP);

        UPDATE products
        SET stock = stock - quantity
        WHERE id = product_id;

        COMMIT;
    END IF;
END;
$$;
```

### Lepszy sposób (z wyjątkiem, transakcją):

```sql
CREATE OR REPLACE PROCEDURE place_order(product_id INT, quantity INT)
LANGUAGE plpgsql AS $$
BEGIN
    BEGIN
        IF NOT check_availability(product_id, quantity) THEN
            RAISE EXCEPTION 'Not enough stock';
        END IF;

        INSERT INTO orders (product_id, quantity, order_date) VALUES 
        (product_id, quantity, CURRENT_TIMESTAMP);

        UPDATE products
        SET stock = stock - quantity
        WHERE id = product_id;

        COMMIT;
    EXCEPTION WHEN products THEN
        ROLLBACK;
        RAISE;
    END;

END;
$$;
```

## Dane:

```sql
INSERT INTO products(name, stock, price) VALUES 
('chleb', 10, 5.00),
('masło', 20, 10.00),
('napój', 28, 3.50);

INSERT INTO orders(product_id, quantity, order_date) VALUES 
(1, 1, '2025-01-01'),
(1, 2, '2025-01-01'),
(2, 3, '2025-01-01');
```
