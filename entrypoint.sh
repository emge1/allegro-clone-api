#!/bin/bash

set -e

if [ "${WAIT_FOR_DB:=true}" = "true" ]; then
  echo "Waiting for PostgreSQL to be ready..."

  while ! nc -z "$DB_HOST" "5432"; do
    echo "PostgreSQL is not ready. Waiting..."
    sleep 1
  done

  echo "PostgreSQL is ready."

  sleep 10

  python manage.py migrate

  echo "Running load_sample_data.sh..."
  /bin/bash /app/load_sample_data.sh
fi

echo "Starting Django application..."
exec python manage.py runserver 0.0.0.0:8000
