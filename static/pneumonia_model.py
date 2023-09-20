from keras.models import load_model
model = load_model("C:\\Users\\Vijay Takbhate\\Desktop\\Professional Workspace\\Pneumonia Detection\\static\\CNN_32_32_1_ASA.h5")

if __name__ == "__main__":
    print(dir(model))