# Docker compose

## Zad 2

### docker_compose.yml
```bash
version: '3.8'

services:
  app:
    build: 
      context: ./app
      # dockerfile: Dockerfile.dev

    ports:
      - "8080:5000"
    depends_on:
      - redis
    volumes:
      - ./app:/usr/src/app

  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"
```

```bash
docker compose up
docker compose up --build
docker compose up -d
```

## Zad 3

```bash
docker compose up
docker compose stop
docker compose rm
```

## Zad 4

```bash
docker exec -it netflix psql -U netflixuser -d netflix
docker cp ./scripts/netflix.sql netflix:/tmp/netflix.sql
docker exec -it netflix psql -U netflixuser -d netflix -f /tmp/netflix.sql

select director, count(1) as ile from netflix_shows WHERE director is not null group by director order by ile desc limit 10;
```