import cv2
import sys

# 1. Initialize the CSRT Tracker (The best overall tracker in OpenCV)
# Note: For older OpenCV versions, you might need: cv2.legacy.TrackerCSRT_create()
tracker = cv2.TrackerCSRT_create()

# 2. Start the Webcam video capture (0 is usually the built-in webcam)
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Could not open webcam.")
    sys.exit()

# Read the very first frame
ok, frame = video.read()
if not ok:
    print('Cannot read video file/stream')
    sys.exit()

# 3. Use OpenCV's built-in UI to let the user select the object with a mouse
# Press SPACE/ENTER after drawing the box, or 'c' to cancel
bbox = cv2.selectROI("Tracking Window", frame, fromCenter=False, showCrosshair=False)

# 4. Initialize the tracker with the selected coordinates on the first frame
tracker.init(frame, bbox)

while True:
    # Read a new frame from the webcam
    ok, frame = video.read()
    if not ok:
        break
        
    # Start timer to calculate FPS (Frames Per Second)
    timer = cv2.getTickCount()

    # 5. Update the tracker with the current frame
    # 'ok' will be True if the object is successfully tracked, False if lost
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # 6. If the tracking is successful, draw the box around the object
    if ok:
        # Tracking success: bbox contains (x, y, width, height)
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
    else :
        # Tracking failure: object went off-screen or got hidden
        cv2.putText(frame, "Tracking failure detected", (100, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # # Display Tracker type and FPS on the screen
    # cv2.putText(frame, "CSRT Tracker", (100, 20), 
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    # cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), 
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    # Display result window
    
    cv2.imshow("Tracking Window", frame)

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()