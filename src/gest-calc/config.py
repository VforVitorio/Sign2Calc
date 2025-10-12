"""
Configuration file for Sign2Calc calculator
Contains all constants used throughout the application
"""

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

# Display area colors
DISPLAY_BG_COLOR = (225, 225, 225)
DISPLAY_BORDER_COLOR = (50, 50, 50)
DISPLAY_TEXT_COLOR = (50, 50, 50)

# =============================================================================
# UI LAYOUT
# =============================================================================
# Button dimensions
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
BUTTON_WIDE_WIDTH = 200  # For first row buttons (C and <)

# Calculator position (right side of screen)
CALC_OFFSET_X = DISPLAY_WIDTH - 500
CALC_OFFSET_Y_START = int(DISPLAY_HEIGHT * 0.15)

# Display area for operation string
DISPLAY_OFFSET_X = DISPLAY_WIDTH - 500
DISPLAY_OFFSET_Y = int(DISPLAY_HEIGHT * 0.05)
DISPLAY_WIDTH_SIZE = 400
DISPLAY_HEIGHT_SIZE = 120

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
FONT = 0  # cv2.FONT_HERSHEY_PLAIN
FONT_SCALE = 3
FONT_THICKNESS = 3

# Border thickness
BORDER_THICKNESS = 3

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================
# Window name
WINDOW_NAME = "Calculator"

# Quit key
QUIT_KEY = 'q'
