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
docker start kontener2
docker attach kontener2
```

-it -> interakcja (wersja terminalowa)

## Historia kontenera
```bash
docker image history nginx:latest

docker pull nginx:latest
docker image history nginx:latest
```

docker.io/library/ubuntu:22.02

myapp:v1.0.0

## Pobieranie Postgres'a
```bash
# 1
docker run -d --name db-test \
> -e POSTGRES_PASSWORD=secret \
> postgres:15-alpine

docker exec -it db-test psql -U postgres

CREATE TABLE users (id INT, NAME VARCHAR(50));
INSERT INTO users VALUES (1, 'Alicja'), (2, 'Jan');
SELECT * FROM users;
\q

# 2
docker stop db-test
docker rm db-test

docker run -d --name db-test -e POSTGRES_PASSWORD=secret postgres:15-alpine
docker exec -it db-test psql -U postgres

SELECT * FROM users;
# Brak tabeli

# 3 - Utworzenie wolumenu dla dockera
docker volume create postgres-data
docker start db-test
docker exec -it db-test sh

psql -U postgres
SHOW config_file;
\q

cat /var/lib/postgresql/data/postgresql.conf
ls -la /var/lib/postgresql/data/

sudo docker run -d --name db-persistent -e POSTGRES_PASSWORD=secret -v postgres-data:/var/lib/postgresql/data postgres:15-alpine

docker volume ls
docker exec -it db-persistent psql -U postgres

CREATE TABLE users (id INT, NAME VARCHAR(50));
INSERT INTO users VALUES (1, 'Alicja'), (2, 'Krzysztof');
SELECT * FROM users;

docker stop db-persistent
docker rm db-persistent
docker run -d --name db-persistent -e POSTGRES_PASSWORD=secret -v postgres-data:/var/lib/postgresql/data postgres:15-alpine
docker exec -it db-persistent psql -U postgres
SELECT * FROM users;

docker volume inspect postgres-data

docker volume rm postgres-data
docker stop db-persistent
docker rm db-persistent
docker volume rm postgres-data
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
docker run -d --name web-test -p 8080:80 -v ~/docker-test:/usr/share/nginx/html nginx:alpine
# localhost:8080
echo "<h3>Update from host</h3>" >> index.html
# localhost:8080

docker stop web-test && sudo docker rm web-test
docker stop db-test && sudo docker rm db-test
```

## Podpięcie sieci
```bash
docker network

# Utworzenie sieci
docker network create myapp-network

docker run -d --name database --network myapp-network -e POSTGRES_PASSWORD=secret postgres:15-alpine
docker run -it --rm --network myapp-network alpine sh

ping database
apk add postgresql-client
psql -U postgres -h database
SHOW hba_file;

docker stop database
docker rm database
docker network rm myapp-network
```

### Typy sieci:
- bridge
- host
- none
- overlay (docker swarm, kubernetes)
- ip vlan
- mac ?

&nbsp;

# Przykład - Utworzenie Bloga

```bash
docker network create blognet
docker volume create blog-data

docker run -d --name blog-db --network blognet -v blog-data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=secret123 -e POSTGRES_DB=blogdb -e POSTGRES_USER=blogger postgres:15-alpine

docker run -d --name blog-app --network blognet -p 8080:80 -e WORDPRESS_DB_HOST=blog-db:5432 -e WORDPRESS_DB_USER=blogger -e WORDPRESS_DB_PASSWORD=secret123 -e WORDPRESS_DB_NAME=blogdb wordpress:latest

# (Wordpress nie działa z postgresem)
docker stop blog-db && docker rm blog-db

docker run -d --name blog-db --network blognet -v blog-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blog-db -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:8.0

docker stop blog-app
docker rm blog-app
docker rm blog-db

# Od nowa
docker volume create blog-data
docker run -d --name blog-db --network blognet -v blog-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blog-db -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:8.0

docker rm blog-db
docker run -d --name blog-db --network blognet -v blog-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blog-db -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:latest

# ....
```

**^ źle (na zajęciach)**

```bash
docker network create blognet
docker volume create blog-data

docker run -d --name blog-db --network blognet -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blogdb -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:latest

docker run -d --name blog-app --network blognet -p 8080:80 -e WORDPRESS_DB_HOST=blog-db -e WORDPRESS_DB_USER=blogger -e WORDPRESS_DB_PASSWORD=secret123 -e WORDPRESS_DB_NAME=blogdb wordpress:latest
```

**^ dobrze (ale brak podpięcia do woluminu :/)**

# 

```bash
docker image inspect wordpress:latest

# -P - (jawne?) losowe porty
docker run -d -P nginx:latest

docker run -d -p 8001:80 nginx:latest
curl http://localhost:8001

# Informacje o portach danej aplikacji
docker port blog-app

# Informacje o zmiennych środowiskowych danej aplikacji
docker exec blog-db env

# Łączenie z aplikacją
docker exec -it blog-db mysql -uroot -prootpass

# Plik ze zmiennymi środowiskowymi
nano app.env

APP_ENV=production
APP_DEBUG=false
APP_PORT=3000
DATABASE_HOST=db
DATABASE_PORT=5432

docker run -d --name app-test --env-file app.env alpine sleep 3600
docker exec app-test env | grep APP

# Aplikacja z ograniczoną pamięcią i CPU
docker run -d --name app-limit --memory="512m" --cpus="0.5" nginx:alpine

docker stats app-limit --no-stream

# Logs
docker logs f5c89e3c27c4
docker logs -f f5c89e3c27c4
docker logs --tail 10 app-limit
docker logs -t app-limit
docker top app-limit

docker exec -it app-limit sh
ps aux
netstat -tulpn
ls -la /usr/share/nginx/html/

# Docker cp
docker cp app.env app-limit:/usr/share/nginx/html/

docker ps 
docker ps -a

docker system df 

# Czyszczenie
docker container prune
docker rmi -f nginx:alpine
docker image prune -a
docker volume prune
docker network prune
docker system prune -a --volumes
```