# Modelowanie danych

reprezentowanie rzeczywistych encji (np. klienci, usługi, produkty)

diagramy ER

atrybuty - owalne

główne ?? - prostokątne

? relacje - romby

# Modele danych

odgrywają kluczową rolę w utrzymaniu spójności danych w systemach współpracujących

źle zdefiniowane mogą prowadzić do zamieszania i niespójności

zła praktyka - definiowanie reguł biznesowych bezpośrednio na podstawie bazy danych, co jest sprzeczne z zasadą "abstrakcji odpowiedzialności"

## Modele danych:
* model danych konceptualny (semantyka domeny)
* model danych logiczny (struktura danych dla określonych technologii)
* model danych fizyczny

# Model encji i relacji (ER)

kluczowy typ modelu danych konceptualnego, zaprojektowanym do uchwycenia i reprezentowania encji i ich relacji

używany zarówno przez deweloperów i użytkowników biznesowych

## Najlepsze praktyki:
* nadmiarowośc danych (nadmiarowe dane mogą powodować niespójność i degradację wydajności)
* saturacja wartości null (używanie złożonych typów danych, jak JSON lub modelowanie wertykalne, np. encja-atrybut-wartość (EAV) )
* ścisłe powiązania (ścisłe powiązanie między encjami może prowadzić do sztywnych struktur, co utrudnia przyszłe zmiany; odpowiednia abstrakcja, modelowanie ogólnień i specjalizacji może zmniejszyć powiąznie ...)

Przykład: portal samochodowy online

# !! Check lista dla każdej kolumny:
* Co jest kluczem głównym?
* Jaka jest domyślna wartość dla każdej kolumny?
* Jaki jest typ każdej kolumny?
* Jakie są ograniczenia dla każdej kolumny lub zestawu kolmumn?
* Czy uprawnienia są poprawnie ustawione na tabele, sekwencje i schematy?
* Czy klucze obce są określone z odpowiednimi akcjami?
* Jaki jest cykl życia danych?
* Jakie operacje są dozwolone na danych?

# Używanie kluczy zastępczych (surrogate keys):
* klucze naturalne mogą się zmieniać (np. adres e-mail) (klucz zastępczy się nie zmienia)
* błędne założenia o kluczach naturalnych (np. adres e-mail, numer telefonu)
* klucze zastępcze mogą wspierać projekt bazy danych tymczasowej
* klucze zastępcze często używają kompaktowych typów danych (np. liczby całkowite), co poprawia wydajność w porównaniu z kluczami naturalnymi

### Wady:
* klucz zastępczy jest generowany automatycznie, co może prowadzić do różnych wyników w różnych bazach testowych
* klucz zastępczy nie jest opisowy (po numerze)

```
\set VERBOSITY 'verbose'
CREATE TABLE user AS SELECT 1;
--ERROR 

CREATE TABLE "user" AS SELECT 1;
--OK
```

# Zadanie

```
CREATE ROLE car_admin WITH LOGIN PASSWORD 'securepass';

CREATE DATABASE db_car OWNER car_admin;

GRANT ALL PRIVILEGES ON DATABASE db_car TO car_admin;
```

```
CREATE TABLE account (
    account_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL CHECK(first_name !~ ' '),
    last_name VARCHAR(100) NOT NULL CHECK(last_name !~ ' '),
    email VARCHAR(50) NOT NULL UNIQUE CHECK(email ~ '^([a-z]|[A-Z]|[0-9]|\.)+@([a-z]|[A-Z]|[0-9])+\.([a-z]|[A-Z]|[0-9]|\.)+$'),
    password VARCHAR(50) NOT NULL CHECK( LENGTH(password) >= 8 )
);
```

```
insert into account(first_name,last_name,email,password) values ('kamil', 'dolkowski', 'kamil.dolk@op.pl', 'haslo123');
```

&nbsp;

### Plik "account.sql":

```
CREATE TABLE account (
    account_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL CHECK( LENGTH(password) >= 8 )
    CHECK (first_name !~ '\s' AND last_name !~ '\s'),
    CHECK (email ~* '^\w+@\w+[.]\w+$'),
    CHECK (char_length(password) >= 8)
);
```

### Logowanie do bazy użytkownikiem 'car_admin':
```
psql -U car_admin -d db_car -h 127.0.0.1
```

**! nadanie uprawnień plikowi i katalogowi**


chmod 777 account.sql
chmod 777 /home/u334531/

#

&nbsp;

```
CREATE TABLE seller_account (
    seller_account_id SERIAL PRIMARY KEY,
    account_id INT UNIQUE NOT NULL REFERENCES account(account_id),
    number_of_advertizement INT DEFAULT 0,
    user_ranking FLOAT,
    total_rank FLOAT
);
```

tak lepiej ^

bardziej elastyczne i mniej dwuznaczne

&nbsp;

```
account_id INT PRIMARY KEY REFERENCES account(account_id) <- tak gorzej
```

tak gorzej ^

# PgAdmin

```
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

sudo apt install pgadmin4

sudo /usr/pgadmin4/bin/setup-web.sh

y
y
```

https://www.pgadmin.org/download/pgadmin-4-apt/

```
#
# Setup the repository
#

# Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

#
# Install pgAdmin
#

# Install for both desktop and web modes:
sudo apt install pgadmin4

# Install for desktop mode only:
sudo apt install pgadmin4-desktop

# Install for web mode only: 
sudo apt install pgadmin4-web 

# Configure the webserver, if you installed pgadmin4-web:
sudo /usr/pgadmin4/bin/setup-web.sh
```