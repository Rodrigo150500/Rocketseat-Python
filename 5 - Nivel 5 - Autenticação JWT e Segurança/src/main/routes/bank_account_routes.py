from flask import Blueprint, jsonify

bank_account_bp =Blueprint("bank_account", __name__)

@bank_account_bp.route("/", methods=['GET'])
def hello():
    return jsonify({"hello": 'words'}), 200

