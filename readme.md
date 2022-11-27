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
[POST] /import - tento endpoint bude příjímat data a parsovat data
[GET] /detail/<nazev modelu>/ - seznam záznamů na základě názvu modelu
[GET] /detail/<nazev modelu>/<id> - všechna data ke konkrétnímu záznamu