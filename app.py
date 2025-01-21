from flask import Flask

app =Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "Home Page"

import api.users.user
import api.products.product as product