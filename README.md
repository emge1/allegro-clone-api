# Overview

Allegro-clone is a clone of a popular e-commerce website.

# Project setup

Clone the repository and open it in IDE (recommended: PyCharm):

`git clone https://github.com/emge1/allegro-clone-api.git`

Create virtual environment and activate it in IDE (recommended IDE: PyCharm):

```
python -m venv venv
venv\Scripts\activate.bat
```

Install the required packages:

`pip install -r requirements/local.txt`

and initialize database:

```
python manage.py makemigrations
python manage.py migrate
```

# Authentication

# API documentation

To view API documentation, run development server and visit http://127.0.0.1:8000/docs/