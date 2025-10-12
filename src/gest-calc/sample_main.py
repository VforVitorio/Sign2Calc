import cv2


class Button:
    """
    Represents a calculator button with position, size, and value
    """

    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        """
        Draw button on the image with background and border
        """
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)

        text_x = self.pos[0] + self.width // 2 - 15
        text_y = self.pos[1] + self.height // 2 + 15

        cv2.putText(img, self.value, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN,
                    3, (50, 50, 50), 3)


# Camera configuration
# Index 0 is usually the default camera (may vary by system)
cap = cv2.VideoCapture(0)

# Camera resolution (actual hardware capability)
CAM_WIDTH = 640
CAM_HEIGHT = 480
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

# Display resolution (target fullscreen resolution)
WIDTH = 1920
HEIGHT = 1080

# Create fullscreen window
cv2.namedWindow("Calculator", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(
    "Calculator", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Calculator button layout
buttonListValues = [['C', '<'],
                    ['7', '8', '9', '/'],
                    ['4', '5', '6', '*'],
                    ['1', '2', '3', '-'],
                    ['0', '.', '=', '+']]

buttonlist = []
for y in range(5):
    for x in range(4):
        # First row only has 2 buttons (C and <)
        if y == 0 and x >= 2:
            break

        xpos = int(WIDTH - 500 + x * 100)
        ypos = int(HEIGHT * 0.15 + y * 100)

        # First row special case: second button needs to be shifted
        if y == 0 and x == 1:
            xpos += 100

        if y == 0:
            # First row has wider buttons
            width = 200
            buttonlist.append(Button((xpos, ypos), width,
                              100, buttonListValues[y][x]))
        else:
            buttonlist.append(
                Button((xpos, ypos), 100, 100, buttonListValues[y][x]))

operation = ""

while True:
    success, img = cap.read()

    # Resize camera feed to fullscreen resolution BEFORE drawing UI elements
    img = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_LINEAR)

    # Display area for operation string
    operation_x = int(WIDTH - 500)
    operation_y = int(HEIGHT * 0.05)

    cv2.rectangle(img, (operation_x, operation_y), (operation_x + 400, operation_y + 120),
                  (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (operation_x, operation_y), (operation_x + 400, operation_y + 120),
                  (50, 50, 50), 3)

    # Draw all calculator buttons
    for button in buttonlist:
        button.draw(img)

    # TODO: Implement gesture detection here
    # When a gesture is detected, set something=True and received_val to button value
    something = False
    received_val = ""

    if something:
        if received_val == "=":
            try:
                operation = str(eval(operation))
            except:
                operation = "Error"
        elif received_val == "C":  # Reset
            operation = ""
        elif received_val == "<":  # Remove last character
            operation = operation[:-1]
        else:
            operation += received_val

    # Display operation string
    cv2.putText(img, operation, (operation_x + 10, operation_y + 75),
                cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    cv2.imshow('Calculator', img)

    # Press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
