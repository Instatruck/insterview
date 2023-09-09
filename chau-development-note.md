# Note
## Deployment
- Run command `docker-compose up --build -d`

## Seeding data
- Run command `docker exec -it movietest python3 manage.py seed_data`

## Running test
- For Django Test
```
docker exec -it movietest python3 manage.py test
```

- For using BDD-framework to test the BDD scenario.
```
docker exec -it movietest python3 manage.py behave
```

## Python test Goal
Test was carried out by `Python 3.11`

# Task Done
1. Python test Goal
2. Django / Django Rest Framework test goals

