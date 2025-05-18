from flask import Blueprint,jsonify

products_routes_bp = Blueprint("products", __name__)

@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"ola": "mundo"})

@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"ola": product_name})