from Data_ingest import GetImg
from Data_process import ProcessImg
from Prediction import Predict
import numpy as np
import os
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

def run_pipe(img:np.ndarray)-> str:
    """ Args: np.ndarray
        Return: str (predicted output)"""
    processed_img = ProcessImg(img).process()
    res = Predict(processed_img).predict()
    return res

