from flask import jsonify, request, Blueprint
from database.models import User
from database.db import db
from flask_jwt_extended import jwt_required

profile = Blueprint('profile', __name__)