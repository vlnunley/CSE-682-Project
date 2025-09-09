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
            entries = get_habit_entries(row["id"])
            goals = get_goals(row["id"])
            habit = {
                "id": row["id"],
                "name": row["name"],
                "goals": goals,
                "entries": entries
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
        
        entries = get_habit_entries(id)
        goals = get_goals(id)
        habit = {
            "id": id,
            "name": ret["name"],
            "goals": goals,
            "entries": entries
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

def get_habit_entries(id: int):
    with get_db_connection(current_app.config) as db:
        cur = db.cursor()
        sql = f"SELECT * FROM {HabitEntry.TABLE} WHERE habit_id = %s"
        cur.execute(sql, (id,))
        ret = cur.fetchall()
        entries = []

        for row in ret:
            entry = {
                "created_date": row["created_date"],
                "note": row["note"],
                "status": row["status"],
            }
            entries.append(entry)
        
    return entries

def get_goals(id: int):
    with get_db_connection(current_app.config) as db:
        cur = db.cursor()
        sql = f"SELECT * FROM {Goal.TABLE} WHERE habit_id = %s"
        cur.execute(sql, (id,))
        ret = cur.fetchall()
        goals = []

        for row in ret:
            goal = {
                "name": row["name"],
                "frequencyNum": row["frequency_num"],
                "frequencyType": row["frequency_type"]
            }
            goals.append(goal)

    return goals