from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<path:path>")
def f_static():
    return send_from_directory('static', path)
