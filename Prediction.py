import numpy as np
import warnings
from keras.models import load_model
from config import config
warnings.filterwarnings('ignore')

class Predict:
    LABELS = {0:"Bacterial pneumonia", 1:"Normal", 2:"Virus pneumonia"}
    model = load_model(config.MODEL_PATH)

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

