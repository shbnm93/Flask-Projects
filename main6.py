from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)



app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    
    breed = StringField("What Breed are you?")
    submit = SubmitField('submit')