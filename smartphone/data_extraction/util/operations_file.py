from zipfile import ZipFile
from data_extraction import app
from werkzeug.utils import secure_filename
from data_extraction.services.converter_to_xml import generate_xml_file
import os


def save_local_file(file):
    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)
    return filename.split(".")[0]


def save_return_file(content, filename, format):
    if format == "csv":
        open(f"{app.config['UPLOAD_FOLDER']}/{filename}_ds.{format}", "w").write(
            content["ds"]
        )
        open(f"{app.config['UPLOAD_FOLDER']}/{filename}_database.{format}", "w").write(
            content["database"]
        )
        zip_files(filename, f"{filename}_ds.{format}", f"{filename}_database.{format}")
        return f"{filename}.zip"
    open(f"{app.config['UPLOAD_FOLDER']}/{filename}.{format}", "w").write(content)
    return f"{filename}.{format}"


def remove_files(func):
    def wrapper():
        result = func()
        files_names = os.listdir(app.config["UPLOAD_FOLDER"])
        [os.remove(f'{app.config["UPLOAD_FOLDER"]}/{name}') for name in files_names]
        return result

    return wrapper


def process_xml_file(func):
    def wrapper(filename):
        generate_xml_file(filename)
        result = func(filename)
        return result

    return wrapper


def zip_files(zipname, *filenames):
    zipObj = ZipFile(f"{app.config['UPLOAD_FOLDER']}/{zipname}.zip", "w")
    for filename in filenames:
        zipObj.write(f"{app.config['UPLOAD_FOLDER']}/{filename}", f"{filename}")
    zipObj.close()