# assessment project for AVALON

## Used technologies
Django, DRF, Postgres, Docker, Redis

---
## API endpoints
| Endpoint                                | Description                   |
|-----------------------------------------|-------------------------------|
| http://localhost:8000/api/v1/docs/      | API Documentation             |
| http://localhost:8000/api/v1/token/     | Login/Token Generation        |
| http://localhost:8000/api/v1/positions/ | Position (Role) CRUD endpoint |
| http://localhost:8000/api/v1/employees/ | Employee CRUD endpoint        |

---
## Project setup
- clone this repository and cd into it
- run `docker-compose up -d --build` project will be running on `localhost:8000`
- migrate `docker exec app python manage.py migrate`
- seed dummy data `docker exec app python manage.py loaddata dump.json`
- run tests `docker exec app python manage.py test`

## Steps of scenario mentioned in requirements pdf
- Obtain jwt token with created dummy user.
```
curl --location --request POST 'http://localhost:8000/api/v1/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "admin"
}'
```
- Get employee list under specific position, use `parent_position=POSITION_ID` query parameter.
  - 1: CTO (has 1 employee)
  - 2: Senior SWE (has 3 employees)
  - 3: SWE (has 5 employees)
```
curl --location --request GET 'http://localhost:8000/api/v1/employees/?parent_position=1' \
--header 'Authorization: Bearer JWT-TOKEN'
```
This CURL will return all Senior SWE and SWE (total 8 employees). \
In case of `parent_position=2`, it will return only SWE (total 5 employees).

---
## Scaling
As this project built with Django, It can be scaled vertically and horizontally as per need.

---
## Logging and Monitoring
ELK stack, NewRelic, Sentry or other monitoring tools can be used to monitor the project. if needed. 

---
## Deployment
There are various ways to deploy this project.
from simple (ie: to heroku, by adding some heroku related configurations)
to complex (ie: to distributed cloud servers)

It depends on the level of scale we need.

---
## Frontend
Couldn't develop frontend due to some personal issues and shortage of time.
