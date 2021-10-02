import time
import migrator
import json

from flask_cors import CORS
from flask import Flask, request
from flask.json import jsonify
from game_state import get_initial_game_state, generate_state

app = Flask(__name__)
CORS(app)

migrator.migrate_up()


data = get_initial_game_state()



@app.route("/status")
def status():
    return jsonify({"status": "Ok!"})


@app.route("/game-state")
def get_game_state():
    time.sleep(1)
    print(json.dumps(data))
    return jsonify(data)


@app.route("/game-state", methods=['POST'])
def save_game_state():
    time.sleep(1)
    request_data = request.get_json()
    newMove = request_data["move"]
    result, new_data = generate_state(data, newMove)

    return jsonify(result)


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 5000
    app.run(HOST, PORT)
