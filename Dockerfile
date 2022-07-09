FROM python:3.9.2

ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/emge1/allegro-clone-api.git

WORKDIR /allegro-clone-api

RUN ls .

RUN pip install -r requirements/local.txt

VOLUME /drf_src

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000