from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class WidgetForm(FlaskForm):
    color = StringField("color")
    submit = SubmitField("Submit")
