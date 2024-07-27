from flask import Flask, request
from flask_smorest import Api

from resources.items import blp as itemBluePrint
from resources.store import blp as storeBluePrint
app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(itemBluePrint)
api.register_blueprint(storeBluePrint)