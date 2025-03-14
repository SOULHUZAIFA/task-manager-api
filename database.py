import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/task_manager")

client = MongoClient(MONGO_URI)
db = client["task_manager"]
tasks_collection = db["tasks"]