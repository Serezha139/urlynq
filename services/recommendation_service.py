from const import FRIENDS, REFERRAL_ID, FIELD_WEIGHTS, HOMETOWN, PROFESSION, INTERESTS, AIMS


vector_fields = ["hometown", "profession", "aims", "interests"]


class RecommendationService:

    def calculate_recommendations(self, users: dict, closest_users: dict):
        recommendations = {}
        final_recommendations = {}

        for user in [u["payload"] for u in users]:
            user_id = user['id']
            user_friends = set(user[FRIENDS])
            recommended_friends = []

            for other_user in [u["payload"] for u in users]:
                if user_id == other_user['id'] or other_user["id"] in user_friends:
                    continue  # Skip the current user

                score = 0

                # Check referral
                if user_id == other_user.get(REFERRAL_ID):
                    score += 6

                # Check common friends
                common_friends = user_friends.intersection(set(other_user[FRIENDS]))
                score += 4 * len(common_friends)

                if score > 0:
                    recommended_friends.append({'id': other_user['id'], 'score': score})

            # Sort recommendations by score in descending order
            recommendations[user_id] = recommended_friends
            final_recommendation = self.merge_recommendations(recommended_friends, closest_users[user_id])
            final_recommendation.sort(key=lambda x: x['score'], reverse=True)

            final_recommendations[user_id] = final_recommendation[:10]  # Limit to top 10 recommendations
        return final_recommendations

    def get_recommended_users(self, user_data: dict, closest_users: dict, n: int = 10):
        reccomendations = self.calculate_recommendations(user_data, closest_users)
        return reccomendations

    def merge_recommendations(self, recommendations, closest_users):
        """
        Merge recommendations with closest users from Qdrant.

        :param recommendations: List of recommended users with scores.
        :param closest_users: List of closest users from Qdrant.
        :return: Merged list of recommended users.
        """
        merged = {user['id']: user for user in recommendations}

        for user in closest_users:
            if user['id'] not in merged:
                merged[user['id']] = user
            else:
                merged[user['id']]['score'] += user['score']

        return list(merged.values())

    def get_max_score(self, user: dict):
        return FIELD_WEIGHTS[HOMETOWN] + FIELD_WEIGHTS[PROFESSION] + len(user['payload'][INTERESTS]) + len(user['payload'][AIMS])

recommendation_service = RecommendationService()


if __name__ == "__main__":
    service = RecommendationService()
    recommended_users = service.get_recommended_users()
    print(recommended_users)
