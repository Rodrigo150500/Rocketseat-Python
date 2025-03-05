from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pessoa_fisica_listar_usuarios_composer import pessoa_fisica_listar_usuarios_composer
from src.main.composer.pessoa_fisica_consultar_saldo_composer import pessoa_fisica_consultar_saldo_composer
from src.main.composer.pessoa_fisica_criar_usuario_composer import pessoa_fisica_criar_usuario_composer
from src.main.composer.pessoa_fisica_realizar_extrato_composer import pessoa_fisica_realizar_extrato_composer
from src.main.composer.pessoa_fisica_sacar_dinheiro_composer import pessoa_fisica_sacar_dinheiro_composer

pessoa_fisica_route_bp = Blueprint("pessoa_fisica_route", __name__)

@pessoa_fisica_route_bp.route("/pessoa_fisica/listar_usuarios", methods = ["GET"])
def pf_listar_usuarios():

    http_request = HttpRequest()

    http_response = pessoa_fisica_listar_usuarios_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/pessoa_fisica/consultar_saldo", methods = ["GET"])
def pf_consultar_saldo():

    http_request = HttpRequest(body = request.json)

    http_response = pessoa_fisica_consultar_saldo_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/pessoa_fisica/criar_usuario", methods = ["POST"])
def pf_criar_usuario():

    http_request = HttpRequest(request.json)

    http_response = pessoa_fisica_criar_usuario_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/pessoa_fisica/realizar_extrato", methods = ["GET"])
def pf_realizar_extrato():

    http_request = HttpRequest(request.json)

    http_response = pessoa_fisica_realizar_extrato_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/pessoa_fisica/sacar_dinheiro", methods = ["PATCH"])
def pf_sacar_dinheiro():

    http_request = HttpRequest(body=request.json)

    http_response = pessoa_fisica_sacar_dinheiro_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code