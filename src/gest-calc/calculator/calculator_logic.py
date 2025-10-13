"""
Calculator logic for Sign2Calc
Handles mathematical operations and state management
"""


class CalculatorLogic:
    """
    Manages calculator state and operations
    """

    def __init__(self):
        """
        Constructor: initialize calculator with empty operation string
        """
        self.operation = ""

    def process_input(self, value):
        """
        Process a button input and update calculator state

        Args:
            value: String representing button pressed ('0'-'9', '+', '-', '*', '/', '=', 'C', '<', '.')

        Returns:
            str: Current operation string after processing

        """

        if value == "=":
            self._evaluate()
        elif value == "C":
            self._clear()
        elif value == "<":
            self._backspace()
        else:
            self._append(value)

        return self.operation

    def _evaluate(self):
        """
        Evaluate the current operation string
        Sets operation to result or "Error" if invalid
        """

        try:
            self.operation = str(eval(self.operation))
        except:
            self.operation = "Error"

    def _clear(self):
        """
        Reset operation to empty string
        """

        self.operation = ""

    def _backspace(self):
        """
        Remove last character from operation
        """

        self.operation = self.operation[:-1]

    def _append(self, value):
        """
        Append a value to the operation string

        Args:
            value: Character to append
        """

        self.operation += value

    def get_operation(self):
        """
        Get current operation string

        Returns:
            str: current operation
        """

        return self.operation
