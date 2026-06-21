import numpy as np 
import cv2 as cv
import os 

def videoFromWebCam():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        exit()
    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow("webcam", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()

def writeVideoToFile():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    root = os.getcwd()
    outpath = os.path.join(root, "outvideo.mp4")

    out = cv.VideoWriter(outpath, fourcc, 40,(640,480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow("webcam", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()





if __name__ == "__main__":
    # videoFromWebCam()
    writeVideoToFile()