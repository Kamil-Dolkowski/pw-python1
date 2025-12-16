reverse proxy, nagłówki, certyfikat ssl

## Reverse proxy
- serwowanie wielu aplikacji na jednym adresie ip
- aplikacje na wielu portach

### Cechy:
- bezpieczeństwo
- load balancer - rozprapagowanie ruchu na wiele serwisów
- można podpiąć ssl
- można cache'ować, np. pliki statyczne
- kompresja
- centralizacja punktów - kilka serwisów za nginx'em

```bash
docker build -t backend-app:1.0 .
docker run -d --name backend --network app-network backend-app:1.0

docker network ls
docker network create app-network
docker run -d --name backend --network app-network backend-app:1.0

docker run -d --name nginx-proxy --network app-network -p 8080:80 -v $(pwd)/../nginx/nginx.conf:/etc/nginx/nginx.conf:ro nginx:latest

docker exec -it nginx-proxy sh
curl http://backend:3000
# {"headers":{"host":"backend:3000"},"hostname":"d96d96e7fcd7","message":"Hello from backend","timestamp":"2025-12-16T09:40:03.148858"}
curl http://localhost:80
# {"headers":{"host":"localhost"},"hostname":"d96d96e7fcd7","message":"Hello from backend","timestamp":"2025-12-16T09:39:47.201020"}
```

# Zad 2
```bash
docker build -t zad2-admin ./admin/
docker build -t zad2-backend ./backend/

docker network create app-network
docker run -d --name admin --network app-network zad2-admin
docker run -d --name backend --network app-network zad2-backend

docker run -d --name zad2-nginx --network app-network -p 8080:80 -v ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro nginx:latest
```

# Gitlab

group: pw-2025

project: pw-cicd

# CI/CD

variables

pipeline

secure files

protected branch 

protected tag