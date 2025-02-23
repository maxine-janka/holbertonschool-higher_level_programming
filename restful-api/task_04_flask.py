#!/usr/bin/python3  
"""A simple API using Python with Flask"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    """View for the Home page"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Displays a list of usernames in users dictionary"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """View for success status"""
    return "OK"

@app.route('/users/<username>')
def display_user_data(username):
    """Displays user data for given username"""
    user_data = users.get(username)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=["POST"])
# Run function when POST request is made to /add_user
def add_user():
    """Adds a new user to the 'users' dictionary"""
    # Get JSON data from post request bodyand return dict
    new_user_data = request.get_json()
    new_username = new_user_data.get("username") # get the value of the key called username
    # Return error if no data or username provided
    if not new_user_data or "username" not in new_user_data:
        return jsonify({"error": "Username is required"}), 400
    # If valid data, store new users data in the users dictionary
    users[new_username] = {
        "username": new_username,
        "name": new_user_data["name"],
        "age": new_user_data["age"],
        "city": new_user_data["city"]
    }
    return jsonify({"message": "User added", "user": new_user_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
