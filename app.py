from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
required_fields = ["name", "age", "email", "password", "username", "number"]


@app.route("/signup", methods=["POST"])
def create_users():
    new_user = request.json

    missing_fields = []
    for field in required_fields:
        if field not in new_user:
            missing_fields.append(field)

    if missing_fields:
        return jsonify({"error": f"{missing_fields} missing"})

    users.append(new_user)
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
