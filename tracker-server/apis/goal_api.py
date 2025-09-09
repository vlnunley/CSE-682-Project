from flask import Blueprint, current_app, jsonify, make_response, request

from utils.db_query import (
    get_db_connection,
    fetch_all_model_data,
    fetch_model_data_by_id,
    create_model,
    update_model,
    delete_model
)
from utils.models import Goal

goal_bp = Blueprint("goal", __name__)

@goal_bp.route("", methods=["POST"])
def get_goals():
    body = request.get_json()
    habit_id = body["habit_id"]

    with get_db_connection(current_app.config) as db:
        cur = db.cursor()
        sql = f"SELECT * FROM {Goal.TABLE} WHERE habit_id = %s"
        cur.execute(sql, (habit_id,))
        ret = cur.fetchall()
        goals = []

        for row in ret:
            goal = {
                "name": row["name"],
                "frequencyNum": row["frequency_num"],
                "frequencyType": row["frequency_type"]
            }
            goals.append(goal)

    return jsonify(goals)

@goal_bp.route("/create", methods=["POST", "PUT"])
def create_goal():
    with get_db_connection(current_app.config) as db:
        model = Goal(**request.get_json())
        return jsonify(create_model(db, model))

@goal_bp.route("/update/<id>", methods=["POST"])
def update_goal(id: int):
    with get_db_connection(current_app.config) as db:
        model = Goal(**request.get_json())
        try:
            update_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)
        
@goal_bp.route("/<id>", methods=["POST"])
def delete_goal(id: int):
    with get_db_connection(current_app.config) as db:
        model = Goal(**request.get_json())
        try:
            return jsonify(delete_model(db, model, id))
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)