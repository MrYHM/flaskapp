
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators

class Add_dpm(Form):
    dpmname = StringField("Department name", [validators.DataRequired("Please enter department name.")])
    submit = SubmitField("Add_dpm")

class Add_user(Form):
    username = StringField("Name",  [validators.DataRequired("Please enter your name.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    department = StringField("Department id", [validators.DataRequired("Please enter Department id.")])
    submit = SubmitField("Sumbit")