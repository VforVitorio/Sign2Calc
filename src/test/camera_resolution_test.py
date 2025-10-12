"""
camera_resolution_test.py
Simple script to check the actual resolution of your webcam
"""

import cv2

# Open webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

# Try to read one frame
success, frame = cap.read()

if success:
    # Get actual dimensions
    height, width = frame.shape[:2]

    print("=" * 50)
    print(f"Camera Resolution: {width} x {height}")
    print("=" * 50)

    # Show the frame with resolution info
    cv2.putText(frame, f"Resolution: {width}x{height}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Camera Resolution Test', frame)
    print("Press any key to close the window...")
    cv2.waitKey(0)
else:
    print("Error: Cannot read frame from camera")

# Release resources
cap.release()
cv2.destroyAllWindows()
