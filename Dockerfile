FROM python:3.11.7

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY README.md /app/README.md
COPY Dockerfile /app/Dockerfile
COPY entrypoint.sh /app/entrypoint.sh
COPY media /app/media
COPY requirements /app/requirements
COPY v1 /app/v1
COPY config /app/config
COPY docker-compose.yml /app/docker-compose.yml
COPY load_sample_data.sh /app/load_sample_data.sh
COPY manage.py /app/manage.py
COPY sample_data /app/sample_data

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

RUN mkdir -p /app/logs && touch /app/logs/clone.log
RUN chmod -R 777 /app/logs/

ARG REQUIREMENTS=requirements/development.txt
RUN pip install --no-cache-dir -r /app/${REQUIREMENTS}

RUN chmod +x /app/load_sample_data.sh /app/entrypoint.sh
RUN sed -i 's/\r$//' /app/load_sample_data.sh &&  sed -i 's/\r$//' /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
