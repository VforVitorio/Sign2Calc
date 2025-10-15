"""
UI Renderer module for Sign2Calc
Handles all drawing operations for the calculator interface
"""

import cv2
import numpy as np
from config import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    BG_COLOR,
    TITLE_TEXT,
    TITLE_X,
    TITLE_Y,
    TITLE_WIDTH,
    TITLE_HEIGHT,
    TITLE_FONT_SCALE,
    TITLE_FONT_THICKNESS,
    WEBCAM_X,
    WEBCAM_Y,
    WEBCAM_WIDTH,
    WEBCAM_HEIGHT,
    GESTURE_INDICATOR_X,
    GESTURE_INDICATOR_Y,
    GESTURE_INDICATOR_WIDTH,
    GESTURE_INDICATOR_HEIGHT,
    OPERATION_DISPLAY_X,
    OPERATION_DISPLAY_Y,
    OPERATION_DISPLAY_WIDTH,
    OPERATION_DISPLAY_HEIGHT,
    DEBUG_PANEL_X,
    DEBUG_PANEL_Y,
    DEBUG_PANEL_WIDTH,
    DEBUG_PANEL_HEIGHT,
    RESULT_DISPLAY_X,
    RESULT_DISPLAY_Y,
    RESULT_DISPLAY_WIDTH,
    RESULT_DISPLAY_HEIGHT,
    FPS_X,
    FPS_Y,
    QUIT_TEXT_X,
    QUIT_TEXT_Y,
    DISPLAY_BG_COLOR,
    DISPLAY_BORDER_COLOR,
    DISPLAY_TEXT_COLOR,
    DEBUG_TEXT_COLOR,
    FPS_COLOR,
    FONT,
    FONT_SCALE,
    FONT_THICKNESS,
    SMALL_FONT_SCALE,
    SMALL_FONT_THICKNESS,
    BORDER_THICKNESS,
    QUIT_KEY
)


