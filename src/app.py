from flask import Flask
from flask.json import jsonify

app = Flask(__name__)


@app.route("/status")
def status():
    return jsonify({"status": "Ok!"})


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 5000
    app.run(HOST, PORT)
