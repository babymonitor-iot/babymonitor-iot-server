from project import app
from flask import request, render_template, send_from_directory, jsonify, send_file
from project.util.response import construct_response
from project.model.tv_model import TV
import json
import requests


tv = TV(False)


@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Smartphone)"


@app.route("/sm", methods=["POST"])
def receive_sm():
    global tv
    if tv.block:
        #TODO show message in screen
        return jsonify(construct_response('status', {'info': "Tv's block"}, 'sm')), 200

    else:
        #TODO show message in screen
        return jsonify(construct_response('status', {'info': "Tv's unlocked"}, 'sm')), 200


@app.route("/change", methods=["POST"])
def change():
    global tv
    msg = requests.json()['msg']
    tv.block = msg['command']
    if tv.block:
        #TODO show message in screen
        return jsonify(construct_response('status', {'info': "Tv's block"})), 200
    else:
        #TODO show message in screen
        return jsonify(construct_response('status', {'info': "Tv's unlocked"})), 200