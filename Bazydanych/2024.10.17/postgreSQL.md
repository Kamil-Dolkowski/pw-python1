## Postgrest - baza danych:

- bezpieczna

- szybka

- wydajna

- praca na wielu instancjach ? (1 baza do zapisu, >2 do odczytu)



-wsparcie dla transakcji ACID

-replikacja i failover

-json w logach

-autovacuum

1996 - zyskał popularność 

## Docker:

- system współdzielony




raid -> do zarządzania dyskami, na płycie głównej

raidy software'owe

odzyskanie danych z raidu


&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

# Instalacja z repozytorium Ubuntu
## install postgres for ubuntu
```sudo apt install postgresql postgresql-contrib```

## status serwera
```sudo systemctl status postgresql```

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

# Instalacja z repozytorium PostgreSQL (wybór konkretnej wersji lub najnowszej)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

# konfiguracja
postgresql.conf     (plik)

## Jak się do niego dostać?:

```
cd /etc/postgresql

cd 16

code .
```

## Odremowane / odhashowane w pliku postgresql.conf:

```
work_mem = 4MB

maintenance_work_mem = 1GB

log_destination = 'stderr'
```
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

```
#logging_collector = off -> by logi były w repozytorium, a nie w systemie

#log_statement = 'none'	

#superuser_reserved_connections = 3 -> oddzielne połączenia dla superusera (admina) [przydatne przy atakach DDOS]

#listen_addresses = 'localhost' -> z jakich adresów można się połączyć do bazy danych -> **warto zmienić !!!**

#wal_level = replica

#max_wal_senders = 10 -> procesy synchronizujące dane między replikami

#synchronous_commit = on

#checkpoint_timeout = 5min

#password_encryption = scram-sha-256
```

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

# Porty:

port = 5432 -> **warto zmienić !!!**

32 000 portów

## Konkretne porty:

- ssh - 22 port

- ftp - 21 port

- sftp - 22 port

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

# VS Code Extensions:

- PostgreSQL


# Azure Data Studio


? sudo chmod +rw pg_hba.conf 

```
sudo -i -u postgres

\du

ALTER USER postgres PASSWORD 'postgres'
```


Database administrative login by Linus domain socket all

IPv4 local conections: all





```
sudo systemctl restart postgresql
```
```
exit
```