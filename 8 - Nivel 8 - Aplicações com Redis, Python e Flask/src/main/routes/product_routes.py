from flask import Blueprint,jsonify, request
from src.main.composer.product_creator_composer import product_creator_composer
from src.main.composer.product_finder_composer import product_finder_composer

from src.http_types.http_request import HttpRequest

products_routes_bp = Blueprint("products", __name__)

@products_routes_bp.route("/products", methods=["POST"])
def insert_product():

    http_request = HttpRequest(body=request.json)
    creator_composer = product_creator_composer()

    response = creator_composer.create(http_request)

    return jsonify(response.body), response.status_code


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):

    http_request= HttpRequest(params={"product_name": product_name})
    
    finder_composer = product_finder_composer()

    response = finder_composer.find_by_name(http_request)
    
    return jsonify(response.body), response.status_code