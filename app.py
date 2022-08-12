from flask import Flask, render_template, request
import pickle

model_name = 'ml-model/model.sav'
app = Flask(__name__)
model = pickle.load(open(model_name,'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction", methods=['POST'])
def prediction():
    houseAge = int(request.form['house_age'])
    distance_ = int(request.form['distance'])
    numberStores = int(request.form['number_stores'])
    pred = round(model.predict([[houseAge,distance_,numberStores]])[0])
    return render_template('index.html', text=f'House price of unit are is {pred}')

if __name__ == "__main__":
    app.run()