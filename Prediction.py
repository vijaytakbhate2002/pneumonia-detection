import cv2 as cv
import numpy as np
from Data_ingest import GetImg
from Data_process import ProcessImg
from static.pneumonia_model import model
from tensorflow.keras.models import Model
import warnings
warnings.filterwarnings('ignore')

class Predict:
    LABELS = {0:"Bacterial pneumonia", 1:"Normal", 2:"Virus pneumonia"}

    def __init__(self,arr:np.ndarray, model:Model)-> None:
        """ Args: np.ndarray
            Return: None"""
        self.arr = arr
        self.model = model

    def predict(self)-> np.ndarray:
        """ Args: None 
            Return: str (bacterial, virul or normal)"""
        res = self.model.predict(self.arr)
        res = np.argmax(res)
        return self.LABELS[res]

