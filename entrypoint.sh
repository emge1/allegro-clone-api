#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate --fake-initial

echo "Running load_sample_data.sh..."
/bin/bash /app/load_sample_data.sh

echo "Starting Django application..."
exec python manage.py runserver 0.0.0.0:8000