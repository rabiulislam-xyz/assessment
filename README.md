# assessment project for AVALON

## Used technologies
Django, DRF, Postgres, Docker, Redis


## API endpoints
| Endpoint                                | Description                   |
|-----------------------------------------|-------------------------------|
| http://localhost:8000/api/v1/docs/      | API Documentation             |
| http://localhost:8000/api/v1/token/     | Login/Token Generation        |
| http://localhost:8000/api/v1/positions/ | Position (Role) CRUD endpoint |
| http://localhost:8000/api/v1/employees/ | Employee CRUD endpoint        |


## Project setup
- run command `docker-compose up -d --build`
- test command `docker-compose run --rm app python manage.py test`

## Scaling
As this project built with Django, It can be scaled vertically and horizontally as per need.

## Logging and Monitoring
ELK stack, NewRelic, Sentry or other monitoring tools can be used to monitor the project. if needed. 

## Deployment
There are various ways to deploy this project.
from simple (ie: to heroku)
to complex (ie: to distributed cloud servers)

It depends on the level of scalability we need.


## Frontend
Couldn't develop frontend due to some personal issues and shortage of time.
