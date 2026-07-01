from ultralytics import YOLO
import cv2 as cv
import cvzone

cam = cv.VideoCapture(0)
model = YOLO('yolov8n.pt')

while True:
    ret, frame = cam.read()
    results = model(frame, stream=True)
    # setting boxes
    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cls = int(box.cls[0])
            cvzone.putTextRect(frame, f'{model.names[cls]}', (x1, y1), scale=1, thickness=1)
    cv.imshow("image", frame)
    cv.waitKey(1)