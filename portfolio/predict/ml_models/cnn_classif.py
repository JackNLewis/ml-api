import numpy as np 
import tensorflow as tf 
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
from django.conf import settings
import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

IMG_SIZE = 64
class_names = ['Buildings','Forest','Glacier','Mountain','Sea','Street']

class Cnn():

    def __init__(self):
        path = os.path.join(settings.MODELS, 'cnn_model.h5')
        self.model = models.load_model(path)
        print("loaded model")

    def predict(self):
        path = os.path.join(settings.MODELS, 'mountain.jpg')
        img = plt.imread(path)
        img = tf.image.resize(img,[IMG_SIZE,IMG_SIZE]).numpy()
        img = img/255
        img = np.expand_dims(img, axis=0)
        y_hat = self.model(img)[0].numpy()
        index = np.argmax(y_hat)
        print('Predict: ' +  class_names[index])
        return class_names[index]

 # img = plt.imread('./mountain.jpg')
        # img = tf.image.resize(img,[IMG_SIZE,IMG_SIZE]).numpy()
        # img = img/255
        # img = np.expand_dims(img, axis=0)
        # y_hat = self.model(img)[0].numpy()
        # index = np.argmax(y_hat)
        # print('Predict: ' +  class_names[index])
# IMG_SIZE = 64
# class_names = ['Buildings','Forest','Glacier','Mountain','Sea','Street']

# model = models.load_model('./cnn_model.h5')

# img = plt.imread('./mountain.jpg')
# img = tf.image.resize(img,[IMG_SIZE,IMG_SIZE]).numpy()
# img = img/255
# img = np.expand_dims(img, axis=0)

# y_hat = model(img)[0].numpy()
# index = np.argmax(y_hat)
# print('Predict: ' +  class_names[index])