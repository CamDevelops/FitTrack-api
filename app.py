from flask import Flask, send_from_directory
from routes.auth import auth
from database.db import db
from database.models import User  # required for SQLAlchemy to register the model
from config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

jwt = JWTManager(app)

CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), 'index.html')

@app.route('/src/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static', 'src'), filename)

if __name__ == '__main__':
    app.run(debug=True)