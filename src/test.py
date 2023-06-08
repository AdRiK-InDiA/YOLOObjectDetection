import os 
import time
import cv2
import torch

model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom

name = 'dogandmaster.jpg'

path = os.path.join(os.getcwd(),'images',name)
img = cv2.imread(path)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Inference
results = model(img)

time = time.strftime("%a %H %M %S %Y")

name_ = time.replace(' ','_')+name

pwd = os.getcwd()

PATH = os.path.join(pwd,'results',name_)

results.save(save_dir=PATH)

results.show()