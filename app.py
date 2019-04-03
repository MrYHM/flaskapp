from flask import Flask
from forms import Add_dpm,Add_user
from models import Department,User
from flask import render_template, request,redirect, url_for, flash
from settings import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = "asgSfsf3Xd8ffy]fw8vfd0zbvssqwertsd4sdwe"

db.init_app(app)
#db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add_dpm',methods=["POST","GET"])
def add_dpm():
    return render_template('add_dpm.html')

@app.route('/addaction',methods=["POST"])
def addaction():
    dpmname = request.form.get("dpmname")
    dpmnames = Department(dpmname=dpmname)
    db.session.add(dpmnames)
    db.session.commit()

    return redirect(url_for('show_all'))

@app.route('/add_user',methods=["POST","GET"])
def add_user():
    user = Add_user()
    if user.validate_on_submit():
        username = user.username.data
        dpm = user.department.data
        password = user.password.data
        usercount = User.query.filter_by(username=username).count()
        if usercount == 0:
            newuser = User(username=username, department=dpm, password=password)
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for('show_all'))
        else:
            error_msg = (u'用户名重复，请换一个！')
            flash(error_msg)
    else:
        message = user.errors
        flash(message)

    return render_template('add_user.html', user=user)


@app.route('/show',methods=["POST","GET"])
def show_all():
    user = User.query.all()
    dpm = Department.query.all()
    db.session.commit()

    return render_template('show.html',users = user, dpms = dpm)

@app.route('/user/<int:id>/delete')
def user_delete(id):
    try:
        userinfo = User.query.get(id)
        db.session.delete(userinfo)
        db.session.commit()
    except:
        flash(u'删除失败，请联系管理员！')

    return redirect(url_for('show_all'))

@app.route('/user/<int:id>/management')
def user_manage(id):
    userinfo = User.query.get(id)

    return render_template('user_update.html',user = userinfo)

@app.route('/user/<int:id>/user_update',methods=["POST"])
def user_update(id):
    username = request.form.get("username")
    password = request.form.get("password")
    department = request.form.get("department")
    userinfo = User.query.get(id)
    userinfo.username = username
    userinfo.password = password
    userinfo.department = department
    db.session.commit()

    return redirect(url_for('show_all'))

@app.route('/dpm/<int:id>/management')
def dpm_manage(id):
    dpminfo = Department.query.get(id)

    return render_template('dpm_update.html',dpm = dpminfo)

@app.route('/dpm/<int:id>/dpm_update',methods=["POST"])
def dpm_update(id):
    department = request.form.get("dpmname")
    dpminfo = Department.query.get(id)
    dpminfo.dpmname = department
    db.session.commit()

    return redirect(url_for('show_all'))

@app.route('/dpm/<int:id>/delete')
def dpm_delete(id):
    try:
        dpminfo = Department.query.get(id)
        db.session.delete(dpminfo)
        db.session.commit()
    except:
        flash(u'删除失败，请联系管理员！')

    return redirect(url_for('show_all'))




if __name__ == '__main__':
    print(app.url_map)
    app.run()
    print(app.url_map)
