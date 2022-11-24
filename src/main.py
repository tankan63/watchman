'''
THE WATCHMAN
QUEIRES IPINFO API TO GET IP GEOLOCATION DATA
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def greeting():
    return "Welcome to WatchDog!"


