from flask import Flask
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = f'{os.path.abspath(os.getcwd())}/data_extraction/tmp'

from .controllers import (
    main_controller
)
from .services import (
    converter_to_xml
)

try:
    path_temp = f'{os.getcwd()}/data_extraction/tmp'
    os.mkdir(path_temp)
except:
    pass