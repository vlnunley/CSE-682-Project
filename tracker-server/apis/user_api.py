from flask import Blueprint, current_app, jsonify, make_response, request

from utils.db_query import (
    get_db_connection,
    fetch_model_data_by_id,
    create_model,
    update_model
)
from utils.models import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/<id>", methods=["GET"])
def get_user(id: int):
    with get_db_connection(current_app.config) as db:
        return jsonify(fetch_model_data_by_id(id))

@user_bp.route("/create", methods=["POST, PUT"])
def create_goal():
    with get_db_connection(current_app.config) as db:
        model = User(**request.get_json())
        return jsonify(create_model(db, model))

@user_bp.route("/update/<id>", methods=["POST"])
def update_goal(id: int):
    with get_db_connection(current_app.config) as db:
        model = User(**request.get_json())
        try:
            update_model(db, model, id)
            return jsonify(model)
        except KeyError as exc:
            return make_response(jsonify({"error": str(exc)}), 404)