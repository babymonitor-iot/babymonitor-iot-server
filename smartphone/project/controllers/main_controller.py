from project import app
from flask import request, render_template, send_from_directory, jsonify, send_file
from project.util.response import construct_response
import json
import requests
import threading

notification = True

@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Smartphone)"

def make_request(data):
    requests.post('http://localhost:5003/smp_receive', json=data)

@app.route("/smp_receive", methods=["POST"])
def receive_bm():
    global notification
    body = request.json


    if body["route"]["from"] == "bm":
        if body["type"] == "notification":
            # Start thread -> count 7 seconds if +-
            # TODO show in screen
            # Forward to TV requests.post('https://localhost:5002', json=body)
            body['route']['from'] = 'smp'
            body['route']['to'] = 'tv'
            threading.Thread(target=make_request, args=(body,)).start()
            return (
                jsonify(
                    construct_response(
                        "confirmation", {"info": "Notification forwarded"}, "bm"
                    )
                ),
                200,
            )

        if body["type"] == "status":
            return (
                jsonify(construct_response("ack", {"info": "OK"}, "bm")),
                200,
            )

    if body["route"]["from"] == "tv":
        
        return (
            jsonify(construct_response("confirmation", {"info": "OK"}, "bm")),
            200,
        )

    return "Error", 400

@app.route("/smp_send", methods=["POST"])
def send_bm():
    body = {
        "type": 'confirmation',
        "msg": '',
        "route": {"from": "smp", "to": "bm"},
    }
    requests.post('http://localhost:5003/smp_send', json=body)