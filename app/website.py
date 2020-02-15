from flask import Flask
from flask import render_template
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html")

@app.route("/nba")
def nba_page():
    return render_template(
        "nba.html")

@app.route("/nhl")
def nhl_page():
    return render_template(
        "nhl.html")

@app.route("/nfl")
def nfl_page():
    return render_template(
        "nfl.html")