"""Entrypoint for backend website"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    """Returns Home Page"""
    return "<h1>The big6 Project</h1>"
