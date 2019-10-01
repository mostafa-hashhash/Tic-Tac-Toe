from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
from algorithm import MiniMAx

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home(): 

    if "board" not in session :
        session["board"] = [[None,None,None],[None,None,None],[None,None,None]]
        session["turn"] = "x"

    return render_template("index.html",
            board = session["board"],
            turn = session["turn"] )


@app.route("/play/<int:r>/<int:c>")
def play(r,c):
    return redirect(url_for("home"))
