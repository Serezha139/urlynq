from services.mongodb import mongo_service


def clean_mongo():
    mongo_service.delete_all_documents()


if __name__ == '__main__':
    clean_mongo()
