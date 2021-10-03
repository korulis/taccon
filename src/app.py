import time
import game_state
import migrator
import json

from flask_cors import CORS
from flask import Flask, request
from flask.json import jsonify
from conf import conf



app = Flask(__name__)
CORS(app)

# migrator.migrate_down()
migrator.migrate_up()
game_state.new_initial_move()

@app.route("/status")
def status():
    return jsonify({"status": "Ok!"})


@app.route("/game-state")
def get_game_state():
    print("Getting game state...")
    time.sleep(conf.delay)
    a_game_state = game_state.get_current_game_state()
    print(json.dumps(a_game_state))

    return jsonify(a_game_state)


@app.route("/move", methods=['POST'])
def save_move():
    print("Saving game state...")
    time.sleep(conf.delay)
    request_data = request.get_json()
    newMove = request_data["move"]
    result = game_state.process_new_move_into_game_state(newMove)

    return jsonify(result)


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 5000
    app.run(HOST, PORT)
