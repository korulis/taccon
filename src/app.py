import os
from flask import Flask
from flask.json import jsonify
from dotenv import load_dotenv

app = Flask(__name__)

class conf:
    __env_path = os.getcwd() + "/.env"
    __env_path_local = os.getcwd() + "/.env.local"
    load_dotenv(dotenv_path=__env_path, override=True)
    load_dotenv(dotenv_path=__env_path_local, override=True)
    some_config = os.environ["POSTGRES_PASSWORD"]


@app.route("/status")
def status():
    print(conf.some_config)
    return jsonify({"status": "Ok!"})


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 5000
    app.run(HOST, PORT)
