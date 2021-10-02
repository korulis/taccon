# taccon

Backend for tic-tac-toe

## Local Setup

- Have python 3.x and docker
- `python -m venv env`
- `source env/Scripts/activate`
- `pip install -r requirements.txt`
- `docker run -d -p 5432:5432 --name tac-db -e POSTGRES_PASSWORD=pass1234 postgres:10.13-alpine`
- If need personal secrets, put into `.env.local` file (create it first).

- Run webapi `python src/app.py`

## Database

- If add migration: `alembic revision -m "my migration name"`
- Apply migrations: `alembic upgrade head`
- Unapply migrations: `alembic downgrade base`
- View migrations history: `alembic history --verbose`
