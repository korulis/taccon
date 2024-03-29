import os
from dotenv import load_dotenv


class Config:
    __env_path = os.getcwd() + "/.env"
    __env_path_local = os.getcwd() + "/.env.local"
    load_dotenv(dotenv_path=__env_path, override=True)
    load_dotenv(dotenv_path=__env_path_local, override=True)

    delay = int(os.environ["TACCON_API_TEST_DELAY"])
    db_user = os.environ["TACCON_DB_USER"]
    db_pass = os.environ["TACCON_DB_PASS"]
    db_host = os.environ["TACCON_DB_HOST"]
    db_port = os.environ["TACCON_DB_PORT"]
    db_name = os.environ["TACCON_DB_NAME"]
    db_connection = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
