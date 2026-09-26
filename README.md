# SWE40006 Task 4 - Docker

Minimal Docker applications created for Deployment Portfolio Task 4.

## Task 4.2 - Credit

Basic Flask web application containerized with Docker and published to Docker Hub.

```bash
docker build -t task4-credit:1.0 src/task4.2-credit
docker run --rm -p 8081:5000 task4-credit:1.0
```

Open <http://localhost:8081>.

## Task 4.3 - Distinction

Minimal Flask status application using environment variables, Gunicorn, a non-root user, a health check, and an exposed network port.

```bash
docker build -t task4-distinction:1.0 src/task4.3-distinction
docker run --rm -p 8082:10000 \
  -e APP_ENV=Production \
  -e "APP_MESSAGE=Application is running successfully" \
  task4-distinction:1.0
```

Open <http://localhost:8082> and use `/health` for the health endpoint.

Live deployment: <https://swe40006-task4-distinction.onrender.com>

## Task 4.4 - High Distinction

Non-web addition and subtraction calculator. Results are persisted through a host-mounted `/data` directory.

```bash
mkdir -p calculator-data
docker build -t task4-calculator:1.0 src/task4.4-hd
docker run --name task4-calculator \
  -v "$(pwd)/calculator-data:/data" \
  task4-calculator:1.0 add 10 4
```

The result is printed in the container logs and appended to `calculator-data/history.txt`.
