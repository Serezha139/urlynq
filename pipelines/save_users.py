from services.lynq_load_service import lynq_service
from services.mongo_vectorization import vectorization_service
from services.mongodb import mongo_service


def save_users_to_mongo():
    json_data = lynq_service.get_user_data()
    print("Fetched data from Lynq service:", json_data)
    vectorized_data = vectorization_service.transform_to_vector(json_data)
    print("Transformed data to vectors:", vectorized_data)
    mongo_service.delete_all_documents()  # Clear existing documents
    mongo_service.insert_many(vectorized_data)
    print("Users saved to MongoDB successfully.")


if __name__ == "__main__":
    save_users_to_mongo()
