from flask import jsonify, request, Blueprint
import bcrypt

auth = Blueprint('auth', __name__)

users = []
required_fields = ["email", "username", "password", "name", "number", "age"]

@auth.route("/signup", methods=["POST"])
def create_users():
    new_user = request.json

    missing_fields = []
    for field in required_fields:
        if field not in new_user:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"{missing_fields} missing"})

    user_email = new_user.get('email')
    email_requirements = ['@', '.']
    for char in email_requirements:
        if char not in user_email:
            return jsonify({"error": "Please Enter a valid email."})

    user_age = new_user.get('age')
    if not isinstance(user_age, int):
        return jsonify({"error": "Enter a valid Age."})

    user_password = new_user.get('password')
    if len(user_password) <= 11:
        return jsonify({"error": "Password must be at least 12 characters long."})

    special_char = ['!', '@', '#', '$', '%', '^', '&', '*']
    if not any(item in user_password for item in special_char):
        return jsonify({"error": "Password must contain a special Character !@#$%^&*"})

    if " " in user_password:
        return jsonify({"error": "Password can't have spaces in it."})

    try:
        password_bytes = user_password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        json_password = hashed_password.decode('utf-8')

        new_user['password'] = json_password

        users.append(new_user)
        return jsonify(users)

    except ValueError:
        return jsonify({"error": "Invalid password format."})
    except Exception:
        return jsonify({"error": "Something went wrong. Please try again."})