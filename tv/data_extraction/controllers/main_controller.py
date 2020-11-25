from data_extraction import app
from data_extraction.util.accepted_browsers import check_request_source
from data_extraction.util.validations import validate_request
from data_extraction.services.converter_to_xml import generate_xml_file
from flask import request, render_template, send_from_directory, jsonify, send_file
from data_extraction.util.operations_file import (
    save_local_file,
    remove_files,
    save_return_file,
)
import json
import requests
import xml.etree.ElementTree as ET


@app.route("/check", methods=["GET"])
def check():
    return "I'm working (Data Extraction)"


@app.route("/data_extraction", methods=["POST"])
@remove_files
def data_extraction():
    validate, msg = validate_request(request)
    if not validate:
        return jsonify({"msg": msg}), 400

    filename = save_local_file(request.files["file"])

    # Generating xml file
    generate_xml_file(filename)
    tree = ET.parse(f"{app.config['UPLOAD_FOLDER']}/{filename}.xml")
    root = tree.getroot()
    xml_str = ET.tostring(root, encoding="unicode")

    body = {
        "xml": xml_str,
        "service_type": request.form["service_type"],
        "filename": filename,
        "source": check_request_source(request),
    }

    if request.form["config"] and "config" in request.form:
        body["config"] = json.loads(request.form["config"])
        response = requests.post(
            "http://anonymization:5002",
            json=body,
        )
    else:
        response = requests.post(
            "http://converter:5003",
            json=body,
        )

    if check_request_source(request):
        filename = save_return_file(
            response.json()['data'], body["filename"], body["service_type"]
        )
        return send_from_directory(
            directory=app.config['UPLOAD_FOLDER'],
            filename=filename,
            as_attachment=True
        )
    else:
        return jsonify(response.json()), 200
