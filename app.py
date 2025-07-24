from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify, request
from flask_cors import CORS
from bson import ObjectId

import time


app = Flask(__name__)
# CORS(app)
# CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
# CORS(app, resources={r"/*": {"origins": "http://localhost:5500"}}, supports_credentials=True)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}}, supports_credentials=True)


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

    print(f"Inserting into collection '{collection_name}':", data)
    result = collection.insert_one(data)
    return jsonify({"status":"success"})

@app.route("/data/<collection_name>/", methods=['GET'])
def fetcher(collection_name):
    # time.sleep(3)
    db = client["mydatabase"]
    collection = db[collection_name]

    documents = list(collection.find())

    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return jsonify(documents)



@app.route("/edit/<collection_name>/<id>/", methods=["PUT", "OPTIONS"])
def updater(collection_name, id):
    if request.method == "OPTIONS":
        return '', 200
    collection = db[collection_name]
    data = request.json
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count:
        return jsonify({"status": "updated"})
    return jsonify({"error": "not found"}), 404

@app.route("/delete/<collection_name>/<id>/", methods=["DELETE"])
def deleter(collection_name, id):
    collection = db[collection_name]
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"status": "deleted"})
    return jsonify({"error": "not found"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)