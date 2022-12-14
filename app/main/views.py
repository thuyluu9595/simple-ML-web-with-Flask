from flask import render_template, redirect, url_for
from . import main
from .forms import HousePricePredictorForm, SignUpForm
from ..models import User
from .. import db
from flask_login import login_user
import pickle


# model_name = '../ml-model/model.sav'
# model = pickle.load(open(model_name, 'rb'))


@main.route("/")
def home():
    return render_template('index.html')


@main.route("/signup", methods=['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        user = User(user_name=signup_form.user_name.data,
                    email=signup_form.email.data,
                    password=signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        return render_template('successful_signup.html')
    return render_template('signup.html', form=signup_form)

# @main.route("/prediction", methods=['GET', 'POST'])
# def prediction():
#     form = HousePricePredictorForm()
#     if form.validate_on_submit():
#         house_age = form.house_age.data
#         distance_ = form.distance.data
#         number_stores = form.number_of_stores.data
#         pred = round(model.predict([[house_age, distance_, number_stores]])[0])
#         return render_template('index.html', form=form, value=pred)
#     return render_template('index.html', form=form)
