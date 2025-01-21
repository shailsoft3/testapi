from flask import Flask

app =Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "Home Page"

from api.users import user
from api.products import product