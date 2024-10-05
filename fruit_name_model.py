import os

import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import misc_functions as mf

model = keras.models.load_model("model.keras")



def preprocess_image(img_path):
    img = PIL.Image.open(img_path)
    img = img.resize((180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array


def inferencing(img_array):
    # Predict the image
    fruit_index_name = mf.get_fruit_index_names()
    predictions = model.predict(img_array)
    fruit = fruit_index_name[np.argmax(predictions[0])]
    return fruit

def run_model(img_path):
    img_array = preprocess_image(img_path)
    fruit = inferencing(img_array)
    return fruit

def class_example_inference(img_array):
    predictions = model.predict(img_array)
    return predictions
    
if __name__ == "__main__":
    # Load the image
    img_path = r"./new_files/test.jpg"
    fruit = run_model(img_path)
    print(f"Predicted fruit is: {fruit}")
