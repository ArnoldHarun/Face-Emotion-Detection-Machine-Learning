import logging
import pandas as pd
import numpy as np 
import os
import seaborn as sn 
import tensorflow as tf 
from keras.models import Sequential 
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from zenml import step

TRAIN_DIR ='C:\Users\User\Desktop\Project\Data\train'
TEST_DIR='C:\Users\User\Desktop\Project\Data\test'

@step

def load_dataset(directory):
    image_paths = []
    labels=[]
    
    for label in os.listdir(directory):
        for filename in os.listdir(directory+label):
            image_path = os.path.join(directory, label, filename)
            image_paths.append(image_path)
            labels.append(label)
    print(label, 'Completed')
    return image_paths, labels
    