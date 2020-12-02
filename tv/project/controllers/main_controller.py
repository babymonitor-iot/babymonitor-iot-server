from project import app
from project.model.tv_model import TV
from project.util.response import construct_response
from flask import request, render_template, send_from_directory, jsonify, send_file
import json
import requests


tv = TV(False)


@app.route("/check", methods=["GET"])
def check():
    return "I'm working TV"


@app.route("/tv_receive", methods=["POST"])
def receive_sm():
    global tv
    print(f'Receive {json.dumps(request.json, indent=4, sort_keys=True)}')
    if tv.block:
        print("Tv's blocked")
        # TODO show message in screen
        return jsonify(construct_response("status", {"info": "Tv's blocked"}, "smp")), 200

    else:
        # TODO show message in screen
        print("Tv's unlocked")
        return (
            jsonify(construct_response("status", {"info": "Tv's unlocked"}, "smp")),
            200,
        )


@app.route("/change", methods=["POST"])
def change():
    global tv

    command = request.json["block"]
    tv.block = command["block"]
    if tv.block:
        # TODO show message in screen
        return jsonify(construct_response("status", {"info": "Tv's blocked"})), 200
    else:
        # TODO show message in screen
        return jsonify(construct_response("status", {"info": "Tv's unlocked"})), 200
