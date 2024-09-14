import os

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

classes = ['apple',
          'banana',  
          'beetroot',
          'bell pepper',
          'cabbage',
          'capsicum',
          'carrot',
          'cauliflower',
          'chilli pepper',
          'corn',
          'cucumber',
          'eggplant',
          'garlic',
          'ginger',
          'grapes',
          'jalepeno',
          'kiwi',
          'lemon',
          'lettuce',
          'mango',
          'onion',
          'orange',
          'paprika',
          'pear',
          'peas',
          'pineapple',
          'pomegranate',
          'potato',
          'raddish',
          'soy beans',
          'spinach',
          'sweetcorn',
          'sweetpotato',
          'tomato',
          'turnip',
          'watermelon']

# Load the model
model = keras.models.load_model("model.keras")



def preprocess_image(img    ):
    # Resize the image
    img = img.resize((180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array


def inferencing(img_array):
    # Predict the image
    predictions = model.predict(img_array)
    fruit = classes[np.argmax(predictions[0])]
    return fruit

if __name__ == "__main__":
    # Load the image
    img = PIL.Image.open("test.jpg")
    img_array = preprocess_image(img)
    fruit = inferencing(img_array)

    print(f"Predicted fruit is: {fruit}")


