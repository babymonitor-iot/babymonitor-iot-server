from flask import Flask


app = Flask(__name__)


from .controllers import (
    main_controller
)

from project.communication.client_tv import ClientTV

client_tv = ClientTV()
