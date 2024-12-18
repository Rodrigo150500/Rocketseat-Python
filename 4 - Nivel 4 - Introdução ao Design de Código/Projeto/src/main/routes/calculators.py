from flask import request, jsonify, Blueprint
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator3_factory import calculator3_factory

from src.errors.error_controller import handler_error



calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route("/calculator/1", methods = ["POST"])
def calculator_1():

    try:

        calc = calculator1_factory()

        response = calc.calculate(request)
        
        return jsonify(response), 200
    
    except Exception as exception:
        
        error_response = handler_error(exception)

        return jsonify(error_response)

@calc_route_bp.route("/calculator/2", methods = ['POST'])
def calculator_2():

    try:
        calc = calculator2_factory()

        response = calc.calculate(request)

        return(jsonify(response)), 200

    except Exception as exception:
    
        error_response = handler_error(exception)

        return jsonify(error_response)

@calc_route_bp.route("/calculator/3", methods = ['POST'])
def calculator_3():

    try:

        calc = calculator3_factory()

        response = calc.calculate(request)

        return (jsonify(response)), 200
        
    except Exception as exception:
    
        error_response = handler_error(exception)

        return jsonify(error_response)