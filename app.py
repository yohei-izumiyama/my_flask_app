from flask import Flask, request, jsonify, render_template, redirect, url_for
from models.models import User, Current
from flask_sqlalchemy import SQLAlchemy
from db import db
    
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://myuser:mypassword@db:3306/mydatabase?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit_user')
def submit_user():
    return render_template("create_user.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('submit_user'))

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/master/<room_id>', methods=["GET"])
def master(room_id):
    current_week = Current.query.get(room_id).week
    return render_template("master.html", room_id=room_id, current_week=current_week)

@app.route('/update_week/<room_id>', methods=["GET", "PUT"])
def update_week(room_id):  
    # get current week on room
    current_week = Current.query.get(room_id).week
    next_week = current_week + 1
    
    # update room
    room_to_update = Current.query.get(room_id)
    if room_to_update:
        room_to_update.week = next_week
        
    db.session.commit()
    # redirect to master view
    return redirect(url_for("master", room_id=room_id))

@app.route('/reset_week/<room_id>', methods=["GET", "PUT"])
def reset_week(room_id):  
    # get current week on room
    room_to_update = Current.query.get(room_id)
    if room_to_update:
        room_to_update.week = 1
        
    db.session.commit()
    # redirect to master view
    return redirect(url_for("master", room_id=room_id))


