from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped


class User(db.Model):
    """User account information"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(220), nullable=False)  # stored as hash
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    ph_number = db.Column(db.String(15))
    age = db.Column(db.Integer, nullable=False)


class Profile(db.Model):
    """User fitness profile - one profile per user"""
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    current_weight = db.Column(db.Float, nullable=False)
    goal_weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    fitness_goal = db.Column(db.String(50), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)

    # Foreign key relationship to User table
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    user: Mapped[User] = db.relationship(backref="profile")  # allows profile.user and user.profile