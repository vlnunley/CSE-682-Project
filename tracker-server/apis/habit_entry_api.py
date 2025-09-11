from flask import Blueprint, current_app, jsonify, make_response, request

from utils.db_query import (
    get_db_connection,
    fetch_all_model_data,
    fetch_model_data_by_id,
    create_model,
    update_model,
    delete_model
)
from utils.models import HabitEntry

habit_entry_bp = Blueprint("habit_entry", __name__)


@habit_entry_bp.route("", methods=["POST"])
def get_habit_entries():
    body = request.get_json()
    habit_id=body["habit_id"]
    with get_db_connection(current_app.config) as db:
        sql = f"SELECT * FROM {HabitEntry.TABLE} WHERE habit_id = %s"
        cur = db.cursor()
        cur.execute(sql, (habit_id, ))
        ret = cur.fetchall()

        entries = []
        for row in ret:
            entry = {
                "id": row["id"],
                "created_date": row["created_date"],
                "note": row["note"],
                "status": row["status"],
            }
            entries.append(entry)

    return jsonify(entries)

@habit_entry_bp.route("/<id>", methods=["GET"])
def get_habit_entry(id: int):
    with get_db_connection(current_app.config) as db:
        sql = f"SELECT * FROM {HabitEntry.TABLE} WHERE id = %s"
        cur = db.cursor()
        cur.execute(sql, (id, ))
        ret = cur.fetchone()

        entry = {
            "id": ret["id"],
            "created_date": ret["created_date"],
            "note": ret["note"],
            "status": ret["status"],
        }
    return jsonify(entry)

@habit_entry_bp.route("/create", methods=["POST", "PUT"])
def create_habit_entry():
    with get_db_connection(current_app.config) as db:
        model = HabitEntry(**request.get_json())
        return jsonify(create_model(db, model))
    
@habit_entry_bp.route("/update/<id>", methods=["POST"])
def update_habit_entry(id: int):
    with get_db_connection(current_app.config) as db:
        model = HabitEntry(**request.get_json())
        try:
            update_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)

@habit_entry_bp.route("/<id>", methods=["POST"])
def delete_habit_entry(id: int):
    with get_db_connection(current_app.config) as db:
        model = HabitEntry(**request.get_json())
        try:
            return jsonify(delete_model(db, model, id))
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)

def get_goal(entry_id):
    with get_db_connection(current_app.config) as db:
        sql = f"SELECT name FROM goal WHERE id = %s"
        cur = db.cursor()
        cur.execute(sql, (entry_id, ))
        ret = cur.fetchone()

    return ret["name"]