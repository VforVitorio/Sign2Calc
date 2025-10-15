"""
Sign2Calc - Gesture-based calculator
Main entry point for the application
"""

import cv2
import time
from config import (
    CAMERA_INDEX,
    CAM_WIDTH,
    CAM_HEIGHT,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    WINDOW_NAME,
    QUIT_KEY,
    BUTTON_VALUES,
    CALC_X,
    CALC_Y,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_WIDE_WIDTH,
    BUTTON_SPACING
)
from ui import Button, UIRenderer
from calculator import CalculatorLogic
from gesture import HandDetector, GestureRecognizer, GestureStabilizer, GestureMapper


def create_buttons():
    """
    Create all calculator buttons based on BUTTON_VALUES layout

    Returns:
        list: List of Button instances
    """
    buttonlist = []

    # Calculate row widths for centering
    row_0_width = 2 * BUTTON_WIDE_WIDTH + BUTTON_SPACING
    other_rows_width = 4 * BUTTON_WIDTH + 3 * BUTTON_SPACING

    # Calculate offset to center smaller rows
    center_offset = (row_0_width - other_rows_width) // 2

    for row in range(5):
        for col in range(len(BUTTON_VALUES[row])):
            value = BUTTON_VALUES[row][col]

            # Calculate position
            if row == 0:
                # First row: C and < buttons (wider)
                xpos = CALC_X + col * (BUTTON_WIDE_WIDTH + BUTTON_SPACING)
                width = BUTTON_WIDE_WIDTH
            else:
                # Other rows: regular buttons (centered)
                xpos = CALC_X + center_offset + col * (BUTTON_WIDTH + BUTTON_SPACING)
                width = BUTTON_WIDTH

            ypos = CALC_Y + row * (BUTTON_HEIGHT + BUTTON_SPACING)

            buttonlist.append(
                Button((xpos, ypos), width, BUTTON_HEIGHT, value))

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

    # Initialize calculator, gesture mapper and buttons
    calculator = CalculatorLogic()
    gesture_mapper = GestureMapper(calculator)
    buttons = create_buttons()

    # Initialize UI renderer
    ui_renderer = UIRenderer()

    # Initialize gesture detection
    hand_detector = HandDetector(
        max_hands=1, detection_confidence=0.7, tracking_confidence=0.7)
    gesture_recognizer = GestureRecognizer()
    gesture_stabilizer = GestureStabilizer(fps=30)

    # Configure stabilizer
    gesture_stabilizer.configure(
        hold_threshold_s=0.7,
        confirmation_cooldown_s=0.5,
        input_timeout_s=6.0
    )

    # FPS calculation
    prev_time = time.time()
    fps = 0

    print(f"Sign2Calc started - Press '{QUIT_KEY}' to quit")

    # Main loop
    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read from camera")
            break

        # Detect hands and draw landmarks on webcam frame
        frame = hand_detector.find_hands(frame, draw=True)
        landmark_list = hand_detector.find_position(frame)

        # Recognize and stabilize gesture
        detected_gesture = None
        if landmark_list:
            detected_gesture = gesture_recognizer.recognize(landmark_list)

        # Stabilize gesture
        result = gesture_stabilizer.update(detected_gesture)

        # Handle confirmed gesture
        if result['gesture']:
            gesture_mapper.handle(result['gesture'])
            gesture_desc = gesture_recognizer.get_gesture_description(
                result['gesture'])
            print(f"Confirmed: {result['gesture']} - {gesture_desc}")

        # Get stabilizer status for debug display
        status = gesture_stabilizer.get_status()

        # Prepare gesture info for display
        gesture_name = status['current_gesture']
        gesture_description = None
        if gesture_name:
            gesture_description = gesture_recognizer.get_gesture_description(
                gesture_name)

        # Prepare debug text
        debug_text = ""
        if status['last_confirmed']:
            desc = gesture_recognizer.get_gesture_description(
                status['last_confirmed'])
            debug_text = f"GESTURE: \"{status['last_confirmed']}\" -> {desc}"

        # Calculate FPS
        current_time = time.time()
        fps = int(1 / (current_time - prev_time)
                  ) if (current_time - prev_time) > 0 else 0
        prev_time = current_time

        # Get calculator state
        operation_text = calculator.get_operation() if calculator.get_operation() else "..."
        result = calculator.get_result()
        result_text = result if result is not None else "..."
        highlighted_value = calculator.get_highlighted_value()

        # Render complete UI frame
        img = ui_renderer.render_frame(
            webcam_frame=frame,
            buttons=buttons,
            operation_text=operation_text,
            result_text=result_text,
            gesture_name=gesture_name,
            gesture_description=gesture_description,
            debug_text=debug_text,
            fps=fps,
            gesture_count=status['gesture_count'],
            hold_threshold=gesture_stabilizer.hold_threshold_frames,
            highlighted_value=highlighted_value
        )

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
