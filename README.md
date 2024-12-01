# Overview

Allegro Clone API is a demo implementation of a popular Polish e-commerce platform, similar to Amazon. This repository serves as the backend for the clone, offering a functional REST API.

Key functionalities include:

* Models for core e-commerce elements like users, products, and orders.
* Serializers and views for handling data and API endpoints.
* Test coverage to ensure reliability.
* Support for both local development and production environments using Docker and docker-compose.


While the backend is under active development, the [frontend](https://github.com/emge1/allegro-clone-frontend) is also in progress and will integrate with this API to simulate the full e-commerce platform experience.


# Table of contents

* [Project setup](#project-setup)
  * [Using Virtual Environment](#using-virtual-environment)
  * [Using Docker Compose](#using-docker-compose)
* [Dependencies](#dependencies)
* [Entity Relationship Diagram](#entity-relationship-diagram)
* [API documentation](#api-documentation)

# Project setup

## Using Virtual Environment

Clone the repository:

```
git clone https://github.com/emge1/allegro-clone-api.git
cd allegro-clone-api
```

Set up a virtual environment:

```
python -m venv venv
venv\Scripts\activate.bat
```

Install dependencies:

```
pip install -r requirements/local.txt 
```

Apply database migrations:

```
python manage.py migrate
```

Start the development server:
```
python manage.py runserver
```

Access the application at http://127.0.0.1:8000/

## Using Docker Compose
Clone the repository:

```
git clone https://github.com/emge1/allegro-clone-api.git
cd allegro-clone-api
```

Build and run the services depending on the environment:

* Local Development
```
docker-compose -f docker-compose.yml up -d web
```

Access the application at http://127.0.0.1:8000/.

# Dependencies
## Backend
* Django
* Django Rest Framework
* Python Decouple
* Pillow
* Django Cors Headers
* Django Debug Toolbar
* Pytest
* Pytest Dajngo
* Pytest Cov
* Pytest JUnitXML
* SQLite (local)
* Postgres (production)

## Frontend
* React
* Axios

# Entity Relationship Diagram 
Below is the Entity Relationship Diagram (ERD) illustrating the relationships between the key entities in the project. Click on the image to view it in a larger size.

![Entity Relationship Diagram](media/entity_diagram.png)

# API documentation

To access the API documentation, start the development server and navigate to:
http://127.0.0.1:8000/docs/

Below is a screenshot of the documentation as seen by a non-authenticated user.
To view a screenshot displaying all possible HTTP methods and endpoints for authenticated users, click [here](media/localhost_8000_docs_.png).
To view API documentation, run development server and visit http://127.0.0.1:8000/docs/

![Swagger docs, non-authenticated](media/docs.png)
