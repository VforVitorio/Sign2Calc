"""
Sign2Calc - Gesture-based calculator
Main entry point for the application
"""

import cv2
from config import (
    CAMERA_INDEX,
    CAM_WIDTH,
    CAM_HEIGHT,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    WINDOW_NAME,
    QUIT_KEY,
    BUTTON_VALUES
)
from ui import Button
from calculator import CalculatorLogic
from gesture import HandDetector, GestureRecognizer


def create_buttons():
    """
    Create all calculator buttons based on BUTTON_VALUES layout

    Returns:
        list: List of Button instances
    """
    buttonlist = []
    for y in range(5):
        for x in range(4):
            # First row only has 2 buttons (C and <)
            if y == 0 and x >= 2:
                break

            xpos = int(DISPLAY_WIDTH - 500 + x * 100)
            ypos = int(DISPLAY_HEIGHT * 0.15 + y * 100)

            # First row special case: second button needs to be shifted
            if y == 0 and x == 1:
                xpos += 100

            if y == 0:
                # First row has wider buttons
                width = 200
                buttonlist.append(
                    Button((xpos, ypos), width, 100, BUTTON_VALUES[y][x]))
            else:
                buttonlist.append(
                    Button((xpos, ypos), 100, 100, BUTTON_VALUES[y][x]))

    return buttonlist


def main():
    """Main application loop"""
    # Initialize camera
    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(3, CAM_WIDTH)
    cap.set(4, CAM_HEIGHT)

    # Create fullscreen window
    cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Initialize calculator and buttons
    calculator = CalculatorLogic()
    buttons = create_buttons()

    # Initialize gesture detection
    hand_detector = HandDetector(
        max_hands=1, detection_confidence=0.7, tracking_confidence=0.7)
    gesture_recognizer = GestureRecognizer()

    print(f"Sign2Calc started - Press '{QUIT_KEY}' to quit")

    # Main loop
    while True:
        success, img = cap.read()

        if not success:
            print("Failed to read from camera")
            break

        # Resize camera feed to fullscreen resolution BEFORE drawing UI elements
        img = cv2.resize(img, (DISPLAY_WIDTH, DISPLAY_HEIGHT),
                         interpolation=cv2.INTER_LINEAR)

        # Detect hands and draw landmarks
        img = hand_detector.find_hands(img, draw=True)

        # Get hand landmarks
        landmark_list = hand_detector.find_position(img)

        # Recognize gesture if hand detected
        current_gesture = None
        if landmark_list:
            current_gesture = gesture_recognizer.recognize(landmark_list)

            # Display detected gesture for debugging
            if current_gesture:
                gesture_desc = gesture_recognizer.get_gesture_description(
                    current_gesture)
                gesture_text = f"{current_gesture}: {gesture_desc}"
                cv2.putText(img, gesture_text, (50, 50),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Display area for operation string
        operation_x = int(DISPLAY_WIDTH - 500)
        operation_y = int(DISPLAY_HEIGHT * 0.05)

        cv2.rectangle(img, (operation_x, operation_y), (operation_x + 400, operation_y + 120),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, (operation_x, operation_y), (operation_x + 400, operation_y + 120),
                      (50, 50, 50), 3)

        # Draw all calculator buttons
        for button in buttons:
            button.draw(img)

        # Display operation string
        cv2.putText(img, calculator.get_operation(), (operation_x + 10, operation_y + 75),
                    cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

        cv2.imshow(WINDOW_NAME, img)

        # Check for quit key
        key = cv2.waitKey(1)
        if key == ord(QUIT_KEY):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Sign2Calc closed")


if __name__ == "__main__":
    main()
