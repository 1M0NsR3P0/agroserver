from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify, request
from flask_cors import CORS
import time


app = Flask(__name__)
CORS(app)


uri = "mongodb+srv://imon:imon55@c0.ckcrbdq.mongodb.net/?retryWrites=true&w=majority&appName=C0"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Connected to MongoDB and accessed collection successfully!")
except Exception as e:
    print(str(e))

@app.route('/')
def home():
    print("server started!!")
    return "server started"
@app.route("/insert/<collection_name>/", methods=['POST'])
def insert(collection_name):
    db = client["mydatabase"]
    collection = db[collection_name]
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    if "date" not in data or "amount" not in data or "note" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    print(f"Inserting into collection '{collection_name}':", data)
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)})

@app.route("/data/<collection_name>/", methods=['GET'])
def fetcher(collection_name):
    time.sleep(3)
    db = client["mydatabase"]
    collection = db[collection_name]

    documents = list(collection.find())

    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return jsonify(documents)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
