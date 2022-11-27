# Project description

## Requirements

- Python 3.10 was used
- Other requirements are in requirements.txt

## Project installation:

- clone project
- python -m venv venv
- pip install -r ./requirements.txt
- set django secret key in .env file

## Run project (in dev mode)
- python manage.py migrate
- python manage.py runserver

## After project started
- try to make post request to import endpoint with json data

Endpoints:
[POST] /import - import json file
[GET] /detail/<nazev modelu>/ - get all records by model name
[GET] /detail/<nazev modelu>/<id> - get object by model name and object id