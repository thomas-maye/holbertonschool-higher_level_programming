from flask import Flask, jsonify, request, json
"""Create a Flask API with the following endpoints:
- GET /: return a welcome message.
- GET /data: return the list of usernames.
- GET /status: return the status of the API.
- GET /users/<username>: return the profile of a user.
- POST /add_user: add a new user to the API.
"""

app = Flask(__name__)

# The dictionary to store the users' profiles.
users = {}


@app.route('/')
def home():
    """Endpoint to return a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_username():
    """Endpoint to return the list of usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Endpoint to return the status of the API."""
    return "OK"


@app.route('/users/<username>')
def name(username):
    """Endpoint to return the profile of a user."""
    if users.get(username):
        return jsonify(users.get(username))
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add a new user."""
    new_user = request.get_json()
    username = new_user.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
