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
