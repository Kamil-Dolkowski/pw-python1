# Tablica accounts

```sql
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    balance NUMERIC(10,2) DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

# Dodawanie danych do tablicy accounts

```sql
INSERT INTO accounts (username, email, balance, is_active, created_at)
VALUES
('john_doe', 'john.doe@example.com', 100.00, TRUE, CURRENT_TIMESTAMP),
('jone_doe', 'jone.doe@example.com', 0, TRUE, CURRENT_TIMESTAMP),
('inactive_user', 'inactive_user@example.com', 50.00, FALSE, CURRENT_TIMESTAMP),
('active_user', 'active_user@example.com', 200.00, TRUE, CURRENT_TIMESTAMP),
('zero_balance', 'zero_balance@example.com', 0, TRUE, CURRENT_TIMESTAMP);
```

&nbsp;

# Utworzenie widoków

## 1. Widok edytowalny 
`WITH CHECK OPTION` - pozwala na edycję danych

```sql
CREATE VIEW editable_accounts AS
SELECT account_id, username, email, balance, is_active
FROM accounts
WHERE is_active = TRUE AND balance > 0
WITH LOCAL CHECK OPTION;
```

## 2. Widok tylko do odczytu

```sql
CREATE VIEW readonly_accounts AS
SELECT DISTINCT account_id, username, email, balance, is_active
FROM accounts
WHERE balance = 0;
```

## 3. Widok zmaterializowany

```sql
CREATE MATERIALIZED VIEW materialized_accounts AS
SELECT account_id, username, email, balance, is_active, created_at
FROM accounts
WHERE is_active = TRUE AND balance > 50
WITH DATA;
```

&nbsp;

# Testowanie widoków

## 1. Widok edytowalny 

```sql
UPDATE editable_accounts
SET balance = balance - 50
WHERE username = 'john_doe';
```
zadziałało poprawnie

```sql
UPDATE editable_accounts
SET balance = 0
WHERE username = 'john_doe';
```
ERROR:  new row violates check option for view "editable_accounts"

DETAIL:  Failing row contains (3, john_doe, john.doe@example.com, 0.00, t, 2024-12-19 08:41:31.023026).

## 2. Widok tylko do odczytu

```sql
UPDATE readonly_accounts
SET balance = 10
WHERE username = 'jone_doe';
```
ERROR:  cannot update view "readonly_accounts"

DETAIL:  Views containing DISTINCT are not automatically updatable.

## 3. Widok zmaterializowany

```sql
SELECT * FROM materialized_accounts;
```

```sql
INSERT INTO accounts (username, email, balance, is_active)
VALUES ('new_user', 'new.user@example.com', 100.00, TRUE);

REFRESH MATERIALIZED VIEW materialized_accounts;
```

#
### Cykliczne odświeżanie widoku zmaterializowanego, wykorzystując harmonogram (np. CRON w systemie operacyjnym lub PostgreSQL `pg_cron`):

