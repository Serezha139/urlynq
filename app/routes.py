from flask import Blueprint, request, jsonify
from services.mongodb import mongo_service
from services.recommendation_service import recommendation_service
from pydantic import ValidationError
from app.auth import auth
from app.serializers import RecommendationRequest
from exceptions import UserNotFoundException


main = Blueprint('main', __name__)

USERNAME = 'admin'
PASSWORD = 'secret'


@main.route('/recommended_users', methods=['POST'])
@auth.login_required
def recommended_users():
    """
    Endpoint to get recommended users.
    Requires basic authentication.
    """
    data = request.get_json()
    try:
        request_data = RecommendationRequest(**data)
        related_users = mongo_service.get_related_users(
            contacts=request_data.contacts,
            events=request_data.events,
            circles=request_data.circles
        )
        closest_users = mongo_service.get_closest_users(request_data.prompt)
        recommendations = recommendation_service.get_recommended_users(related_users, closest_users, request_data)
    except UserNotFoundException:
        return jsonify({"error": "User not found"}), 404
    except ValidationError as e:
        return jsonify(e.errors()), 400

    return jsonify(recommendations)
