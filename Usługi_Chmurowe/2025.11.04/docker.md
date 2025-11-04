comet - przeglądarka

OpenWeb UI - własny model AI

Perplexity - głosowe AI

## Przeglądarki AI
### Wady:
- brak suwerenności, brak własnej decyzji
- modele mogą być nauczone, by promować pewne marki
- sprzedawanie danych dla AI

### Zalety:
- szybkość wyszukiwania
- automatyzacja wyszukiwania

&nbsp;

# Konteneryzacja

## Konteneryzacja VS Maszyny wirtualne (VM)

### VM:
- koszt maszyny
- wszędzie działa
- potrzebna administracja, architektura
- izolacja systemu
- dużo czasu do uruchomienia i konfiguracji

### Konteneryzacja:
- dużo tańsze
- CI/CD
- szybki czas uruchomienia
- elastyczna wymiana/zmiana użycia zasobów
- izolacja kontenerów
- ulotne informacje w kontenerze
- niektóre kontenery (procesor ARM) mogą nie działać na Macu

## Zastosowanie

Nowe serwisy -> konteneryzacja

Stare serwisy -> VM

## 2 podejścia dla baz danych:
- dla baz danych nie stosuje się kontenerów (produkcja - VM)
- dla baz danych można stosować kontenery (dla testów, skalowania, małe projekty)

&nbsp;

# Docker

Windows 10 Home -> WSL

## Instalacja potrzebnych bibliotek + update
```bash
sudo apt update
sudo apt upgrade

sudo apt-get install -y \
ca-certificates \
curl \
gnupg \
lsb-release
```
**^ [możliwe że nie trzeba było tego zrobić] ^**

## Instalacja dockera
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Utworzenie grupy 'docker'
```bash
docker --version
docker info
sudo docker run hello-world

docker ps
sudo docker ps
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

## Utworzenie obrazu ubuntu
```bash 
docker images 
docker container ls
docker run -it ubuntu bash

# W oddzielnym oknie
sudo docker logs 073e36237fee
```

## Pobieranie obrazów
```bash
docker images

docker pull ubuntu:latest
docker pull alpine:latest
```

dockerhub

## Sposoby uruchamiania kontenerów
```bash
# Sposób 1
docker run -it alpine sh
docker run -it --name kontener1 alpine sh

# Sposób 2
sudo docker start kontener2
sudo docker attach kontener2
```

-it -> interakcja (wersja terminalowa)

## Historia kontenera
```bash
sudo docker image history nginx:latest

sudo docker pull nginx:latest
sudo docker image history nginx:latest
```

docker.io/library/ubuntu:22.02

myapp:v1.0.0

# Pobieranie Postgres'a
```bash
# 1
sudo docker run -d --name db-test \
> -e POSTGRES_PASSWORD=secret \
> postgres:15-alpine

sudo docker exec -it db-test psql -U postgres

CREATE TABLE users (id INT, NAME VARCHAR(50));
INSERT INTO users VALUES (1, 'Alicja'), (2, 'Jan');
SELECT * FROM users;
\q

# 2
sudo docker stop db-test
sudo docker rm db-test

sudo docker run -d --name db-test -e POSTGRES_PASSWORD=secret postgres:15-alpine
sudo docker exec -it db-test psql -U postgres

SELECT * FROM users;
# Brak tabeli

# 3 - Utworzenie wolumenu dla dockera
sudo docker volume create postgres-data
sudo docker start db-test
sudo docker exec -it db-test sh

psql -U postgres
SHOW config_file;
\q

cat /var/lib/postgresql/data/postgresql.conf
ls -la /var/lib/postgresql/data/

sudo docker run -d --name db-persistent -e POSTGRES_PASSWORD=secret -v postgres-data:/var/lib/postgresql/data postgres:15-alpine

sudo docker volume ls
sudo docker exec -it db-persistent psql -U postgres

CREATE TABLE users (id INT, NAME VARCHAR(50));
INSERT INTO users VALUES (1, 'Alicja'), (2, 'Krzysztof');
SELECT * FROM users;

sudo docker stop db-persistent
sudo docker rm db-persistent
sudo docker run -d --name db-persistent -e POSTGRES_PASSWORD=secret -v postgres-data:/var/lib/postgresql/data postgres:15-alpine
sudo docker exec -it db-persistent psql -U postgres
SELECT * FROM users;

sudo docker volume inspect postgres-data

sudo docker volume rm postgres-data
sudo docker stop db-persistent
sudo docker rm db-persistent
sudo docker volume rm postgres-data
```

-d -> detach (w tle)

-e -> env ?

## Strona statyczna w dockerze
```bash
# Utworzenie strony (index.html)
mkdir docker-test
echo "<h1>Hello from host</h1>" > docker-test/index.html
cat docker-test/index.html

# Utworzenie kontenera
sudo docker run -d --name web-test -p 8080:80 -v ~/docker-test:/usr/share/nginx/html nginx:alpine
# localhost:8080
echo "<h3>Update from host</h3>" >> index.html
# localhost:8080

sudo docker stop web-test && sudo docker rm web-test
sudo docker stop db-test && sudo docker rm db-test
```