"""
UI Components for Sign2Calc calculator
Contains reusable UI elements like buttons and displays
"""

import cv2
from config import (
    BUTTON_BG_COLOR,
    BUTTON_BORDER_COLOR,
    BUTTON_TEXT_COLOR,
    BUTTON_HIGHLIGHT_COLOR,
    BUTTON_HIGHLIGHT_BORDER,
    BORDER_THICKNESS,
    BORDER_THICK,
    FONT,
    FONT_SCALE,
    FONT_THICKNESS
)


class Button:
    """
    Represents a calculator button with position, size and value
    """

    def __init__(self, pos, width, height, value):
        """
        Constructor for initializing the button

        Args:
            pos: tuple (x, y) for top-left corner position
            width: button width in pixels
            height: button height in pixels
            value: Text to display on button (e.g. "7", "+")
        """
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
        self.highlighted = False

    def set_highlight(self, highlighted):
        """
        Set whether this button should be highlighted

        Args:
            highlighted: bool, True to highlight the button
        """
        self.highlighted = highlighted

    def draw(self, img):
        """
        Draw button on the image with background and border
        Highlights button if it's currently selected

        Args:
            img: OpenCV image array to draw on
        """
        # Choose colors based on highlight state
        bg_color = BUTTON_HIGHLIGHT_COLOR if self.highlighted else BUTTON_BG_COLOR
        border_color = BUTTON_HIGHLIGHT_BORDER if self.highlighted else BUTTON_BORDER_COLOR
        border_thickness = BORDER_THICK if self.highlighted else BORDER_THICKNESS

        # Draw the filled background
        cv2.rectangle(
            img,
            self.pos,
            (self.pos[0] + self.width, self.pos[1] + self.height),
            bg_color,
            cv2.FILLED
        )

        # Draw the borders
        cv2.rectangle(
            img,
            self.pos,
            (self.pos[0] + self.width, self.pos[1] + self.height),
            border_color,
            border_thickness
        )

        # Calculate text size to center it properly
        text_size = cv2.getTextSize(
            self.value, FONT, FONT_SCALE, FONT_THICKNESS)[0]
        text_x = self.pos[0] + (self.width - text_size[0]) // 2
        text_y = self.pos[1] + (self.height + text_size[1]) // 2

        # Draw text
        cv2.putText(
            img,
            self.value,
            (text_x, text_y),
            FONT,
            FONT_SCALE,
            BUTTON_TEXT_COLOR,
            FONT_THICKNESS
        )

    def get_value(self):
        """
        Get the value/label of this button

        Returns:
            str: The button's value
        """
        return self.value
