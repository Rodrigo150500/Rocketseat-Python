from flask import request, jsonify, Blueprint
from src.calculators.calculator1 import Calculator1
from src.calculators.calculator2 import Calculator2
from src.drivers.numpy_handlers import Numpy_handlers

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route("/calculator/1", methods = ["POST"])
def calculator_1():

    calc = Calculator1()
    response = calc.calculate(request)
    
    return jsonify(response), 200

@calc_route_bp.route("/calculator/2", methods = ['POST'])
def calculator_2():

    numpy_driver_handler = Numpy_handlers()

    calc = Calculator2(numpy_driver_handler)


    response = calc.calculate(request)

    return(jsonify(response)), 200