from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    uri = "mongodb+srv://imon:imon55@c0.ckcrbdq.mongodb.net/?retryWrites=true&w=majority&appName=C0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        db = client["mydatabase"]
        collection = db["mycollection"]
        return "Connected to MongoDB and accessed collection successfully!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
