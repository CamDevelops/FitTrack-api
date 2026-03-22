from flask import jsonify, request, Blueprint
from database.models import User
from database.db import db
from sqlalchemy.exc import IntegrityError
import bcrypt

auth = Blueprint('auth', __name__)

REQUIRED_USER_FIELDS = ["email", "username", "password", "name", "ph_number", "age"]

@auth.route("/signup", methods=["POST"])
def signup():
    user_data = request.json

    missing_fields = []
    for field in REQUIRED_USER_FIELDS:
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

        new_user = User(
            username=user_data.get('username'),
            password=user_data.get('password'),
            email=user_data.get('email'),
            name=user_data.get('name'),
            ph_number=user_data.get('ph_number'),
            age=user_data.get('age')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Account has been Created!"})

    except IntegrityError as e:
        db.session.rollback()
        error_message = str(e.orig)
        if "email" in error_message:
            return jsonify({"error": "That email is already registered."})
        if "username" in error_message:
            return jsonify({"error": "That username has been taken."})

    except ValueError:
        return jsonify({"error": "Invalid password format."})
    except Exception:
        return jsonify({"error": "Something went wrong. Please try again."})