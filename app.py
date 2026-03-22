from flask import Flask
from routes.auth import auth
from database.db import db
from database.models import User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)