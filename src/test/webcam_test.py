import cv2

# corresponding to /dev/video2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open capture")
    exit(1)

# These two lines must be changed with the webcam resolution obtained from src/test/camera_resolution_test.py
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Video capture started at {}x{}".format(
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break
    cv2.imshow("Video2 Full HD", frame)
    # Escape
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
