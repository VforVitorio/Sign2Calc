"""
This file contains the UI Components for the SIgn2Calc calculator
Contains reusable UI elements like buttons and displays
"""

import cv2
from config import (
    BUTTON_BG_COLOR,
    BUTTON_BORDER_COLOR,
    BUTTON_TEXT_COLOR,
    BORDER_THICKNESS,
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

    def draw(self, img):
        """
        Draw button on the image with background and border

        Args:
            img: OpenCV image array to draw on
        """

        # Draw the filled background

        cv2.rectangle(
            img,
            self.pos,
            (self.pos[0] + self.width, self.pos[1] + self.height),
            BUTTON_BG_COLOR,
            cv2.FILLED
        )

        # Draw the borders
        cv2.rectangle(
            img,
            self.pos,
            (self.pos[0] + self.width, self.pos[1] + self.height),
            BUTTON_BORDER_COLOR,
            BORDER_THICKNESS
        )

        # Calculate the text position (centered)
        text_x = self.pos[0] + self.width // 2 - 15
        text_y = self.pos[1] + self.width // 2 + 15

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
