import os
import sys
sys.path.append(__file__.split('\\')[:-2])

# Paths
ROOT_PATH = '\\'.join(__file__.split('\\')[:-2])
IMGS_FOLDER_PATH = os.path.join(ROOT_PATH, 'images')
MODEL_PATH = os.path.join(ROOT_PATH, 'model\\CNN_32_32_1_ASA.h5')
TEST_IMG_BACTERIA = os.path.join(IMGS_FOLDER_PATH, "bacteria\\person100_bacteria_475 (1).jpg")
TEST_IMG_VIRUS = os.path.join(IMGS_FOLDER_PATH, "virus\\person1635_virus_2831.jpg")
TEST_IMG_NORMAL = os.path.join(IMGS_FOLDER_PATH, "normal\\IM-0001-0001.jpg")

INPUT_METHOD = ("User input", "bacterial image", "virus image", "normal image")