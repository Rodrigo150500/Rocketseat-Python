from flask import request, jsonify, Blueprint
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    http_request = HttpRequest(body=request.json)
    print(http_request)
    return jsonify({"ola":"mundo"}),200