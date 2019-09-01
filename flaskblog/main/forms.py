from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class SurveyForm(FlaskForm):
	question1 = RadioField('1. I always feel unhappy.', choices=[(5,'Agree'),(4,'Somewhat Agree'),(3,'Neutral'),(2,'Somewhat Disagree'),(1,'Disagree')])
	question2 = RadioField('2. I always can\'t sleep well.', choices=[(5,'Agree'),(4,'Somewhat Agree'),(3,'Neutral'),(2,'Somewhat Disagree'),(1,'Disagree')])
	question3 = RadioField('Question 3', choices=[(5,'Agree'),(4,'Somewhat Agree'),(3,'Neutral'),(2,'Somewhat Disagree'),(1,'Disagree')])
	question4 = RadioField('Question 4', choices=[(5,'Agree'),(4,'Somewhat Agree'),(3,'Neutral'),(2,'Somewhat Disagree'),(1,'Disagree')])
	question5 = RadioField('Question 5', choices=[(5,'Agree'),(4,'Somewhat Agree'),(3,'Neutral'),(2,'Somewhat Disagree'),(1,'Disagree')])
	submit = SubmitField('Submit')
