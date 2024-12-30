#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate

sleep 5

echo "Database synchronization"
sqlite3 /app/config/db.sqlite3 ".tables"

echo "Running load_sample_data.sh..."
/bin/bash /app/load_sample_data.sh

echo "Starting Django application..."
exec python manage.py runserver 0.0.0.0:8000