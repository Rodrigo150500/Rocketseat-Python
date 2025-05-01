from flask import request, jsonify, Blueprint
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.main.composer.registry_order_composer import registry_order_composer
from src.errors.erro_handler import error_handler

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():

    use_case = registry_order_composer()
    
    http_request = HttpRequest(body=request.json)

    response = use_case.registry(http_request)

    return jsonify(response.body), response.status_code

