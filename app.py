import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
import io
from pipeline import run_pipe
import cv2 as cv

st.title("Pneumonia Detection")

uploaded_file = st.file_uploader("Drop chest X-ray", type=["jpg", "png", "jpeg"])
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



