from flask import Blueprint, request, jsonify
from services.auth_service import validate_user

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    is_valid = validate_user(username, password)

    if is_valid:
        return jsonify({
            "success": True,
            "message": "Login Successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid Username or Password"
    })

