from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/<name>")
def home(name):
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
