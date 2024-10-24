bazy wektorowe -> pod AI

postgreSQL 17 -> AI

biblioteka postgis -> przechowywanie współrzędnych

# Login i hasło

## Terminal Linux

```
sudo -i -u postgres [wejście do postgreSQL]

sudo usermod -aG sudo nazwa_uzytkownika [utworzenie nowego użytkownika bazy danych]

sudo usermod -aG sudo u334531
```

## Terminal PostgreSQL

```
psql [sprawdzenie wersji PostgreSQL ? ]
```

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

**?**

nano postgresql.conf

nano pg_hba.conf

systemctl restart postgresql

&nbsp; 

**Usunięcie PostgreSQL'a:**

sudo systemctl stop postgresql

sudo apt remove --purge postgresql* 

sudo rm -rf var/lib/postgresql/

sudo reboot

&nbsp; 

&nbsp; 

&nbsp; 

# Login i hasło

## Logowanie jako użytkownik postgres

```
sudo -i -u postgres

psql
```

## Ustawianie hasła dla użytkownika postgres

```
\password postgres
```
&nbsp; 

### Reset, włączenie haseł (zmiana sposobu logowania):

```
cd /etc/postgresql/16/main/
sudo nano pg_hba.conf
[zmiana wykonana poniżej]
sudo systemctl restart postgresql
sudo -i -u postgres
```

### Zmiana 2 pierwszych peer na md5 [pg_hba.conf]

```
# Database administrative login by Unix domain socket
local   all             postgres                                md5 <- 

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     md5 <-
```

peer -> md5 / trust

## Nowe hasło ALTER

```
sudo -u postgres psql
```

```
ALTER USER postgres PASSWORD 'nowe_haslo';
```

## Sprawdzenie konfiguracji połączenia

```
psql -h 127.0.0.1 -U postgres -d twoja_baza
```

&nbsp; 

&nbsp; 

&nbsp; 

# Metody uwierzytelniania

pg_hba.conf <- plik konfiguracyjny



## Trust (zaufanie)

Zastosowanie:

* kiedy środowisko jest bezpieczne
* środowisko testowe, hermetyczne

Ryzyko:

* umożliwia dostęp bez uwierzytelniania

## md5 (md5 z hasłem)

Zastosowanie:

* najpopularniejszy
* umiarkowane bezpieczeństwo
* hasło zaszyfrowane

Ryzyko:

* podatne na brute-force i rainbow tables

## Password (hasło w formie jawnej)

Zastosowanie:

* wewnątrz VPN
* kiedy potrzebne jest hasło, ale nie jego szyfrowanie

Ryzyko:

* hasło niezaszyfrowane

## Scram-sha-256

Zastosowanie:

* bezpieczeństwo

Ryzyko:

* wymaga kompatybilnych klientów PostgreSQL

## Ident (mapowanie użytkownika)

Zastosowanie:

* systemy unixowe do automatycznego uwierzytelniania użytkowników
* większe firmy

Ryzyko:

* ograniczone do systemów lokalnych
*gdy mapowanie jest źle skonfigurowane, może stanowić lukę bezpieczeństwa

## Peer (mapowanie użytkownika systemowego, tylko dla lokalnych połączeń)

Zastosowanie:

* tylko lokalne połączenia
* najczęściej zmieniany

Ryzyko:

* 

## Ldap (uwierzytelnienia LDAP)

Zastosowanie:

* w korporacjach

Ryzyko:

* umiejętność skonfigurowania 

ldap + serwer ldap'a

## Radius (uwierzytelnianie RADIUS)

zdalna autentykacja

Zastosowanie:

* w korporacjach, gdzie używa się serwera RADIUS do scentralizowanego uwierzytelniania

Ryzyko:

* wymaga prawidłowej konfiguracji serwera RADIUS i odpowiednich zabezpieczeń dla komunikacji

radius + serwer + sekret 

## Cert (uwierzytelnianie certyfikatami SSL)

Zastosowanie:

* wysoki posiom bezpieczeństwa

Ryzyko:

* 

&nbsp; 

&nbsp; 

&nbsp; 

# Konwencje nazewnictwa

## Nazwy opisowe

* nazwy w liczbie pojedynczej
* nazwa odwzorowywuje obiekt
* nazwy złożone (podkreślnik, nie Camel Case)
* klucz główny sufix "id"
* klucz obcy podobny do klucza referencyjnego
* jednoznaczność nazw
* unikalne nazwy
* nie zaleca się używania słów kluczowych
