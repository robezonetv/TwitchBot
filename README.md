## Prerequisites

Install poetry and run `poetry install` to install dependencies.

## Setup
1. create a `.env` file in the root directory and add the following variables:

```
ACCESS_TOKEN=abcdefg
DJANGO_SECRET_KEY=abcdefg
```

2. run `poetry run python manage.py migrate` to create the database
3. run `poetry run python main.py` to run the bot