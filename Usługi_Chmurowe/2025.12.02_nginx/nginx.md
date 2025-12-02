Książka "Czysty kod. Podręcznik dobrego programisty" 

pylint

pep 8 

# Nginx

## Nginx vs Apache

### Nginx
- asynchroniczny
- tysiące połączeń
- czytelne pliki konfiguracyjne
- do rozdzielania ruchu
- serwowanie plików statycznych

### Apache
- jednowątkowy
- nieczytelne pliki konfiguracyjne

## Uruchomienie, logi i test

```bash
docker run -d -p 80:80 --name moj-nginx nginx:latest

docker logs busy_napier
docker logs busy_napier -f

curl http://localhost
```

## Pliki konfiguracyjne

```bash
docker exec -it moj-nginx /bin/bash

cd /etc/nginx/
cat nginx.conf

cd conf.d
cat default.conf
```

## Logi 

```bash
docker logs --since 15m moj-nginx
docker logs --since 2025-12-02T09:05:00  moj-nginx

docker logs moj-nginx 2>&1 | grep error
```

## sprawdzenie konfiguracji, restart

```bash
# sprawdzenie konfiguracji
nginx -t
docker exec moj-nginx nginx -t

docker exec moj-nginx nginx -s reload
docker restart moj-nginx
```

```bash

```