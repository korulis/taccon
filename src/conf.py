import os
from dotenv import load_dotenv


class conf:
    __env_path = os.getcwd() + "/.env"
    __env_path_local = os.getcwd() + "/.env.local"
    load_dotenv(dotenv_path=__env_path, override=True)
    load_dotenv(dotenv_path=__env_path_local, override=True)

    db_connection = os.environ["TACCON_DB_CONNECTION"]
