from flask import Flask


app = Flask(__name__)


from .controllers import (
    main_controller
)