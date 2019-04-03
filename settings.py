
#from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required

db = SQLAlchemy()

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost/test"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True