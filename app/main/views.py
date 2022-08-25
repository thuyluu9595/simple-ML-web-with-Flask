from flask import render_template, redirect, url_for
from . import main
from .forms import HousePricePredictorForm
from .. import db
import pickle


# model_name = '../ml-model/model.sav'
# model = pickle.load(open(model_name, 'rb'))

@main.route("/")
def home():
    return render_template('home.html')


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