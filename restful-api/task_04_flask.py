from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user details.
users = {}


@app.route('/')
def home():
    """
    Endpoint to display a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
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
    return "OK"


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
    new_user = request.get_json()

    # Check if the username is provided.
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the user already exists.
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user to the dictionary.
    users[username] = {
        "username": new_user.get('username'),
        "name": new_user.get('name'),
        "age": new_user.get('age'),
        "city": new_user.get('city')
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # Run the Flask app.
    app.run()
