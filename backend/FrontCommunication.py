from flask import Flask


def initServer():
    # initialize server
    app.run("localhost", 5000)

app = Flask(__name__)
@app.route("/")
def hello():

    return "Hello, World!"
