# --- Builder stage ---
FROM python:3.11.7-slim AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements /app/requirements
RUN pip install --no-cache-dir -r /app/requirements/production.txt

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

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app/v1 /app/v1
COPY --from=builder /app/README.md /app/README.md

RUN useradd --create-home --shell /sbin/nologin nonrootuser && chown -R nonrootuser:nonrootuser /app
USER nonrootuser

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]