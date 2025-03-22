from flask import Blueprint, request, jsonify

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.main.composer.registry_user_composer import registry_user_composer

from src.errors.error_handler import error_handler

tasks_routes_bp = Blueprint("tasks" ,__name__)

@tasks_routes_bp.route("/registry", methods=['POST'])
def registry_user():
    
    try:
        http_request = HttpRequest(body=request.json)
        http_response = registry_user_composer().handle(http_request)

        return jsonify(http_response.body, http_response.status_code)
    
    except Exception as exception:
        http_response = error_handler(exception)

        return jsonify(http_response.body, http_response.status_code)