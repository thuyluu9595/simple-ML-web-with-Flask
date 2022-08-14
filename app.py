from flask import Flask, render_template, request, session, url_for, redirect
import pickle
from forms import HousePricePredictorForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '6a75dcbc0976d995ebb55ede81bd7ebab4fc97bac3259f21d7314744a5ff794d'
model_name = 'ml-model/model.sav'
model = pickle.load(open(model_name, 'rb'))


# @app.route("/")
# def home():
#     return render_template('index.html')


@app.route("/", methods=['GET', 'POST'])
def prediction():
    form = HousePricePredictorForm()
    if form.validate_on_submit():
        house_age = form.house_age.data
        distance_ = form.distance.data
        number_stores = form.number_of_stores.data
        pred = round(model.predict([[house_age, distance_, number_stores]])[0])
        return render_template('index.html', form=form, value=pred)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
