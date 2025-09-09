import json
from flask import Flask, request

from apis.goal_api import goal_bp
from apis.habit_api import habit_bp
from apis.habit_entry_api import habit_entry_bp
from apis.user_api import user_bp

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

app.register_blueprint(goal_bp, url_prefix="/goal")
app.register_blueprint(habit_bp, url_prefix="/habit")
app.register_blueprint(habit_entry_bp, url_prefix="/habit_entry")
app.register_blueprint(user_bp)

for rule in app.url_map.iter_rules():
    print(rule, rule.methods)

@app.before_request
def log_request():
    print(">>>", request.method, request.path)

@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, PUT, DELETE, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Origin, Authorization, Content-Type, X-Auth-Token")
    return response

@app.route("/")
def index():
    return "API for the Habit and Mood Tracker"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)