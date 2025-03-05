from flask import jsonify, request, Blueprint
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pessoa_juridica_consultar_saldo_composer import pessoa_juridica_consultar_saldo_composer
from src.main.composer.pessoa_juridica_criar_usuario_composer import pessoa_juridica_criar_usuarios_composer
from src.main.composer.pessoa_juridica_listar_usuarios_composer import pessoa_juridica_listar_usuarios_composer
from src.main.composer.pessoa_juridica_realizar_extrato_composer import pessoa_juridica_realizar_extrato
from src.main.composer.pessoa_juridica_sacar_dinheiro_composer import pessoa_juridica_sacar_dinheiro_composer


pessoa_juridica_route_bp = Blueprint("pessoa_juridica_route", __name__)

@pessoa_juridica_route_bp.route("/pessoa_juridica/consultar_saldo", methods = ["GET"])
def pj_consultar_saldo():
    
    http_request = HttpRequest(request.json)

    http_response = pessoa_juridica_consultar_saldo_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code 

@pessoa_juridica_route_bp.route("/pessoa_juridica/criar_usuario", methods=["POST"])
def pj_criar_usuario():

    http_request = HttpRequest(body = request.json)

    http_response = pessoa_juridica_criar_usuarios_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/pessoa_juridica/listar_usuarios", methods=["GET"])
def pj_listar_usuarios():

    http_request = HttpRequest()

    http_response = pessoa_juridica_listar_usuarios_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/pessoa_juridica/realizar_extrato", methods = ["GET"])
def pj_realizar_extrato():

    http_request = HttpRequest(request.json)

    http_response = pessoa_juridica_realizar_extrato().handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route("/pessoa_juridica/sacar_dinheiro", methods = ["PATCH"])
def pj_sacar_dinheiro():

    http_request = HttpRequest(body = request.json)

    http_response = pessoa_juridica_sacar_dinheiro_composer().handle(http_request)

    return jsonify(http_response.body), http_response.status_code