class UIRenderer:
    """
    Manages all UI rendering operations for the calculator
    """

    def __init__(self):
        """
        Initialize UI renderer
        """
        pass

    def create_blank_canvas(self):
        """
        Create a blank canvas with background color

        Returns:
            numpy.ndarray: Blank image canvas
        """
        # Create blank image filled with background color
        canvas = np.ones((DISPLAY_HEIGHT, DISPLAY_WIDTH, 3), dtype=np.uint8)
        canvas[:] = BG_COLOR
        return canvas

    def draw_title(self, img):
        """
        Draw the title bar at the top

        Args:
            img: Image to draw on
        """
        # Draw title background
        cv2.rectangle(
            img,
            (TITLE_X, TITLE_Y),
            (TITLE_X + TITLE_WIDTH, TITLE_Y + TITLE_HEIGHT),
            DISPLAY_BG_COLOR,
            cv2.FILLED
        )

        # Draw title border
        cv2.rectangle(
            img,
            (TITLE_X, TITLE_Y),
            (TITLE_X + TITLE_WIDTH, TITLE_Y + TITLE_HEIGHT),
            DISPLAY_BORDER_COLOR,
            BORDER_THICKNESS
        )

        # Calculate centered text position
        text_size = cv2.getTextSize(
            TITLE_TEXT, FONT, TITLE_FONT_SCALE, TITLE_FONT_THICKNESS)[0]
        text_x = TITLE_X + (TITLE_WIDTH - text_size[0]) // 2
        text_y = TITLE_Y + (TITLE_HEIGHT + text_size[1]) // 2

        # Draw title text
        cv2.putText(
            img,
            TITLE_TEXT,
            (text_x, text_y),
            FONT,
            TITLE_FONT_SCALE,
            DISPLAY_TEXT_COLOR,
            TITLE_FONT_THICKNESS
        )

    def draw_webcam_area(self, img, webcam_frame):
        """
        Draw the webcam feed in the designated area

        Args:
            img: Canvas image
            webcam_frame: Webcam frame to display
        """
        # Resize webcam frame to fit area
        resized_frame = cv2.resize(
            webcam_frame,
            (WEBCAM_WIDTH, WEBCAM_HEIGHT),
            interpolation=cv2.INTER_LINEAR
        )

        # Place webcam frame on canvas
        img[WEBCAM_Y:WEBCAM_Y + WEBCAM_HEIGHT,
            WEBCAM_X:WEBCAM_X + WEBCAM_WIDTH] = resized_frame

        # Draw border around webcam area
        cv2.rectangle(
            img,
            (WEBCAM_X, WEBCAM_Y),
            (WEBCAM_X + WEBCAM_WIDTH, WEBCAM_Y + WEBCAM_HEIGHT),
            DISPLAY_BORDER_COLOR,
            BORDER_THICKNESS
        )

    def draw_gesture_indicator(self, img, gesture_name, gesture_description,
                                gesture_count=0, hold_threshold=1):
        """
        Draw the current detected gesture indicator with progress bar

        Args:
            img: Image to draw on
            gesture_name: Name of detected gesture (or None)
            gesture_description: Description of gesture action
            gesture_count: Current frame count holding the gesture
            hold_threshold: Frames needed to confirm gesture
        """
        # Draw background
        cv2.rectangle(
            img,
            (GESTURE_INDICATOR_X, GESTURE_INDICATOR_Y),
            (GESTURE_INDICATOR_X + GESTURE_INDICATOR_WIDTH,
             GESTURE_INDICATOR_Y + GESTURE_INDICATOR_HEIGHT),
            DISPLAY_BG_COLOR,
            cv2.FILLED
        )

        # Draw border
        cv2.rectangle(
            img,
            (GESTURE_INDICATOR_X, GESTURE_INDICATOR_Y),
            (GESTURE_INDICATOR_X + GESTURE_INDICATOR_WIDTH,
             GESTURE_INDICATOR_Y + GESTURE_INDICATOR_HEIGHT),
            DISPLAY_BORDER_COLOR,
            BORDER_THICKNESS
        )

        # Draw text and progress bar
        if gesture_name:
            text = f"{gesture_name}"
            cv2.putText(
                img,
                text,
                (GESTURE_INDICATOR_X + 10, GESTURE_INDICATOR_Y + 35),
                FONT,
                SMALL_FONT_SCALE,
                DISPLAY_TEXT_COLOR,
                SMALL_FONT_THICKNESS
            )

            # Draw progress bar
            progress_bar_x = GESTURE_INDICATOR_X + 10
            progress_bar_y = GESTURE_INDICATOR_Y + 55
            progress_bar_width = GESTURE_INDICATOR_WIDTH - 20
            progress_bar_height = 30

            # Draw progress bar background
            cv2.rectangle(
                img,
                (progress_bar_x, progress_bar_y),
                (progress_bar_x + progress_bar_width, progress_bar_y + progress_bar_height),
                DISPLAY_BORDER_COLOR,
                BORDER_THICKNESS
            )

            # Calculate and draw progress fill
            if hold_threshold > 0:
                progress = min(gesture_count / hold_threshold, 1.0)
                fill_width = int(progress_bar_width * progress)

                if fill_width > 0:
                    # Use green color for progress
                    progress_color = (100, 255, 100)  # Light green
                    cv2.rectangle(
                        img,
                        (progress_bar_x, progress_bar_y),
                        (progress_bar_x + fill_width, progress_bar_y + progress_bar_height),
                        progress_color,
                        cv2.FILLED
                    )

    def draw_buttons(self, img, buttons, highlighted_value=None):
        """
        Draw all calculator buttons

        Args:
            img: Image to draw on
            buttons: List of Button objects
            highlighted_value: Value to highlight (or None)
        """
        for button in buttons:
            # Set highlight if this button's value matches
            if highlighted_value and button.get_value() == highlighted_value:
                button.set_highlight(True)
            else:
                button.set_highlight(False)
            button.draw(img)

    def draw_operation_display(self, img, operation_text):
        """
        Draw the operation display showing current calculation

        Args:
            img: Image to draw on
            operation_text: Text to display
        """
        # Draw background
        cv2.rectangle(
            img,
            (OPERATION_DISPLAY_X, OPERATION_DISPLAY_Y),
            (OPERATION_DISPLAY_X + OPERATION_DISPLAY_WIDTH,
             OPERATION_DISPLAY_Y + OPERATION_DISPLAY_HEIGHT),
            DISPLAY_BG_COLOR,
            cv2.FILLED
        )

        # Draw border
        cv2.rectangle(
            img,
            (OPERATION_DISPLAY_X, OPERATION_DISPLAY_Y),
            (OPERATION_DISPLAY_X + OPERATION_DISPLAY_WIDTH,
             OPERATION_DISPLAY_Y + OPERATION_DISPLAY_HEIGHT),
            DISPLAY_BORDER_COLOR,
            BORDER_THICKNESS
        )

        # Draw label
        cv2.putText(
            img,
            f"OPERATION: {operation_text}",
            (OPERATION_DISPLAY_X + 15, OPERATION_DISPLAY_Y + 38),
            FONT,
            SMALL_FONT_SCALE,
            DISPLAY_TEXT_COLOR,
            SMALL_FONT_THICKNESS
        )

    def draw_debug_panel(self, img, debug_text):
        """
        Draw the debug panel with gesture detection info

        Args:
            img: Image to draw on
            debug_text: Debug information to display
        """
        # Draw background
        cv2.rectangle(
            img,
            (DEBUG_PANEL_X, DEBUG_PANEL_Y),
            (DEBUG_PANEL_X + DEBUG_PANEL_WIDTH,
             DEBUG_PANEL_Y + DEBUG_PANEL_HEIGHT),
            DISPLAY_BG_COLOR,
            cv2.FILLED
        )

        # Draw border
        cv2.rectangle(
            img,
            (DEBUG_PANEL_X, DEBUG_PANEL_Y),
            (DEBUG_PANEL_X + DEBUG_PANEL_WIDTH,
             DEBUG_PANEL_Y + DEBUG_PANEL_HEIGHT),
            DISPLAY_BORDER_COLOR,
            BORDER_THICKNESS
        )

        # Draw debug text
        cv2.putText(
            img,
            debug_text,
            (DEBUG_PANEL_X + 10, DEBUG_PANEL_Y + 30),
            FONT,
            SMALL_FONT_SCALE,
            DEBUG_TEXT_COLOR,
            SMALL_FONT_THICKNESS
        )

    def draw_result_display(self, img, result_text):
        """
        Draw the result display box

        Args:
            img: Image to draw on
            result_text: Result to display
        """
        # Draw background
        cv2.rectangle(
            img,
            (RESULT_DISPLAY_X, RESULT_DISPLAY_Y),
            (RESULT_DISPLAY_X + RESULT_DISPLAY_WIDTH,
             RESULT_DISPLAY_Y + RESULT_DISPLAY_HEIGHT),
            DISPLAY_BG_COLOR,
            cv2.FILLED
        )

        # Draw border
        cv2.rectangle(
            img,
            (RESULT_DISPLAY_X, RESULT_DISPLAY_Y),
            (RESULT_DISPLAY_X + RESULT_DISPLAY_WIDTH,
             RESULT_DISPLAY_Y + RESULT_DISPLAY_HEIGHT),
            DISPLAY_BORDER_COLOR,
            BORDER_THICKNESS
        )

        # Draw result text
        cv2.putText(
            img,
            f"RESULT: {result_text}",
            (RESULT_DISPLAY_X + 15, RESULT_DISPLAY_Y + 55),
            FONT,
            FONT_SCALE,
            DISPLAY_TEXT_COLOR,
            FONT_THICKNESS
        )

    def draw_fps(self, img, fps):
        """
        Draw FPS counter

        Args:
            img: Image to draw on
            fps: FPS value to display
        """
        cv2.putText(
            img,
            f"FPS: {fps}",
            (FPS_X, FPS_Y),
            FONT,
            SMALL_FONT_SCALE,
            FPS_COLOR,
            SMALL_FONT_THICKNESS
        )

    def draw_quit_instruction(self, img):
        """
        Draw quit instruction

        Args:
            img: Image to draw on
        """
        cv2.putText(
            img,
            f'Press "{QUIT_KEY}" to quit',
            (QUIT_TEXT_X, QUIT_TEXT_Y),
            FONT,
            SMALL_FONT_SCALE,
            DEBUG_TEXT_COLOR,
            SMALL_FONT_THICKNESS
        )

    def render_frame(self, webcam_frame, buttons, operation_text, result_text,
                     gesture_name, gesture_description, debug_text, fps,
                     gesture_count=0, hold_threshold=1, highlighted_value=None):
        """
        Render complete frame with all UI elements

        Args:
            webcam_frame: Webcam feed frame
            buttons: List of Button objects
            operation_text: Current operation string
            result_text: Current result string
            gesture_name: Detected gesture name (or None)
            gesture_description: Gesture description
            debug_text: Debug information
            fps: Current FPS
            gesture_count: Current frame count holding gesture
            hold_threshold: Frames needed to confirm gesture
            highlighted_value: Value to highlight on calculator (or None)

        Returns:
            numpy.ndarray: Complete rendered frame
        """
        # Create blank canvas
        img = self.create_blank_canvas()

        # Draw all UI elements
        self.draw_title(img)
        self.draw_webcam_area(img, webcam_frame)
        self.draw_gesture_indicator(img, gesture_name, gesture_description,
                                    gesture_count, hold_threshold)
        self.draw_buttons(img, buttons, highlighted_value)
        self.draw_operation_display(img, operation_text)
        self.draw_debug_panel(img, debug_text)
        self.draw_result_display(img, result_text)
        self.draw_fps(img, fps)
        self.draw_quit_instruction(img)

        return img
