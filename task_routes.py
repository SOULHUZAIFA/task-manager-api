from flask import Blueprint, jsonify, request
from database import tasks_collection
from models import Task

task_blueprint = Blueprint("tasks", __name__)

@task_blueprint.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = list(tasks_collection.find({}, {"_id": 0}))
    return jsonify(tasks), 200

@task_blueprint.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(data["title"], data["description"])
    tasks_collection.insert_one(task.to_dict())
    return jsonify({"message": "Task added"}), 201

@task_blueprint.route("/tasks/<string:title>", methods=["DELETE"])
def delete_task(title):
    tasks_collection.delete_one({"title": title})
    return jsonify({"message": "Task deleted"}), 200