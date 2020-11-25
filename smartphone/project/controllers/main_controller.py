from project import app
from flask import request, render_template, send_from_directory, jsonify, send_file
from project.util.response import construct_response
import json
import requests


@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Smartphone)"


@app.route("/sm", methods=["POST"])
def receive_bm():
    body = request.json
    if body['type'] == 'notification':
        #TODO show in screen
        #Forward to TV        requests.post('https://localhost:5002', json=body)
        return jsonify(construct_response('confirmation', {'info': "Notification forward"}, 'bm')), 200

    if body['type'] == 'status':
        return jsonify(construct_response('confirmation', {'info': "OK"}, 'bm')), 200


@app.route("/tv", methods=["POST"])
def receive_tv():
    body = request.json
    if body['type'] == 'notification':
        #TODO show in screen
        #Forward to TV
        msg = construct_response('confirmation', {'info': "Notification confirmed"}, 'tv')
        requests.post('https://localhost:5002', json=msg)
        return jsonify(construct_response('confirmation', {'info': "Notification forward"}, 'bm')), 200

    if body['type'] == 'status':
        return jsonify(construct_response('confirmation', {'info': "OK"}, 'bm')), 200