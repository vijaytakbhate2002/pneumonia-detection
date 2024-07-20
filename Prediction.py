import cv2 as cv
import numpy as np
from Data_ingest import GetImg
from Data_process import ProcessImg
import warnings
from keras.models import load_model
warnings.filterwarnings('ignore')

class Predict:
    LABELS = {0:"Bacterial pneumonia", 1:"Normal", 2:"Virus pneumonia"}
    model = load_model("static\\CNN_32_32_1_ASA.h5")

    def __init__(self,arr:np.ndarray)-> None:
        """ Args: np.ndarray
            Return: None"""
        self.arr = arr

    def predict(self)-> np.ndarray:
        """ Args: None 
            Return: str (bacterial, virul or normal)"""
        res = self.model.predict(self.arr)
        res = np.argmax(res)
        return self.LABELS[res]

