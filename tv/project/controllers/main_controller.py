from project import app, client_tv
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
    print(f"Receive {json.dumps(request.json, indent=4, sort_keys=True)}")
    if tv.block:
        print("Tv's blocked")
        # TODO show message in screen
        return (
            jsonify(construct_response("status", {"info": "Tv's blocked"}, "smp")),
            200,
        )

    else:
        # TODO show message in screen
        print("Tv's unlocked")
        return (
            jsonify(construct_response("status", {"info": "Tv's unlocked"}, "smp")),
            200,
        )


@app.route("/change", methods=["POST"])
def change():

    command = request.json["lock"]
    client_tv.status = command

    return (
        jsonify(
            construct_response("status", {"info": f"Tv's status is {client_tv.status}"})
        ),
        200,
    )
