
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@mysql:3306/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.INTEGER, primary_key=True)
    dpmname = db.Column(db.String(80), unique=True)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=False)
    department = db.Column(db.INTEGER, db.ForeignKey('departments.id'))
    superuser = db.Column(db.Boolean, nullable=True, default=False)


db.create_all()




