import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import blueprint, abort
from db import stores
