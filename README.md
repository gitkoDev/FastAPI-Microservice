# FastAPI Notes Microservice
Python + `FastAPI` asynchronous REST API. Authentication is implemented using JWT. Each user can add and access their own notes ONLY using a valid JSON Web Token

## Tools used


- `Database` &nbsp; **=>**  &nbsp;  Postgres + [asyncpg](https://github.com/MagicStack/asyncpg)
- `Database migrations` &nbsp; **=>**  &nbsp; [Alembic](https://github.com/sqlalchemy/alembic)
- `Data validation` &nbsp; **=>**  &nbsp;  [Pydantic](https://github.com/pydantic/pydantic)
- `ORM` &nbsp; **=>**  &nbsp; [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- `Authentification and middleware` &nbsp; **=>**  &nbsp;  [Python Jose](https://github.com/mpdavis/python-jose)

## Startup

Run `make run` or `docker compose up --build `in root folder to apply all necessary migrations and start the project.

## Endpoints

### *Swagger documentation with request/response body examples available at `http://127.0.0.1:8000/docs` after project startup*
### Authorization
- ```0.0.0.0:8080/auth ``` &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Create new user
- ```0.0.0.0:8080/auth/token``` &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Log in to get access token

### API
- ```0.0.0.0:8080/api/v1``` &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Add note to user
- ```0.0.0.0:8080/api/v1``` &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Get all notes for user
- ```0.0.0.0:8080/api/v1/{note_id}``` &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Get user's note note id
- ```0.0.0.0:8080/api/v1/{note_id}``` &ensp; `=>`  &ensp; **PUT** &ensp;  `=>` &ensp; Update user's note by node id
- ```0.0.0.0:8080/api/v1/{note_id}``` &ensp; `=>`  &ensp; **DELETE** &ensp;  `=>` &ensp; Delete user's note by note id
