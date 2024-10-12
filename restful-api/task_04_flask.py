"""Create a Flask application."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user details.
users = {}


@app.route('/')
def home():
    """
    Endpoint to display a welcome message.
    """
    return "<p>Welcome to the Flask API!</p>"


@app.route('/data')
def get_data():
    """
    Endpoint to return a JSON object.
    """
    usernames = list(users.keys())
    return jsonify(usernames), 200


@app.route('/status')
def status():
    """
    Endpoint to return a simple status message.
    """
    return "<p>OK</p>"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint to return the details of a user.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user.
    """
    if not request.json or 'username' not in request.json:
        return jsonify({"error": "Invalid request"}), 400
    new_user = request.get_json()
    username = new_user.get["username"]
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": new_user.get("username"),
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


"""
Run the Flask application.
"""
if __name__ == '__main__':
    app.run()
