# imort required packages
from flask import Flask,render_template,request
import requests
import joblib
import numpy as np
import sklearn 
from sklearn.preprocessing import StandardScaler

# Create a flask object
app = Flask("House prediction")

# load ML model using joblib
model = joblib.load('regression_model.pkl')

# define the route (basically url)to which we need to send http request
# HTTP GET request method
@app.route('/', methods=['GET'])
def home():
    return render_template('base1.html')

# creating object for standard scaler
sc = StandardScaler()

# define the route for post method
# HTTP POST methods
@app.route('/predict', methods = ['POST'])
# define the predict function which is to going to predict the result from ml model based on the given values through html form
def predict():
    if request.method == 'POST':
        #Use request.form to get the data from html form through post method.
        #these all are nothing but features of our dataset(ml model)
        area = int(request.form['area'])
        rooms=int(request.form['rooms'])
        bathroom=int(request.form['bathroom'])
        floors=int(request.form['floors'])

        driveway=request.form['driveway']
        #driveway(feature) is categorised into yes and no, therefore we have done one-hot encoding on it while building model 
        if(driveway=='YES'):
            driveway = 1
        else:
            driveway=0
        

        #game_room(feature) is categorised into yes and no ,therefore we have done one-hot encoding on it while building model
        game_room=request.form['game_room']
        if game_room == 'YES':
            game_room = 1
        else:
            game_room = 0
        

        #celler(feature) is categorised into yes and no,therefore we have done one-hot encoding on it while building model
        cellar=request.form['cellar']
        if cellar == 'YES':
            cellar = 1
        else:
            cellar = 0

        gas=request.form['gas']
        if gas == 'YES':
            gas = 1
        else:
            gas = 0
        
        air=request.form['air']
        if air == 'YES':
            air = 1
        else:
            air = 0
        
        garage=request.form['garage']
        if garage == 'YES':
            garage = 1
        elif(garage == 'NO'):
            garage = 0
        else:
            garage = 2
            
        situation=request.form['situation']
        if situation == 'YES':
            situation = 1
        else:
            situation = 0
        
        prediction = model.predict([[area,rooms,bathroom,floors,driveway,game_room,cellar,gas,air,garage,situation]])
        output=round(prediction[0],2)
        #condition for invalid values
        if output<0:
            return render_template('base1.html',prediction_text='Sorry You Can Sell This House')
        else:
            return render_template('base1.html',prediction_text ='You Can Sell your house At $ {}'.format(output))
    else:
        return render_template('base1.html')

if __name__ == '__main__':
    #run method starts our web service
    # #Debug : as soon as I save anything in my structure, server should start again
    app.run(debug = True)
