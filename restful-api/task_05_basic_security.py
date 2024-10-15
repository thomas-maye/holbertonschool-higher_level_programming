#!/usr/bin/env python
"""Create an Secure API with Flask using Basic and JWT Authentication."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)


# Create a Flask app
app = Flask(__name__)

# Role based protected route
app.config["SECRET_KEY"] = 'thisisasecretkey'

# Create an instance of HTTPBasicAuth for basic authentication
auth = HTTPBasicAuth()

# Create an instance of JWTManager for JWT authentication
jwt = JWTManager(app)

# Create a dictionary of users with their passwords
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


# Verify password for basic authentication
@auth.verify_password
def verify_password(username, password):
    """Method to verify the username and password"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


# Create a route to return a welcome message
@app.route('/')
def home():
    """Endpoint to return a welcome message."""
    return "Welcome to the Flask API!"


# Basic Authenticationprotected route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Method to return a protected response"""
    return "Basic Auth: Access Granted"

@app.route('/signup', methods=['POST'])
def signup():
    """Method to signup a user"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username:
        return jsonify({"error": "Missing username"}), 400
    if not password:
        return jsonify({"error": "Missing password"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {"username": username, "password": generate_password_hash(password), "role": "user"}
    return jsonify({"message": "User created", "user": users[username]})

# Login route to get a token
@app.route('/login', methods=['POST'])
def login():
    """Method to login and get a token"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username,
                                                     'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


# JWT Authentication protected route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Method to return a protected response"""
    return "JWT Auth: Access Granted"


# Role based protected route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Method to return a protected response for admin only"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# Custom error handlers for JWT
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


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
