import cv2 as cv
import os 
import numpy

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCorners=500,
                      qualityLevel=0.1,
                      minDistance=15,
                      blockSize=9)

image_filter = PREVIEW
alive = True

winName = 'Camer filters demo'
cv.namedWindow(winName, cv.WINDOW_NORMAL)
result=None

source = cv.VideoCapture(0)


if not source.isOpened():
    print("Could not open camera")
    exit()

while alive:
    ret, frame = source.read()
    if not ret:
        break
    frame = cv.flip(frame, flipCode=1)# horizontal

    if image_filter == PREVIEW:
        result=frame

    elif image_filter == CANNY:
        result= cv.Canny(frame, 80, 150)

    elif image_filter == BLUR:
        result = cv.blur(frame, (13, 13))
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x, y in numpy.float32(corners).reshape(-1, 2):
                cv.circle(result, (int(x), int(y)), 10, (255, 0, 0 ), 1)
        
        cv.imshow(winName, result)

    key = cv.waitKey(1) # esc key
    if key == ord('q'):
        alive = False
    elif key == ord('c') or key == ord('C'):
        image_filter = CANNY
    elif key == ord('b') or key == ord('B'):
        image_filter = BLUR
    elif key == ord('f') or key == ord('F'):
        image_filter = FEATURES
    elif key == ord('p') or key == ord('P'):
        image_filter = PREVIEW
    cv.imshow(winName, result)

source.release()
cv.destroyAllWindows()