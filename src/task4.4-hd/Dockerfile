FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    OUTPUT_FILE=/data/history.txt

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && mkdir -p /data && chown appuser:appgroup /data

COPY --chown=appuser:appgroup calculator.py .

USER appuser
VOLUME ["/data"]

ENTRYPOINT ["python", "calculator.py"]
