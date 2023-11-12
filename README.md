## Requirements
- Python 3.10.7
- Django 4.2.7
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python3 -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Start and Use
Run migration
```
python manage.py makemigrations
python manage.py migrate
```
Run server.
```
python manage.py runserver
```

## Run unitest

`python manage.py test`

## Load seed data

`python manage.py loaddata fixtures/data.json`

## Run docker

`docker compose up`
