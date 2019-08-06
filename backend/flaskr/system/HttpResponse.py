from flask import jsonify, Response
import os
from flaskr.system import config


class HttpResponse:
    def __init__(self):
        pass

    @staticmethod
    def success_response(data, code=200):
        resp = jsonify(data) if type(data) != Response else data
        resp.headers['Access-Control-Allow-Origin'] = os.environ["PERMIT_APP"]
        resp.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.status_code = code
        return resp

    @staticmethod
    def error_response(data, code=400):
        resp = jsonify(data) if type(data) != Response else data
        resp.headers['Access-Control-Allow-Origin'] = os.environ["PERMIT_APP"]
        resp.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.status_code = code
        return resp
