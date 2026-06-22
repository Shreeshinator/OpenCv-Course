import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
import os

def convolution2d():
    root = os.getcwd()
    path = os.path.join(root, "dino.png")
    img = cv.imread(path)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    n = 100
    kernel = np.ones((n,n), np.float32)/(n*n)
    imgFilter = cv.filter2D(imgRGB, -1, kernel)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imgRGB)

    plt.subplot(122)
    plt.imshow(imgFilter)
    plt.show()

if __name__ == "__main__":
    convolution2d()