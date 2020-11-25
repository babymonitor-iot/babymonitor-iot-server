from data_extraction import app
import os


def generate_xml_file(filename):
    os.system(f"rrdtool dump {app.config['UPLOAD_FOLDER']}/{filename}.rrd > {app.config['UPLOAD_FOLDER']}/{filename}.xml")

