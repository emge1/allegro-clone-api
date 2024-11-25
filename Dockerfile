FROM python:3.11.7

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings.local

WORKDIR /app

COPY requirements/local.txt /app/requirements/local.txt
COPY requirements/base.txt /app/requirements/base.txt
COPY requirements/production.txt /app/requirements/production.txt
ARG REQUIREMENTS
RUN pip install --no-cache-dir -r /app/${REQUIREMENTS}

COPY . /app

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000