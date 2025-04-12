from flask import request, jsonify, Blueprint

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    print(request.json)
    return jsonify({"ola":"mundo"}),200