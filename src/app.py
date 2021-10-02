import uuid
import migrator

from flask import Flask
from flask.json import jsonify

import alembic.config






app = Flask(__name__)

migrator.migrate_up()
migrator.migrate_down()

@app.route("/status")
def status():
    return jsonify({"status": "Ok!"})


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 5000
    app.run(HOST, PORT)
