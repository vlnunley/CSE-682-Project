from flask import Blueprint, current_app, jsonify, make_response, request

from utils.db_query import (
    get_db_connection,
    fetch_all_model_data,
    fetch_model_data_by_id,
    create_model,
    update_model,
    delete_model
)
from utils.models import Habit, HabitEntry, Goal

habit_bp = Blueprint("habits", __name__)

@habit_bp.route("", methods=["GET"])
def get_all_habits_test():
    with get_db_connection(current_app.config) as db:
        model = Habit(**request.get_json())
        return jsonify(fetch_all_model_data(db, model))

@habit_bp.route("", methods=["POST"])
def get_all_habits():
    body = request.get_json()
    user_id=body["user_id"]

    with get_db_connection(current_app.config) as db:
        sql = f"SELECT * FROM {Habit.TABLE} WHERE user_id = %s AND active = true"
        cur = db.cursor()
        cur.execute(sql, (user_id,))
        ret = cur.fetchall()
        habits = []

        for row in ret:
            habit = {
                "id": row["id"],
                "created_date": row["created_date"],
                "name": row["name"],
                "description": row["description"],
                "classification": row["classification"]
            } 
            habits.append(habit)

    return jsonify(habits)

@habit_bp.route("/<id>", methods=["POST"])
def get_habit_by_id(id: int):
    body = request.get_json()
    user_id=body["user_id"]

    with get_db_connection(current_app.config) as db:
        sql = f"SELECT * FROM {Habit.TABLE} WHERE user_id = %s AND id = %s"
        cur = db.cursor()
        cur.execute(sql, (user_id, id))
        ret = cur.fetchone()
        habit = {
            "id": id,
            "name": ret["name"],
            "classification": ret["classification"]
        }

    return jsonify(habit)

@habit_bp.route("/create", methods=["POST", "PUT"])
def create_habit():
    with get_db_connection(current_app.config) as db:
        model = Habit(**request.get_json())
        return jsonify(create_model(db, model))

@habit_bp.route("/update/<id>", methods=["POST"])
def update_habit(id: int):
    with get_db_connection(current_app.config) as db:
        model = Habit(**request.get_json())
        try:
            update_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)
        
@habit_bp.route("/<id>", methods=["DELETE"])
def delete_habit(id: int):
    with get_db_connection(current_app.config) as db:
        model = Habit(**request.get_json())
        try:
            entrySql = "DELETE FROM habit_entry WHERE"
            delete_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)