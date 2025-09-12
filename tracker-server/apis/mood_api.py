from flask import Blueprint, current_app, jsonify, make_response, request

from utils.db_query import (
    get_db_connection,
    fetch_all_model_data,
    fetch_model_data_by_id,
    create_model,
    update_model,
    delete_model
)
from utils.models import MoodEntry, Mood

mood_bp = Blueprint("mood", __name__)

@mood_bp.route("", methods=["POST"])
def get_goals():
    body = request.get_json()
    user_id = body["user_id"]

    with get_db_connection(current_app.config) as db:
        cur = db.cursor()
        sql = f"SELECT * FROM {MoodEntry.TABLE} WHERE user_id = %s"
        cur.execute(sql, (user_id,))
        ret = cur.fetchall()
        moods = []

        for row in ret:
            emoji = getEmoji(row["mood_id"])
            mood = {
                "id": row["id"],
                "created_date": row["created_date"],
                "note": row["note"],
                "mood": emoji,
            }
            moods.append(mood)

    return jsonify(moods)

@mood_bp.route("/create", methods=["POST", "PUT"])
def create_goal():
    with get_db_connection(current_app.config) as db:
        model = MoodEntry(**request.get_json())
        return jsonify(create_model(db, model))

@mood_bp.route("/update/<id>", methods=["POST"])
def update_goal(id: int):
    with get_db_connection(current_app.config) as db:
        model = MoodEntry(**request.get_json())
        try:
            update_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)
        
@mood_bp.route("/<id>", methods=["POST"])
def delete_goal(id: int):
    with get_db_connection(current_app.config) as db:
        model = MoodEntry(**request.get_json())
        try:
            return jsonify(delete_model(db, model, id))
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)
        
@mood_bp.route("/initEmojis")
def initEmojis():
    emotions = ["Contempt", "Happy", "Sad", "Angry", "Anxious", "Tired", "Excited"]
    with get_db_connection(current_app.config) as db:
        sql = f"INSERT INTO mood (name) VALUES (%s) returning id"
        with db.cursor() as cur:
            for e in emotions:
                cur.execute(sql, (e,))
                db.commit()
    return jsonify("Okay!")

@mood_bp.route("/emojis", methods=["GET"]) 
def getAllEmojis():
    with get_db_connection(current_app.config) as db:
        return fetch_all_model_data(db, Mood)
    
def getEmoji(mood_id):
    with get_db_connection(current_app.config) as db:
        sql = f"SELECT * FROM {Mood.TABLE} WHERE id = %s"
        cur = db.cursor()
        cur.execute(sql, (mood_id, ))
        ret = cur.fetchone()

        return ret["name"]