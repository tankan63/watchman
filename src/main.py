'''
THE WATCHMAN
QUEIRES IPINFO API TO GET IP GEOLOCATION DATA
'''



from flask import Flask, request
import logging
import json
import urllib.request


IP_TOKEN = "4af01c2a1a2ade"

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
    # r = request.get_json(force=True)
    # We got the remote address
    r = request.remote_addr
    
    '''
    TM'S Note: trying to query the ipinfo API from localhost will result in a bogon
    '''

    try:
        ip_req = urllib.request.urlopen("https://ipinfo.io/" + r + "?token=" + IP_TOKEN)
        ip_res = ip_req.read()
        ip_data = json.loads(ip_res.decode('utf-8'))
        print(ip_data)
        return ip_data, 204
    except:
        return -100, 404


