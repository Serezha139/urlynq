from services.mongodb import mongo_service
from services.recommendation_service import recommendation_service

def save_recommendations():
    users = mongo_service.fetch_all()
    all_closest_users = {}
    for user in users:
        max_score = recommendation_service.get_max_score(user)
        closest_users = mongo_service.get_n_closest_users(user['vector'], user['payload']['id'], n=10, max_score=max_score)
        all_closest_users[user['payload']['id']] = closest_users
    recommendations = recommendation_service.get_recommended_users(users, all_closest_users)
    for user_id, recs in recommendations.items():
        mongo_service.update_many(
            {"payload.id": user_id},
            {"$set": {"recommendations": recs}}
        )


if __name__ == "__main__":
    save_recommendations()
    print("Recommendations saved successfully.")