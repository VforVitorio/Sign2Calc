"""
Calculator logic module
Handles calculator state and operations
"""


class CalculatorLogic:
    """
    Manages calculator state and operations
    """

    def __init__(self):
        """
        Initialize calculator state
        """
        self.operation = ""
        self.result = None
        self.current_digit = 0
        self.digit_mode = False

    def start_digit(self):
        """
        Enter digit mode and reset current digit to 0
        """
        self.digit_mode = True
        self.current_digit = 0

    def increment_digit(self):
        """
        Increment current digit by 1 (wraps at 10)
        Only works in digit mode
        """
        if self.digit_mode:
            self.current_digit = (self.current_digit + 1) % 10

    def confirm_digit(self):
        """
        Confirm current digit and add to operation
        Exits digit mode
        """
        if self.digit_mode:
            self.operation += str(self.current_digit)
            self.digit_mode = False
            self.current_digit = 0

    def add_operator(self, operator):
        """
        Add operator to operation
        Auto-confirms digit if in digit mode

        Args:
            operator: Operator string ("+", "-", "*", "/")
        """
        if self.digit_mode:
            self.confirm_digit()
        self.operation += operator

    def calculate(self):
        """
        Evaluate operation and display result
        Handles errors gracefully
        """
        try:
            # Store result separately, keep operation for display
            self.result = str(eval(self.operation))
            self.digit_mode = False
        except:
            self.result = "Error"
            self.digit_mode = False

    def clear(self):
        """
        Reset calculator to initial state
        """
        self.operation = ""
        self.result = None
        self.current_digit = 0
        self.digit_mode = False

    def backspace(self):
        """
        Remove last character from operation
        Clears result if present
        """
        # Clear result if it exists
        if self.result is not None:
            self.result = None
        # Remove last character from operation
        elif len(self.operation) > 0:
            self.operation = self.operation[:-1]

    def get_operation(self):
        """
        Get current operation string for display

        Returns:
            str: Operation string (with current digit if in digit mode)
        """
        if self.digit_mode:
            return self.operation + str(self.current_digit)
        return self.operation

    def get_current_digit(self):
        """
        Get current digit being built

        Returns:
            int: Current digit (0-9)
        """
        return self.current_digit

    def is_digit_mode(self):
        """
        Check if calculator is in digit mode

        Returns:
            bool: True if in digit mode
        """
        return self.digit_mode

    def get_result(self):
        """
        Get the calculated result

        Returns:
            str or None: Result string or None if no result yet
        """
        return self.result
