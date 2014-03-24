from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(Form):
    email = TextField('name',
                      validators=[DataRequired()])
    text = TextAreaField('content',
                         validators=[DataRequired()])
