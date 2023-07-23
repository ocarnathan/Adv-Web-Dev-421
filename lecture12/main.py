import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__)) 
#__file__ refers to main.py
# abspath -> absolute path -> provides the full directory path

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

class Student(db.Model):
    __tablename__="students"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    grade = db.Column(db.Integer)
    attendance = db.Column(db.Integer)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.attendance
    
    def __repr__(self):
        return f"Student {self.name} got {self.grade} on midterm exam, attendance = {self.attendance}" # f is for string formatting