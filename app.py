from flask import Flask
from routes.auth import auth
from database.db import db
from database.models import User  # required for SQLAlchemy to register the model
from config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)