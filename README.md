# taccon

Backend for tic-tac-toe

## Local Setup

- Have python 3.x
- `python -m venv env`
- `source env/Scripts/activate`
- `pip install -r requirements.txt`
- `docker run -d -p 5432:5432 --name tac-db -e POSTGRES_PASSWORD=pass1234 postgres:10.13-alpine`
- `python src/app.py`
