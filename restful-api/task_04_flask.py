from flask import Flask, jsonify, request

app = Flask(__name__)

# The users dictionary will store the user data
users = {}


@app.route('/')
def home():
    """
    Endpoint to welcome the user to the API.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    Endpoint to retrieve the list of usernames.
    """
    usernames = list(users.keys())
    return jsonify(usernames), 200


@app.route('/status')
def status():
    """
    Endpoint to check the status of the API.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint to retrieve the user data for a specific username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

    if username is None:
        return jsonify({"error": "Username is required"}), 400


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user to the users dictionary.
    """
    new_user_data = request.get_json()

    # Check if the request data is empty
    username = new_user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user to the users dictionary
    users[username] = {
        "username": new_user_data.get('username'),
        "name": new_user_data.get('name'),
        "age": new_user_data.get('age'),
        "city": new_user_data.get('city')
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # Run the Flask app
    app.run()
