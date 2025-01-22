import json
from flask import Flask,jsonify
from countryinfo import CountryInfo
import socket



app =Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "Home Page"

@app.route("/country/<string:name>")
def get_country_detail(name):
    print(name)
    # Create a CountryInfo object with the provided name
    country = CountryInfo(name)
    
    # Gather country details
    country_details = {
        "Country": name,
        "Capital": country.capital(),
        "Currencies": country.currencies(),
        "Languages": country.languages(),
        "Borders": country.borders(),
        "Provinces": country.provinces(),
        "Area": country.area(),
        "Calling Codes": country.calling_codes(),
        "Capital Latitudes and Longitudes": country.capital_latlng(),
        "TimeZone": country.timezones(),
        "Population": country.population(),
        "Other Names": country.alt_spellings(),
    }

    # Return the details as a JSON response
    return jsonify(country_details)

@app.route("/getip")
def getIp():

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    return f"Your Computer Name is: {hostname}\nYour Computer IP Address is: {IPAddr}"


from api.users import user
from api.products import product