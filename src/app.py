import uuid
import migrator

from flask_cors import CORS
from flask import Flask
from flask.json import jsonify

app = Flask(__name__)
CORS(app)

migrator.migrate_up()

board = [None]*9
current_state = {"nextPlayer": "O",
                    "winner": None, "stepNumber": 0, "board": board}
data = {"state": {"current": current_state, "history": [current_state]}}


@app.route("/status")
def status():
    return jsonify({"status": "Ok!"})


@app.route("/game-state")
def get_game_state():
    return jsonify(data)


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 5000
    app.run(HOST, PORT)
