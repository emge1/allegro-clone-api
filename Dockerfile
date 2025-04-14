# --- Builder stage ---
FROM python:3.11.7-slim AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

ARG REQUIREMENTS=requirements/development.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    libffi-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements /app/requirements
RUN pip install --no-cache-dir -r /app/${REQUIREMENTS}

COPY README.md /app/README.md
COPY v1 /app/v1

# --- Runtime stage ---
FROM python:3.11.7-slim

#LABEL maintainer="E <my@email.com>" \
#      version="1.0.0" \
#      description="API with Dockerfile"

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY manage.py /app/manage.py
COPY config /app/config
COPY Dockerfile /app/Dockerfile
COPY media /app/media
COPY docker-compose.yml /app/docker-compose.yml
COPY load_sample_data.sh /app/load_sample_data.sh
COPY sample_data /app/sample_data
COPY entrypoint.sh /app/entrypoint.sh

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app/v1 /app/v1
COPY --from=builder /app/README.md /app/README.md

RUN mkdir -p /app/logs && touch /app/logs/clone.log && chmod -R 755 /app/logs/

RUN chmod +x /app/load_sample_data.sh /app/entrypoint.sh
RUN sed -i 's/\r$//' /app/load_sample_data.sh &&  sed -i 's/\r$//' /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
