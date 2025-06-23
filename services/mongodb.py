from pymongo import MongoClient
import settings
from exceptions import UserNotFoundException
from services.mongo_vectorization import vectorize


class MongoDBService:
    def __init__(self):
        mongo_client = MongoClient(settings.MONGO_CONNECTION_URI, tlsAllowInvalidCertificates=True)
        database = mongo_client[settings.DATABASE_NAME]
        self.collection = database[settings.COLLECTION_NAME]

    def insert_many(self, data):
        if isinstance(data, list):
            return self.collection.insert_many(data)
        else:
            raise ValueError("Data must be a list of documents.")

    def find(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def fetch_all(self):
        return list(self.collection.find({}))

    def delete_many(self, query):
        return self.collection.delete_many(query)

    def delete_all_documents(self):
        return self.collection.delete_many({})

    def update_many(self, filter_query, update_query):
        return self.collection.update_many(filter_query, update_query)

    def get_recommended_users(self, user_id):
        search_query = {"payload.id": user_id}
        result = self.collection.find_one(search_query)
        if not result:
            raise UserNotFoundException(f"User with id {user_id} not found or has no recommendations.")
        return result.get('recommendations', [])

    def get_related_users(self, contacts, circles, events, referral_user_id):
        result = self.collection.find({
            "$or": [
                {"payload.contacts": {"$in": contacts}},
                #{"payload.circles": {"$in": circles}},
                {"payload.events": {"$in": events}},
                {"payload.referralUserId": referral_user_id}
            ]
        })
        return [item['payload'] for item in result]

    def get_closest_users(self, prompt):
        user_vector = vectorize(prompt)
        pipeline = [
            {
                '$vectorSearch': {
                    'index': 'vector_index',
                    'path': 'vector',
                    'queryVector': user_vector,
                    'numCandidates': 150,
                    'limit': 150,
                }
            }, {
                '$project': {
                    '_id': 0,
                    'payload.id': 1,
                    'score': {
                        '$meta': 'vectorSearchScore'
                    }
                }
            }
        ]
        result = self.collection.aggregate(pipeline)
        return [{"id": item["payload"]["id"], "score": item["score"]} for item in result]


if settings.ENVIRONMENT == settings.TEST:
    from unittest.mock import MagicMock
    mongo_service = MagicMock()
else:
    mongo_service = MongoDBService()

