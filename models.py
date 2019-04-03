from settings import db




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







