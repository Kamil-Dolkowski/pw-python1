**cirlce ci** - do automatyzowania aplikacji

**redis** - baza danych klucz-wartość

# Docker c.d.

```bash
docker search mysql
docker pull python

docker system df
docker system prune
```

## clean.sh
```bash
#!/bin/bash

echo "clear"

# usunięcie kontenerów starszych niż 7 dni
docker container prune --filter "until=168h" -f

docker image prune -f

docker system df
```

## Zbudowanie kontenera do aplikacji

### Dockerfile
```bash
FROM python:3.11

WORKDIR /app

# Kopiowanie plików
COPY requirements.txt .

# Instalacja zależności
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "app.py"]
```

&nbsp;

```bash
docker build -t docker-test:v1 .
docker run -p 5000:5000 --name docker-test docker-test:v1

docker run -d -p 5000:5000 --name docker-test1 docker-test:v1

curl http://localhost:5000/health

curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" /
-d '{ "title": "Learn Docker" }'

docker history docker-test:v1
```

```bash
docker build -f Dockerfile.copy -t test-copy .
docker build -f Dockerfile.add -t test-add .

docker images


docker build -t docker-test:v5 -f Dockerfile.stage .
```

## CMD vs ENTRYPOINT

### Dockerfile.cmd
```bash
FROM alpine

CMD ["echo", "Hello from CMD Dockerfile"]
```

### Dockerfile.entrypoint
```bash
FROM alpine

ENTRYPOINT ["echo", "Hello from ENTRYPOINT Dockerfile"]
```

### Dockerfile.cmd-entrypoint
```bash
FROM alpine

ENTRYPOINT ["echo"]
CMD ["Hello from CMD Dockerfile"]
```

&nbsp;

```bash
docker build -t test-cmd -f Dockerfile.cmd .
docker run test-cmd:latest
# Hello from CMD Dockerfile
docker run test-cmd:latest echo "Wyświetl"
# Wyświetl

docker build -t test-entrypoint -f Dockerfile.entrypoint .
docker run test-entrypoint:latest
# Hello from ENTRYPOINT Dockerfile
docker run test-entrypoint:latest "Dodatkowy argument"
# Hello from ENTRYPOINT Dockerfile Dodatkowy argument

docker build -t test-cmdentry -f Dockerfile.cmd-entrypoint .
docker run test-cmdentry:latest
# Hello from CMD Dockerfile
docker run test-cmdentry:latest "Custom"
# Custom
```

# Zad 1
- Utwórz obraz z ubuntu 22.04
- Zainstaluj curl
- Ustaw label
- Uruchom bash

Po uruchomieniu użyj polecenia `curl --version`

```bash
FROM ubuntu:22.04

LABEL maintainer="Kamil"
LABEL description="Obraz z Ubuntu 22.04 z curl"

RUN apt-get update && apt-get install -y curl && apt-get clean

#CMD/ENTRYPOINT
CMD ["bash"]
```

```bash
docker build -t ubuntu-custom:1.0.0 .
docker run ubuntu-custom:1.0.0
docker run -it ubuntu-custom:1.0.0
curl --version
docker run ubuntu-custom:1.0.0 curl --version
```

# Zad 2
- Użyj obrazu python:3.11-slim
- Zdefiniuj ARG o nazwie APP_VERSION z wartością domyślną 1.0.0
- Katalog roboczy /app
- Kopiuj plik requirements.txt (Flask==3.0.0, Request==2.31)
- Instaluj zależności z requirements.txt
- Ustaw etykietę z wersją aplikacji zdefiniowaną w ARG

```bash
FROM python:3.11-slim

ARG APP_VERSION=1.0.0

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

LABEL version=${APP_VERSION}
LABEL description="Aplikacja Python w wersji ${APP_VERSION}"

CMD ["python", "-m", "pytest"]
```

```bash
docker build -t z2:1.0.0 .
docker inspect z2:1.0.0

docker build --build-arg APP_VERSION=2.0.0 -t z2:2.0.0 .
docker inspect z2:2.0.0
```

# Zad 3 
- Zmiana użytkownika na ubuntu z root na appuser

```bash
FROM ubuntu:22.04

LABEL maintainer="Kamil"
LABEL description="Obraz z Ubuntu 22.04 z curl"

RUN adduser --disabled-password --gecos '' appuser

RUN apt-get update && apt-get install -y curl && apt-get clean

USER appuser

#CMD/ENTRYPOINT
CMD ["bash"]
```

```bash
docker build -t ubuntu:v3 .

```