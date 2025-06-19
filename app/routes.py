from flask import Blueprint, request, Flask, jsonify
from services.mongodb import mongo_service
from app.auth import auth
from exceptions import UserNotFoundException

main = Blueprint('main', __name__)

USERNAME = 'admin'
PASSWORD = 'secret'


@main.route('/recommended_users', methods=['GET'])
@auth.login_required
def recommended_users():
    """
    Endpoint to get recommended users.
    Requires basic authentication.
    """
    user_id = request.args.get('user_id')
    try:
        recommendations = mongo_service.get_recommended_users(user_id)
    except UserNotFoundException:
        return jsonify({"error": "User not found"}), 404
    return jsonify(recommendations)
