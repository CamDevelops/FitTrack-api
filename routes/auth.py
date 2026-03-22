from flask import jsonify, request, Blueprint
import bcrypt

auth = Blueprint('auth', __name__)

registered_users = []
required_user_fields = ["email", "username", "password", "name", "number", "age"]

@auth.route("/signup", methods=["POST"])
def signup():
    user_data = request.json

    missing_fields = []
    for field in required_user_fields:
        if field not in user_data:
            missing_fields.append(field)
    if missing_fields:
        return jsonify({"error": f"{missing_fields} missing"})

    email = user_data.get('email')
    required_email_chars = ['@', '.']
    for char in required_email_chars:
        if char not in email:
            return jsonify({"error": "Please Enter a valid email."})

    age = user_data.get('age')
    if not isinstance(age, int):
        return jsonify({"error": "Enter a valid Age."})

    password = user_data.get('password')
    if len(password) <= 11:
        return jsonify({"error": "Password must be at least 12 characters long."})

    required_special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    if not any(char in password for char in required_special_chars):
        return jsonify({"error": "Password must contain a special Character !@#$%^&*"})

    if " " in password:
        return jsonify({"error": "Password can't have spaces in it."})

    try:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        hashed_password_str = hashed_password.decode('utf-8')

        user_data['password'] = hashed_password_str

        registered_users.append(user_data)
        return jsonify(registered_users)

    except ValueError:
        return jsonify({"error": "Invalid password format."})
    except Exception:
        return jsonify({"error": "Something went wrong. Please try again."})