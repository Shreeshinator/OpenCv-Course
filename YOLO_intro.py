from ultralytics import YOLO
import cv2 as cv

model = YOLO("yolov8n.pt")
results = model("https://ultralytics.com/images/bus.jpg", show=True)
cv.waitKey(0)
# annotated = results[0].plot()

# cv.imshow("YOLO", annotated)
# cv.waitKey(0)
# cv.destroyAllWindows()