from flask import Flask, jsonify, request
import json


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "<p>OK</p>"


@app.route('/users/<username>')
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "User is required"}), 400
    new_user = request.get_json()
    username = new_user["username"]
    users[username] = {
        "username": new_user.get("username"),
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }
    return jsonify({"message": "User is added", "user": users[username]}), 201


if __name__ == '__main__':
    app.run()
