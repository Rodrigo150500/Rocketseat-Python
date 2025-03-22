from flask import Blueprint, request, jsonify

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.main.composer.registry_user_composer import registry_user_composer
from src.main.composer.login_composer import login_composer
from src.main.composer.create_new_task_composer import create_new_task_composer
from src.main.composer.list_all_tasks_by_user_id import list_all_tasks_by_user_id_composer

from src.errors.error_handler import error_handler
from src.main.middlewares.auth_jwt import auth_jwt

tasks_routes_bp = Blueprint("tasks" ,__name__)

@tasks_routes_bp.route("/registry", methods=['POST'])
def registry_user():
    
    try:
        http_request = HttpRequest(body=request.json)
        http_response = registry_user_composer().handle(http_request)

        return jsonify(http_response.body, http_response.status_code)
    
    except Exception as exception:
        http_response = error_handler(exception)

        return jsonify(http_response.body), http_response.status_code

@tasks_routes_bp.route("/login", methods=["POST"])
def login():


    try:

        http_request = HttpRequest(body=request.json)
        http_response = login_composer().handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except Exception as exception:

        http_response = error_handler(exception)

        return jsonify(http_response.body), http_response.status_code



@tasks_routes_bp.route("/create_new_task/<user_id>", methods=["POST"])
def create_new_task(user_id):

    try:
        token_info = auth_jwt()

        http_request = HttpRequest(body=request.json,
                                   params={"user_id": user_id},
                                   header= request.headers,
                                   token_info= token_info
                                   )

        http_response = create_new_task_composer().handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        
        http_response = error_handler(exception)

        return jsonify(http_response.body), http_response.status_code

@tasks_routes_bp.route("/list_all_tasks/<user_id>", methods=["GET"])
def list_all_tasks(user_id):

    try:
        token_info = auth_jwt()

        http_request = HttpRequest(params={"user_id": user_id},
                                    token_info=token_info)
        http_response = list_all_tasks_by_user_id_composer().handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
        
    except Exception as exception:

        http_response = error_handler(exception)

        return jsonify(http_response.body), http_response.status_code