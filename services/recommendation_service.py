from const import FRIENDS, REFERRAL_ID, HOMETOWN, PROFESSION, INTERESTS, AIMS, CONTACTS, REFERRAL_ID
from collections import defaultdict
from app.serializers import RecommendationRequest


vector_fields = ["hometown", "profession", "aims", "interests"]


def exponential_increase(exponential_base, n):
    if n == 0:
        return 0
    return (2 - 1/n) * exponential_base


def filter_and_sort_recommendations(recommendations):
    filtered_recommendations = {user_id: score for user_id, score in recommendations.items() if score > 0}
    sorted_recommendations = sorted(filtered_recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations


class RecommendationService:

    def calculate_recommendations(self, related_users, closest_users, recommendation_request: RecommendationRequest):
        final_recommendations = defaultdict(int)
        excluded = recommendation_request.exclude + recommendation_request.contacts + [recommendation_request.userId]
        contacts = set(recommendation_request.contacts)
        events = set(recommendation_request.events)
        for user in related_users:
            if user['id'] in excluded:
                continue
            score = 0
            contact_intersection = len(contacts.intersection(set(user.get(CONTACTS, []))))
            events_intersection = len(events.intersection(set(user.get(INTERESTS, []))))
            score += exponential_increase(recommendation_request.baseMutualContactsValue, contact_intersection)
            score += exponential_increase(recommendation_request.baseMutualEventsValue, events_intersection)
            score += user.get(REFERRAL_ID) == recommendation_request.referralUserID and recommendation_request.referralUserIdValue or 0
            final_recommendations[user['id']] = score
        for user in closest_users:
            final_recommendations[user['id']] += user['score']
            if final_recommendations[user['id']] < recommendation_request.cutoffValue:
                del final_recommendations[user['id']]

        return filter_and_sort_recommendations(final_recommendations)

    def get_single_user_recommendations(self, request: RecommendationRequest):
        pass

    def get_recommended_users(self, related_users, closest_users: dict, recommendation_request: RecommendationRequest):
        reccomendations = self.calculate_recommendations(related_users, closest_users, recommendation_request)
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

recommendation_service = RecommendationService()


if __name__ == "__main__":
    service = RecommendationService()
    recommended_users = service.get_recommended_users()
    print(recommended_users)
