from flask import Flask, jsonify, request
import bcrypt

app = Flask(__name__)

users = []
required_fields = ["email", "username", "password", "name", "number", "age"]

@app.route("/signup", methods=["POST"])
def create_users():
    new_user = request.json

    missing_fields = []
    for field in required_fields:
        if field not in new_user:
            missing_fields.append(field)

    if missing_fields:
        return jsonify({"error": f"{missing_fields} missing"})

    user_age = new_user.get('age')
    if not isinstance(user_age, int):
        return jsonify({"error": "Enter a valid Age"})

    uh_password = new_user.get('password')
    password_bytes = uh_password.encode("utf-8")
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password_bytes, salt)
    json_password = hashed_password.decode('utf-8')

    new_user['password'] = json_password

    users.append(new_user)
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
