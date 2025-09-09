from flask import Blueprint, current_app, jsonify, make_response, request

from utils.db_query import (
    get_db_connection,
    fetch_model_data_by_id,
    create_model,
    update_model
)
from utils.models import Users

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/<name>", methods=["GET"])
def get_user(name: str):
    with get_db_connection(current_app.config) as db:
        sql = f"SELECT * FROM {Users.TABLE} WHERE username = %s"
        cur = db.cursor()
        cur.execute(sql, (name,))
        ret = cur.fetchone()

        user = {
            "id": ret["id"],
            "username": name,
            "password": ret["password"]
        }

        return jsonify(user)
    
@user_bp.route("/create", methods=["POST", "PUT"])
def create_user():
    with get_db_connection(current_app.config) as db:
        model = Users(**request.get_json())
        return jsonify(create_model(db, model))

@user_bp.route("/update/<id>", methods=["POST"])
def update_user(id: int):
    with get_db_connection(current_app.config) as db:
        model = Users(**request.get_json())
        try:
            update_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)
        
def check_user():
    pass
    
    