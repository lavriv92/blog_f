from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class TestForm(Form):
    name = TextField('name', validators=[DataRequired()])
