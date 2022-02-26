from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
from flask_cors import cross_origin


app = Flask(__name__,template_folder='templates')
model = pickle.load(open("dtrmodel.pkl", "rb"))

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/predictor',methods=["GET","POST"])
@cross_origin()
def home():
    return render_template('predictor.html')



@app.route("/predictor/predict",methods=["GET","POST"])
@cross_origin()
def predict():
    '''
    Here we will take the input from the index.html page values and then make prediction using our model
    '''
    if request.method=="POST":
        
        p=float(request.form["price"])
        k=int(request.form['kms'])
        t=request.form['Transmission']
        s=request.form['Seller']
        o=request.form['Owner']
        a=int(request.form['age'])
        
        
        if t=='Manual':
            z=1
        else:
            z=0
        
        if s=='Dealer':
            l=0
        else:
            l=1
        
        if o=='First':
            n=0
        elif o=='Second':
            n=1
        else:
            n=3
        
        predict = model.predict([[p,k,l,z,n,a]])[0]
        
        output=round(predict,3)
        
        return render_template('predictor.html',predict_price="Price of the Vehicle is ₹{} Lakhs".format(output))
    return render_template("predictor.html")


if __name__ == '__main__':      
    app.run(port='8080',debug=True)