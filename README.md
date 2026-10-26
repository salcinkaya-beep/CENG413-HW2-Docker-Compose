# CENG413 HW-2: Two Services with Docker Compose

A Flask application uses Redis to store a persistent visit counter.

## Start

Run these commands inside the project folder:

```bash
docker compose up -d --build
docker compose ps
curl http://localhost:8082/counter
```

Each request to `/counter` increases the value stored in Redis.
