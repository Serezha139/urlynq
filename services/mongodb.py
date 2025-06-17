from pymongo import MongoClient
from settings import MONGO_CONNECTION_URI, DATABASE_NAME, COLLECTION_NAME


class MongoDBService:
    def __init__(self):
        mongo_client = MongoClient(MONGO_CONNECTION_URI, tlsAllowInvalidCertificates=True)
        database = mongo_client[DATABASE_NAME]
        self.collection = database[COLLECTION_NAME]

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

    def update_many(self, filter_query, update_query):
        return self.collection.update_many(filter_query, update_query)

    def get_n_closest_users(self, user_vector, user_id, max_score, n=10):
        pipeline = [
            {
                '$vectorSearch': {
                    'index': 'vector_index',
                    'path': 'vector',
                    'queryVector': user_vector,
                    'numCandidates': 150,
                    'limit': n + 1
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
        return [{"id": item["payload"]["id"], "score": item["score"] * max_score} for item in result if item.get('payload')['id'] != user_id]


mongo_service = MongoDBService()
