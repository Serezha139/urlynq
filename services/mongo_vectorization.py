from sentence_transformers import SentenceTransformer
from const import VECTOR_FIELDS

model = SentenceTransformer("roberta-large-nli-stsb-mean-tokens")

def transform_to_vector(json_data):
    vectorized_data = []
    for record in json_data:
        vector_payload = process_record(model, record)
        vectorized_data.append(vector_payload)
    # Fields to be converted to vectors

    return vectorized_data

def process_record(model, record):
    vector = []
    for field in VECTOR_FIELDS:
        if field in record:
            vector.extend(
                record[field] if isinstance(record[field], list) else [record[field]])
    # Initialize the SentenceTransformer model
    # Generate the vector representation
    vector = model.encode(" ".join(map(str, vector)), convert_to_tensor=True).tolist()
    # Prepare data for insertion: vector and payload
    vector_payload = {"vector": vector, "payload": record}
    return vector_payload


def vectorize(prompt):
    vector = model.encode(prompt, convert_to_tensor=True).tolist()
    return vector
