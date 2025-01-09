### Zadanie: Tworzenie i zarządzanie widokami w PostgreSQL

#### Cel zadania:
Nauczysz się tworzyć różne rodzaje widoków w PostgreSQL:
1. Zwykłe widoki (edytowalne i tylko do odczytu).
2. Widoki z opcją `WITH CHECK OPTION`.
3. Widoki zmaterializowane.

Przećwiczysz ich zastosowanie, w tym dodawanie, modyfikowanie, odświeżanie oraz testowanie ograniczeń.

---

#### Kontekst:
Jesteś administratorem systemu finansowego i musisz przygotować różne widoki raportowe dla tabeli `transactions`, aby umożliwić:
1. Przegląd i aktualizację danych dla transakcji powyżej określonej kwoty.
2. Tylko odczyt danych dla transakcji odrzuconych.
3. Szybki dostęp do raportów z wykorzystaniem widoków zmaterializowanych.

---

#### Tabela `transactions`

Utwórz tabelę, która będzie przechowywać informacje o transakcjach użytkowników:

```sql
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('approved', 'rejected', 'pending')) NOT NULL
);
```

---

#### Krok 1: Wstaw dane testowe

Wprowadź dane do tabeli `transactions`:

```sql
INSERT INTO transactions (user_id, transaction_date, amount, status)
VALUES
(1, CURRENT_TIMESTAMP - INTERVAL '5 days', 500.00, 'approved'),
(2, CURRENT_TIMESTAMP - INTERVAL '4 days', 150.00, 'rejected'),
(3, CURRENT_TIMESTAMP - INTERVAL '3 days', 1000.00, 'approved'),
(4, CURRENT_TIMESTAMP - INTERVAL '2 days', 50.00, 'pending'),
(5, CURRENT_TIMESTAMP - INTERVAL '1 day', 200.00, 'rejected');
```

---

#### Krok 2: Tworzenie widoków

1. **Widok edytowalny z `WITH CHECK OPTION`**  
   Utwórz widok zawierający tylko zatwierdzone transakcje powyżej 100 zł. Widok ten pozwala na dodawanie i aktualizowanie danych, pod warunkiem, że spełniają warunki widoku.

   ```sql
   CREATE VIEW editable_approved_transactions AS
   SELECT transaction_id, user_id, transaction_date, amount, status
   FROM transactions
   WHERE status = 'approved' AND amount > 100
   WITH LOCAL CHECK OPTION;
   ```

2. **Widok tylko do odczytu**  
   Utwórz widok zawierający tylko odrzucone transakcje. Widok ten nie pozwala na modyfikację danych.

   ```sql
   CREATE VIEW readonly_rejected_transactions AS
   SELECT DISTINCT transaction_id, user_id, transaction_date, amount, status
   FROM transactions
   WHERE status = 'rejected';
   ```

3. **Widok zmaterializowany**  
   Utwórz widok zmaterializowany zawierający wszystkie transakcje zatwierdzone w ciągu ostatnich 7 dni. Widok ten przechowuje dane statycznie i wymaga odświeżania.

   ```sql
   CREATE MATERIALIZED VIEW recent_approved_transactions AS
   SELECT transaction_id, user_id, transaction_date, amount, status
   FROM transactions
   WHERE status = 'approved' AND transaction_date >= CURRENT_DATE - INTERVAL '7 days'
   WITH DATA;
   ```

---

#### Krok 3: Testowanie widoków

1. **Testowanie widoku edytowalnego**:
   - Dodaj nową transakcję przez widok:
     ```sql
     INSERT INTO editable_approved_transactions (user_id, transaction_date, amount, status)
     VALUES (6, CURRENT_TIMESTAMP, 200.00, 'approved');
     ```
   - Spróbuj dodać transakcję, która narusza warunki widoku:
     ```sql
     INSERT INTO editable_approved_transactions (user_id, transaction_date, amount, status)
     VALUES (7, CURRENT_TIMESTAMP, 50.00, 'approved');
     -- Powinno zgłosić błąd.
     ```

2. **Testowanie widoku tylko do odczytu**:
   - Wyświetl dane:
     ```sql
     SELECT * FROM readonly_rejected_transactions;
     ```
   - Spróbuj zaktualizować dane w widoku:
     ```sql
     UPDATE readonly_rejected_transactions
     SET amount = 300.00
     WHERE transaction_id = 2;
     -- Powinno zgłosić błąd.
     ```

3. **Testowanie widoku zmaterializowanego**:
   - Wyświetl dane z widoku:
     ```sql
     SELECT * FROM recent_approved_transactions;
     ```
   - Dodaj nową zatwierdzoną transakcję do tabeli `transactions`, a następnie odśwież widok:
     ```sql
     INSERT INTO transactions (user_id, transaction_date, amount, status)
     VALUES (8, CURRENT_TIMESTAMP, 500.00, 'approved');
     ```
   - Wyświetl dane z widoku:
     ```sql
     SELECT * FROM recent_approved_transactions;
     ```
   - Wykonaj refresh danych z widoku:
     ```sql
     REFRESH MATERIALIZED VIEW recent_approved_transactions;
     ```
     
   - Sprawdź, czy nowa transakcja pojawiła się w widoku.