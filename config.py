import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://myuser:mypassword@db:3306/mydatabase?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
