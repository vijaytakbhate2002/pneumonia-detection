import cv2 as cv
import numpy as np
import warnings
warnings.filterwarnings('ignore')


class GetImg:
    def __init__(self,path:str)-> None:
        """path of image"""
        self.path = path

    def get_img(self)-> np.ndarray:
        """ Args: None 
            Return: image array (cv)"""
        img = cv.imread(self.path)
        return img

