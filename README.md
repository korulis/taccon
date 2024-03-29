# taccon

Backend webapi for tic-tac-toe game

## Local Setup

- Have python 3.x
- `python -m venv env`
- `source env/Scripts/activate`
- `pip install -r requirements.txt`
- Database: `docker run -d -p 5432:5432 --name tac-db -e POSTGRES_PASSWORD=pass1234 postgres:10.13-alpine`
- If need personal secrets, put into `.env.local` file (create it first).
- Run webapi `python src/app.py`
- Run tests `docker start tac-db` and  `python -m unittest test/GameStateTests.py  -v`

## Database

- If add migration: `alembic revision -m "my migration name"`
- Apply migrations: `alembic upgrade head`
- Unapply migrations: `alembic downgrade base`
- View migrations history: `alembic history --verbose`
