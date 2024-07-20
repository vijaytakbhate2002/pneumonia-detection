import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
import io
from pipeline import run_pipe
import cv2 as cv
from config import config

st.header("Pneumonia Detection", divider='rainbow')
st.sidebar.header("Select an Image", divider='rainbow')
selected_image = st.sidebar.radio("Choose an image:", config.INPUT_METHOD)

class ImageSelctor:
    """
        Args: selected_image = string imput
        Rturns: file like object of uploaded image

        Description : This class takes selected_image as input and based on this decides which image 
        should load to uploaded_file variable;
        If slected_image from (bact_img, virus_img, normal_img);
        then it will select preloaded image as per users instructions and converts image object into
        file like object with 'image_to_fil_like' function.
        If selected_image  == user_input then it will take input from UI 
        It returns file like object 
    """
    bact_img = Image.open(config.TEST_IMG_BACTERIA)
    virus_img = Image.open(config.TEST_IMG_VIRUS)
    normal_img = Image.open(config.TEST_IMG_NORMAL)

    def __init__(self):
        self.uploaded_file = None

    def image_to_file_like(self, image, format='JPEG'):
        buffer = BytesIO()
        image.save(buffer, format=format)
        buffer.seek(0)  
        return buffer

    def file_selector(self, selected_image:str):
       
        if selected_image == config.INPUT_METHOD[1]:
            st.sidebar.image(self.bact_img, caption="bacterial X-ray")
            uploaded_file = self.image_to_file_like(self.bact_img)

        elif selected_image == config.INPUT_METHOD[2]:
            st.sidebar.image(self.virus_img, caption="virus X-ray")
            uploaded_file = self.image_to_file_like(self.virus_img)

        elif selected_image == config.INPUT_METHOD[3]:
            st.sidebar.image(self.normal_img, caption="normal X-ray")
            uploaded_file = self.image_to_file_like(self.normal_img)
            
        elif selected_image == config.INPUT_METHOD[0]:
            uploaded_file = st.file_uploader("Drop chest X-ray", type=["jpg", "png", "jpeg"])
        return uploaded_file

file_uploader = ImageSelctor()
uploaded_file = file_uploader.file_selector(selected_image=selected_image)

def reshape_img(img:np.ndarray,dims:tuple)-> np.ndarray:
    """"Args: np.ndarray (image)
        Return: np.ndarray (reshaped image)"""
    reshaped_ = img[dims[1]:dims[1]+dims[3], dims[0]:dims[0]+dims[2]]
    return reshaped_

if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes))
    image_np = np.array(image)
    show_img = cv.resize(image_np,(200,200))
    flag = False
    
    with st.expander("Crop image"):
        x = st.slider("seletct x: ",min_value=0, max_value=200, value=0)
        y = st.slider("seletct y: ",min_value=0, max_value=200, value=0)
        w = st.slider("seletct w: ",min_value=1, max_value=200, value=200)
        h = st.slider("seletct h: ",min_value=1, max_value=200, value=200)
        dims = (x,y,w,h)
        reshaped_img = reshape_img(show_img,dims=dims)
        flag = True
    if flag:
        processed_img = reshaped_img
    else:
        reshape_img = image_np

    st.image(reshaped_img, caption="Uploaded Image", use_column_width=False)
    predicted = run_pipe(reshaped_img)
    if predicted == "Normal":
        st.success(predicted)
    else:
        st.error(predicted)



