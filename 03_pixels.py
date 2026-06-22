import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
import os

def readAndWriteSinglePixel():
    root = os.getcwd()
    path = os.path.join(root, "dino.png")
    img = cv.imread(path)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    readAndWriteSinglePixel()