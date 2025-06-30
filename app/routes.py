from flask import Blueprint, request, jsonify
from services.mongodb import mongo_service
from services.recommendation_service import recommendation_service
from pydantic import ValidationError
from app.auth import auth
from app.serializers import RecommendationRequest
from exceptions import UserNotFoundException

import logging
logger = logging.getLogger()


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
    try:
        data = request.get_json()

        logger.info('Received request for recommended users.')
        request_data = RecommendationRequest(**data)
        related_users = mongo_service.get_related_users(
            contacts=request_data.contacts,
            events=request_data.events,
            circles=request_data.circles,
            referral_user_id=request_data.referralUserID,
        )
        closest_users = mongo_service.get_closest_users(request_data.prompt)
        recommendations = recommendation_service.get_recommended_users(related_users, closest_users, request_data)
    except UserNotFoundException:
        return jsonify({"error": "User not found"}), 404
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except Exception as e:
        import traceback
        tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        payload = {'errror': tb_str}
        return jsonify(payload), 500

    return jsonify(recommendations)
