from urllib.parse import quote_plus
import os


PROD = 'PROD'
TEST = 'TEST'

ENVIRONMENT = os.environ.get('ENVIRONMENT', PROD)

# MongoDB connection settings
if ENVIRONMENT == PROD:
    DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "MY_DATABASE_NAME")
    COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "USER_RECOMMENDATIONS")
    MONGO_CONNECTION_URI = os.getenv("MONGO_CONNECTION_URI")

LYNQ_SECRET = os.getenv("LYNQ_API_SECRET", "")
LYNQ_API_URL = os.getenv("LYNQ_API_URL", "https://api-staging.lynq.me/api/v1/users/matching")
LYNQ_API_USER_LIMIT = 1000

# API authentication token
API_AUTH_TOKEN = os.getenv("LYNQ_API_SECRET", "test")

TOKEN_LIST = {
    API_AUTH_TOKEN: "default_user",
}