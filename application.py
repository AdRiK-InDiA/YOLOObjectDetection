from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os 
import time
import cv2
import torch
from werkzeug.utils import secure_filename
import DataClean

application = Flask(__name__)
app=application

model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST']) # type: ignore
def predict_datapoint():
    	if request.method == "POST":
            image = request.files['file1']
            if image.filename == '':
                print("Image must have a file name")
                return render_template('index.html')
            DataClean.clean_static()
            filename = secure_filename(image.filename)
            image.save(os.path.join(os.getcwd(),'static','images',filename))
            name = filename
            path = os.path.join(os.getcwd(),'static','images',name)
            img = cv2.imread(path)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            # Inference
            results = model(img)
            time_ = time.strftime("%a %H %M %S %Y")
            name_ = time_.replace(' ','_')+name
            pwd = os.getcwd()
            PATH = os.path.join(pwd,'static','results',name_)
            results.save(save_dir=PATH)
            return render_template("results.html",filename=name_)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5500)