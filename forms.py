from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class HousePricePredictorForm(FlaskForm):
    house_age = IntegerField('house_age', validators=[DataRequired()])
    distance = IntegerField('distance', validators=[DataRequired()])
    number_of_stores = IntegerField('number_of_stores', validators=[DataRequired()])
    submit = SubmitField('Predict')
