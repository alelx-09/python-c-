"""
this script is used to preprocess data for a convolutional neural network 
using PIL and openCV 

"""


import numpy as np
import os 
import cv2
from PIL import Image



getpics= " path to pictures here "  #give complete path 
num_pics = len(os.listdir(getpics))
w,h= 150 # width and height of picture
chan= 3

data= np.ndarray([numpics, w,h,chan])

for i,pic in enumerate(os.listdir(getpics)):
    pics= Image.open(getpics + pic)
    pics = np.array(pics)
    pics= cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
    pics = cv2.resize(pics,(w,h))
    data[i,:,:,:]=np.reshape(-1,w,h,chan)
    x= data