# SWE40006 Task 4 - Docker

Minimal Docker applications created for Deployment Portfolio Task 4.

## Task 4.2 - Credit

Basic Flask web application containerized with Docker and published to Docker Hub.

```bash
docker build -t task4-credit:1.0 src/task4.2-credit
docker run --rm -p 8081:5000 task4-credit:1.0
```

Open <http://localhost:8081>.

### Secondary Docker environment

The Docker Hub image was also pulled and run inside an independent Docker-in-Docker daemon on the same Mac. The daemon is available only through loopback ports.

```bash
docker run -d --privileged --name task4-secondary-docker \
  --restart unless-stopped \
  -e DOCKER_TLS_CERTDIR= \
  -p 127.0.0.1:23750:2375 \
  -p 127.0.0.1:8083:8080 \
  docker:29-dind

docker context create task4-secondary \
  --docker "host=tcp://127.0.0.1:23750"

docker --context task4-secondary pull \
  karthik02kv/swe40006-task4-credit:1.0

docker --context task4-secondary run -d \
  --name task4-credit-secondary \
  -p 8080:5000 \
  karthik02kv/swe40006-task4-credit:1.0
```

The application from the secondary environment is available at <http://127.0.0.1:8083>.

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
