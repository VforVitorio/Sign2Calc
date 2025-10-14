"""
Gesture mapper module
Maps confirmed gestures to calculator actions
"""


class GestureMapper:
    """
    Maps gestures to calculator operations
    """

    def __init__(self, calculator):
        """
        Initialize gestrue mapper with CalculatorLogic instance
        """

        self.calculator = calculator
        self.gesture_map = {
            "FIST": self._handle_fist,
            "INDEX": self._handle_index,
            "TWO_FINGERS": self._handle_two_fingers,
            "PALM": self._handle_palm,
            "THUMB_UP": self._handle_thumb_up,
            "PINKY": self._handle_pinky,
            "SHAKA": self._handle_shaka,
            "OK_SIGN": self._handle_ok_sign
        }

    def handle(self, gesture_name):
        """
        Handle confirmed gesture

        Args:
            gesture_name: Name of confirmed gesture

        Returns:
            bool: True if gesture was handled
        """

        if gesture_name in self.gesture_map:
            self.gesture_map[gesture_name]()
            return True
        return False

    def _handle_fist(self):
        """Start digit mode"""
        self.calculator.start_digit()

    def _handle_index(self):
        """Increment digit"""
        self.calculator.increment_digit()

    def _handle_two_fingers(self):
        """Confirm digit"""
        self.calculator.confirm_digit()

    def _handle_palm(self):
        """Addition operator"""
        self.calculator.add_operator("+")

    def _handle_thumb_up(self):
        """Subtraction operator"""
        self.calculator.add_operator("-")

    def _handle_pinky(self):
        """Multiplication operator"""
        self.calculator.add_operator("*")

    def _handle_shaka(self):
        """Division operator"""
        self.calculator.add_operator("/")

    def _handle_ok_sign(self):
        """Calculate result"""
        self.calculator.calculate()
