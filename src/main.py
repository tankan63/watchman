'''
THE WATCHMAN
QUEIRES IPINFO API TO GET IP GEOLOCATION DATA
'''



from flask import Flask, request
import coloredlogs
import logging
import json

app = Flask(__name__)

users = {"1-Host": {"ip": "127.0.0.1", \
        "hostname": "localhost", \
        "city": "Boston", \
        "region": "Massachusetts", \
        "country": "US", \
        "loc": "-100, -100", \
        "org": "RCN", \
        "postal": "02xxx", \
        "timezone": "America/New_York"}}

@app.route("/")
def greeting():
    return "Welcome to WatchDog!"

@app.route("/users")
def get_user_list():
    return json.dumps(users)

@app.route("/users", methods=['POST'])
def append_user():
    r = request.get_json()
    print(r)
    return r, 204


