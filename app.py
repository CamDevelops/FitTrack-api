# Imports
from flask import Flask, jsonify, request

# App Initialization
app = Flask(__name__)

# Data Storage
# In-memory list to store registered users
users = []

# List of fields required for user signup
required_fields = ["name", "age", "email", "password", "username", "number"]

# Routes
@app.route("/signup", methods=["POST"])
def create_users():
    """
    Handle user signup/registration.

    Expects JSON body with: name, age, email, password, username, number
    Returns: List of all registered users on success, or error message if fields are missing
    """
    # Get the JSON data from the request body
    new_user = request.json

    # Validate that all required fields are present
    missing_fields = []
    for field in required_fields:
        if field not in new_user:
            missing_fields.append(field)

    # If any fields are missing, return an error response
    if missing_fields:
        return jsonify({"error": f"{missing_fields} missing"})

    # Add the new user to the users list
    users.append(new_user)

    # Return all users as JSON response
    return jsonify(users)


# App Entry Point
if __name__ == '__main__':
    # Run the Flask development server with debug mode enabled
    app.run(debug=True)
