from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel
import time
from settings import MONGO_CONNECTION_URI, COLLECTION_NAME, DATABASE_NAME

# Connect to your Atlas deployment
client = MongoClient(MONGO_CONNECTION_URI)

# Access your database and collection
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

# Create your index model, then create the search index
search_index_model = SearchIndexModel(
  definition={
    "fields": [
      {
        "type": "vector",
        "path": "plot_embedding",
        "numDimensions": 384,
        "similarity": "dotProduct",
        "quantization": "scalar"
      }
    ]
  },
  name="vector_index",
  type="vectorSearch"
)

result = collection.create_search_index(model=search_index_model)
print("New search index named " + result + " is building.")

# Wait for initial sync to complete
print("Polling to check if the index is ready. This may take up to a minute.")
predicate=None
if predicate is None:
    predicate = lambda index: index.get("queryable") is True

while True:
    indices = list(collection.list_search_indexes(result))
    if len(indices) and predicate(indices[0]):
        break
    time.sleep(5)
    print(result + " is ready for querying.")

client.close()
