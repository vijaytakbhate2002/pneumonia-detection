import streamlit as st
import cv2
import numpy as np

# Create a Streamlit app
st.title("Image Crop App")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded image file as bytes
    image_bytes = uploaded_file.read()

    # Convert the image bytes to a NumPy array
    image_np = np.frombuffer(image_bytes, np.uint8)

    # Decode the image using OpenCV
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    # Display the original image
    st.image(img, caption="Original Image", use_column_width=True)

    # Allow the user to specify the cropping coordinates
    crop_x = st.slider("Crop X-coordinate", 0, img.shape[1], img.shape[1] // 4)
    crop_y = st.slider("Crop Y-coordinate", 0, img.shape[0], img.shape[0] // 4)
    crop_width = st.slider("Crop Width", 1, img.shape[1] - crop_x, img.shape[1] // 2)
    crop_height = st.slider("Crop Height", 1, img.shape[0] - crop_y, img.shape[0] // 2)

    # Crop the image based on user-defined coordinates
    cropped_img = img[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]

    # Display the cropped image
    st.image(cropped_img, caption="Cropped Image", use_column_width=True)
