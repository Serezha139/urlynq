from urllib.parse import quote_plus
import os

# MongoDB connection settings
DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")
MONGO_USERNAME = quote_plus(os.getenv("MONGO_USERNAME"))
MONGO_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_APP_NAME = os.getenv("MONGO_APP_NAME")
MONGO_CONNECTION_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?retryWrites=true&w=majority&appName={MONGO_APP_NAME}"

# LYNQ API settings
LYNQ_SECRET = os.getenv("LYNQ_API_SECRET", "")
LYNQ_API_URL = os.getenv("LYNQ_API_URL", "https://lynq-server-06d2fa72825a.herokuapp.com/api/v1/users/matching")
