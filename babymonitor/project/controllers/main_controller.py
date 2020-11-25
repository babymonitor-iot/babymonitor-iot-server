from project import app
from flask import request, jsonify
from project.service.bm_service import BabyMonitorService
from project.util.validations import validate_request
import json
import requests

internal_state = 'normal'

'''
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
'''


@app.route("/check", methods=["GET"])
def check():
    return "I'm working BabyMonitor"


@app.route("/bm_status", methods=["GET"])
def bm_status():
    global internal_state
    return internal_state


@app.route("/bm_send", methods=["GET"])
def bm_send():
    global internal_state

    body = {
        'type': 'notification',
        'msg': {
            'breathing': True,
            'time_no_breathing': 0,
            'sleeping': True,
            'crying': False,
        },
        'route': {
            'from': 'bm',
            'to': 'smp',
        }
    }
    # if request.get('type') == 'notification':
    #     internal_state = 'critical'
    # BabyMonitorService().insert_data(request.json)
    # body = BabyMonitorService().last_record()

    # Send request to smp
    requests.post(
        "http://localhost:5003/bm_receive",
        json=body,
    )

    return 'Message sent', 200


@app.route("/bm_receive", methods=["POST"])
def bm_receive():
    global internal_state
    validate, msg = validate_request(request)

    if not validate:
        return jsonify({"msg": msg}), 400

    internal_state = 'normal'

    return 'OK', 200
