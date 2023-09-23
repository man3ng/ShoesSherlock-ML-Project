import os
import numpy as np
import matplotlib.pyplot as plt

import tensorflow.keras as keras
import tensorflow as tf

from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)

import h5py
from keras.models import load_model

#change directory to your own workspace
loaded_model = load_model("/workspaces/shoesherlock-Tri-Kevin/shoesherlockv2-5-2.h5")


def shoes_prediction(user_img):
    img = tf.keras.preprocessing.image.load_img(user_img, target_size = (224,224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.array([img_array])
    brand_predict = ""
    prediction = loaded_model.predict(img_array)
    #print(prediction) #to see the confidence
    if np.argmax(prediction, axis = 1)[0] == 1:
        brand_predict = "Adidas"
    else:
        brand_predict = "Nike"
    return brand_predict

