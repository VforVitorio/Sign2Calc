"""
Configuration file for Sign2Calc calculator
Contains all constants used throughout the application
"""
import cv2

# =============================================================================
# CAMERA CONFIGURATION
# =============================================================================
# Camera hardware capabilities (actual capture resolution)
CAM_WIDTH = 640
CAM_HEIGHT = 480

# Camera device index (0 is usually default camera)
CAMERA_INDEX = 0

# =============================================================================
# DISPLAY CONFIGURATION
# =============================================================================
# Target display resolution (fullscreen)
DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1080

# =============================================================================
# UI COLORS (BGR format for OpenCV)
# =============================================================================
# Button colors
BUTTON_BG_COLOR = (225, 225, 225)  # Light gray
BUTTON_BORDER_COLOR = (50, 50, 50)  # Dark gray
BUTTON_TEXT_COLOR = (50, 50, 50)   # Dark gray

# Button highlight colors (when gesture detects them)
BUTTON_HIGHLIGHT_COLOR = (100, 255, 100)  # Light green
BUTTON_HIGHLIGHT_BORDER = (0, 200, 0)     # Green

# Display area colors
DISPLAY_BG_COLOR = (225, 225, 225)
DISPLAY_BORDER_COLOR = (50, 50, 50)
DISPLAY_TEXT_COLOR = (50, 50, 50)

# Background color
BG_COLOR = (240, 240, 240)  # Very light gray

# Debug/info text colors
DEBUG_TEXT_COLOR = (50, 50, 50)
FPS_COLOR = (0, 150, 255)  # Orange color for better visibility

# =============================================================================
# UI LAYOUT
# =============================================================================
# Title
TITLE_TEXT = "Welcome to Sign2Calc!"
TITLE_X = DISPLAY_WIDTH // 2 - 300
TITLE_Y = 80
TITLE_WIDTH = 600
TITLE_HEIGHT = 60

# Webcam feed area
WEBCAM_X = 50
WEBCAM_Y = 160
WEBCAM_WIDTH = 1200
WEBCAM_HEIGHT = 700

# Gesture indicator (top right)
GESTURE_INDICATOR_X = 1280
GESTURE_INDICATOR_Y = 160
GESTURE_INDICATOR_WIDTH = 560
GESTURE_INDICATOR_HEIGHT = 100

# Calculator buttons area (right side)
CALC_X = 1280
CALC_Y = 270
BUTTON_WIDTH = 130
BUTTON_HEIGHT = 110
BUTTON_WIDE_WIDTH = 270  # For first row buttons (C and <)
BUTTON_SPACING = 10

# Result display (bottom, large - main display)
RESULT_DISPLAY_X = 50
RESULT_DISPLAY_Y = 900
RESULT_DISPLAY_WIDTH = 1820
RESULT_DISPLAY_HEIGHT = 80

# Debug panel (below result display)
DEBUG_PANEL_X = 50
DEBUG_PANEL_Y = 990
DEBUG_PANEL_WIDTH = 1300
DEBUG_PANEL_HEIGHT = 60

# Operation display (bottom right, smaller)
OPERATION_DISPLAY_X = 1370
OPERATION_DISPLAY_Y = 990
OPERATION_DISPLAY_WIDTH = 500
OPERATION_DISPLAY_HEIGHT = 60

# FPS display (top left corner)
FPS_X = 60
FPS_Y = 50

# Quit instruction (top right corner)
QUIT_TEXT_X = 1650
QUIT_TEXT_Y = 50

# =============================================================================
# CALCULATOR BUTTON LAYOUT
# =============================================================================
BUTTON_VALUES = [
    ['C', '<'],                    # Clear and backspace
    ['7', '8', '9', '/'],          # Numbers and division
    ['4', '5', '6', '*'],          # Numbers and multiplication
    ['1', '2', '3', '-'],          # Numbers and subtraction
    ['0', '.', '=', '+']           # Zero, decimal, equals, addition
]

# =============================================================================
# TEXT RENDERING
# =============================================================================
# Font configuration
FONT = cv2.FONT_HERSHEY_PLAIN
FONT_SCALE = 3
FONT_THICKNESS = 3

# Title font
TITLE_FONT_SCALE = 3
TITLE_FONT_THICKNESS = 3

# Small text (FPS, quit)
SMALL_FONT_SCALE = 1.5
SMALL_FONT_THICKNESS = 1

# Border thickness
BORDER_THICKNESS = 2
BORDER_THICK = 4  # For highlighted elements

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================
# Window name
WINDOW_NAME = "Calculator"

# Quit key
QUIT_KEY = 'q'
