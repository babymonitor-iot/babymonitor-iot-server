from project import app
from flask import request, jsonify
import json
import requests

"""
request to send:
{
    "type": 'status'/'notification',
    'msg': {
        'breathing': ,
        'time_no_breathing':,
        'sleeping': ,
        'crying': ,
        },
    'route': {
        'from': ,
        'to': ,
    }
}

request to receive:
{
    "type": "confirmation",
    "msg": {
        "info": "Notificaiton confirmed!"
    }
    "route": {
        "from": ,
        "to": ,
    }
}

"""


@app.route("/check", methods=["GET"])
def check():
    return "I'm working Test"


@app.route("/bm_receive", methods=["POST"])
def bm_receive():
    port, route = filter(request.json["route"]["to"])

    requests.post(
        f"http://localhost:{port}/{route}",
        json=request.json,
    )

    return "OK", 200


@app.route("/smp_receive", methods=["POST"])
def smp_receive():
    port, route = filter(request.json["route"]["to"])
    response = requests.post(
        f"http://localhost:{port}/{route}",
        json=request.json,
    )

    if "tv" in route:
        port, route = filter(response.json()["route"]["to"])
        requests.post(
            f"http://localhost:{port}/{route}",
            json=response.json(),
        )

    return "OK", 200


@app.route("/tv_receive", methods=["POST"])
def tv_receive():
    port, route = filter(request.json["route"]["to"])

    requests.post(
        f"http://localhost:{port}/{route}",
        json=request.json,
    )

    return "OK", 200


def filter(destiny):
    if destiny == "bm":
        return "5000", "bm_receive"
    if destiny == "smp":
        return "5001", "smp_receive"
    if destiny == "tv":
        return "5002", "tv_receive"
