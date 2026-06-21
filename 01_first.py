import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np 

def readImage():
    root = os.getcwd()
    path = os.path.join(root, "dino.png")
    img = cv.imread(path)
    cv.imshow("hello", img)
    cv.waitKey(0)
    print(img.shape)

def writeImage():
    root = os.getcwd()
    path = os.path.join(root, "dino.png")
    img = cv.imread(path)
    outPath = os.path.join(root, "dinoCP.png")
    cv.imwrite(outPath, img)


if __name__ == "__main__":
    readImage()
    # writeImage()
    