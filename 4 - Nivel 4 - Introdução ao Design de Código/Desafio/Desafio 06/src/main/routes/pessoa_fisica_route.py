from flask import Blueprint, jsonify

pessoa_fisica_route_bp = Blueprint("pessoa_fisica_route", __name__)


@pessoa_fisica_route_bp.route("/test", methods = ['GET'])
def test():
    return jsonify({"ola": "mundo"}),200
