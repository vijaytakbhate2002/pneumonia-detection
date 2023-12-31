import cv2 as cv
import numpy as np
from Data_ingest import GetImg
from static.pneumonia_model import model
import warnings
warnings.filterwarnings('ignore')

class ProcessImg:

    SHAPE = (32,32)
    def __init__(self,img:np.ndarray)-> None:
        """ Args: np.ndarray
            Return: None"""
        self.img = img
        self.img_shape = img.shape

    def process(self)-> np.ndarray:
        """ Args: None 
            Return: resized, gray, expand dims"""
        self.img = cv.resize(self.img,self.SHAPE)
        if len(self.img_shape) == 3:
            self.img = cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        self.img = np.expand_dims(np.expand_dims(self.img,axis=0),axis=-1)
        return self.img

if __name__ == "__main__":
    img = cv.imread("C:\\Users\\Vijay Takbhate\\Desktop\\Professional Workspace\\Pneumonia Detection\\images\\bacteria\\person100_bacteria_475 (1).jpg")
    a = ProcessImg(img).process()
    cv.imshow("Processed image",a)
    cv.waitKey(4000)

