from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from diseaseprognosis.pipeline import PredictionPipeline

#initialize flask app
app = Flask(__name__)


# route to display the home page
# need to write html code with frontend developers
@app.route('/',methods=['GET'])  
def homePage():
    return render_template("index.html")


# route to train the pipeline online
@app.route('/train',methods=['GET'])  
def training():
    os.system("python main.py")
    return "Training Successful!"

# manual prediction
@app.route('/predict', methods=['GET'])
def pred():
    pred_user_data = [[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    obj = PredictionPipeline()
    predict = obj.predict(pred_user_data)
    return str(predict)


# prediction through postman
@app.route('/predict', methods=['POST'])
def pred_postman():
    # collect data in json format
    data = request.json['data']
    # convert collected values into 2D array
    new_data = [list(data.values())]
    # prediction
    obj = PredictionPipeline()
    output = obj.predict(new_data)[0]
    return str(output)


if __name__ == "__main__":
	app.run(debug=True)

    