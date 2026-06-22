import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def callback(x):
    pass

def cannyEdgeDetection():
    root = os.getcwd()
    path = os.path.join(root, "dino.png")
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)

    winName = "Canny Edge Detection"

    cv.namedWindow(winName)
    cv.createTrackbar("threshold1", winName, 100, 255, callback)
    cv.createTrackbar("threshold2", winName, 200, 255, callback)

    while True:
        if cv.waitKey(1) == ord("q"):
            break

        threshold1 = cv.getTrackbarPos("threshold1", winName)
        threshold2 = cv.getTrackbarPos("threshold2", winName)

        if threshold1 == 0:
            threshold1 = 1
        if threshold2 == 0:
            threshold2 = 1

        edges = cv.Canny(img, threshold1, threshold2)

        cv.imshow(winName, edges)

    cv.destroyAllWindows()


if __name__ == "__main__":
    cannyEdgeDetection()