from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify


app = Flask(__name__)

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
@app.route("/insert")
def insert():
        db = client["mydatabase"]
        collection = db["mycollection"]
        data = {"name": "Jane Doe", "age": 25, "email": "jane@example.com"}
        result = collection.insert_one(data)
        print("inserted!!")
        return jsonify({"inserted_id": str(result.inserted_id)})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
