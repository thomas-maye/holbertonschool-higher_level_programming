#!/usr/bin/env python
"""Create an Secure API with Flask using Basic and JWT Authentication."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)


# Dictionary to store user data with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Create a Flask app
app = Flask(__name__)
# Create an instance of HTTPBasicAuth for basic authentication
auth = HTTPBasicAuth()


# Create a function to verify the password for basic authentication
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# Create a page handler for the home page
@app.route("/")
def home():
    return "Welcome to the Flask API!"


#  Create a protected route that requires basic authentication
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# Role based protected route
app.config["JWT_SECRET_KEY"] = 'my_secret_key'
# Create an instance of JWTManager for JWT authentication
jwt = JWTManager(app)

# Create a route to login and get a JWT token
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


# Create a protected route that requires JWT authentication
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Create a protected route that requires JWT authentication and admin role
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    if current_user not in users:
        return jsonify({"error": "User not found"}), 404

    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Error handlers for JWT authentication
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run()