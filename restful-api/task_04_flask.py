from flask import Flask, jsonify, request
import json

"""
Create a Flask application.
"""
app = Flask(__name__)
"""
The users dictionary will store the user details.
"""
users = {}


@app.route('/')
def home():
    """
    Endpoint to display a welcome message.
    """
    return "<p>Welcome to the Flask API!</p>"


@app.route('/data')
def data():
    """
    Endpoint to return a JSON object.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Endpoint to return a simple status message.
    """
    return "<p>OK</p>"


@app.route('/users/<username>')
def user(username):
    """
    Endpoint to return the details of a user.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user.
    """
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


"""
Run the Flask application.
"""
if __name__ == '__main__':
    app.run()
