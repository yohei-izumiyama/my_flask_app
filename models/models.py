from flask_sqlalchemy import SQLAlchemy
from db import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
class Current(db.Model):
    __tablename__ = "current"
    room_id = db.Column(db.String(50), primary_key=True)
    week = db.Column(db.Integer(), nullable=False)

class Sheet(db.Model):
    __tablename__ = "sheet"
    room_id = db.Column(db.String(50), primary_key=True)
    room_name = db.Column(db.String(50), nullable=True)
    team_id = db.Column(db.String(50), primary_key=True)
    team_name = db.Column(db.String(50), nullable=True)
    role_id = db.Column(db.String(50), primary_key=True)
    role_name = db.Column(db.String(50), nullable=True)
    week = db.Column(db.Integer(), primary_key=True)
    order_this_week = db.Column(db.Integer(), nullable=True)