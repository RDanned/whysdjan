# Project description

## Requirements

- Python 3.10 was used
- Other requirements are in requirements.txt

## Project installation:

- clone project
- python -m venv venv
- pip install -r ./requirements.txt

## Run project (in dev mode)
- python manage.py migrate
- python manage.py runserver

Endpoints:
[POST] /import - import json file
[GET] /detail/<nazev modelu>/ - get all records by model name
[GET] /detail/<nazev modelu>/<id> - get object by model name and object id