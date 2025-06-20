from sentence_transformers import SentenceTransformer
from const import VECTOR_FIELDS, FIELD_WEIGHTS



def transform_to_vector(json_data):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    vectorized_data = []
    for record in json_data["data"]["users"]:
        vector_payload = process_record(model, record)
        vectorized_data.append(vector_payload)
    # Fields to be converted to vectors

    return vectorized_data


def process_record(model, record):
    vector = []
    for field in VECTOR_FIELDS:
        if field in record:
            vector.extend(
                record[field] if isinstance(record[field], list) else [record[field] * FIELD_WEIGHTS.get(field, 1)])
    # Initialize the SentenceTransformer model
    # Generate the vector representation
    vector = model.encode([" ".join(map(str, vector))], convert_to_tensor=True).tolist()[0]
    # Prepare data for insertion: vector and payload
    vector_payload = {"vector": vector, "payload": record}
    return vector_payload
