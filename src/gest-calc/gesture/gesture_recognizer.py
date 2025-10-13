"""
Gesture recognition module
Analyzes hand landmarks to classify gestures
"""


class GestureRecognizer:
    """
    Recognizes hand gestures from MediaPipe landmarks
    """

    def __init__(self):
        """
        Initalize gesture recognizer
        """
        # MediaPipe landmark indices
        # Thumb, Index, Middle, Ring, Pinky tips
        self.tip_ids = [4, 8, 12, 16, 20]
        # Index, Middle, Ring, Pinky (without thumb)
        self.finger_tip_ids = [8, 12, 16, 20]

    def recognize(self, landmark_list):
        """
        Recognize gesture from hand landmarks

        Args:
            landmark_list: List of landmarks from HandDetector in format [(id, x, y), ...]

        Returns:
            str: Gesture name or None if no gesture recognizes
        """

        if not landmark_list or len(landmark_list) < 21:
            return None

        # Get which fingers are up
        fingers = self._get_fingers_up(landmark_list)

        # Classify gesture based on fingers up

        return self._classify_gesture(fingers)

    def _get_fingers_up(self, landmark_list):
        """
        Determine which fingers are extended

        Args:
            landmark_list: List of landmarks [(id, x, y), ...]

        Returns:
            list: [thumb, index, middle, ring, pinky] where 1 = up, 0 = down
        """
        fingers = []

        # Thumb: tip (4) further right than IP joint (3)
        if landmark_list[self.tip_ids[0]][1] > landmark_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers: tip Y < PIP Y (lower Y = higher up on screen)
        for tip_id in self.finger_tip_ids:
            pip_id = tip_id - 2  # PIP joint is 2 indices before tip

            if landmark_list[tip_id][2] < landmark_list[pip_id][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def _classify_gesture(self, fingers):
        """
        Classify gesture based on which fingers are up

        Args:
            fingers: List [thumb, index, middle, ring, pinky] (1=up, 0=down)

        Returns:
            str: Gesture name or None
        """
        # Fist: all fingers down
        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"

        # Index: only index finger up
        if fingers == [0, 1, 0, 0, 0]:
            return "INDEX"

        # Two fingers (peace sign): index and middle up
        if fingers == [0, 1, 1, 0, 0]:
            return "TWO_FINGERS"

        # No recognized gesture
        return None

    def get_gesture_description(self, gesture_name):
        """
        Get human-readable description of gesture

        Args:
            gesture_name: Gesture name from recognize()

        Returns:
            str: Description of what the gesture does
        """
        descriptions = {
            "FIST": "Start new digit (0)",
            "INDEX": "Increment digit (+1)",
            "TWO_FINGERS": "Confirm digit"
        }

        return descriptions.get(gesture_name, "Unknown gesture")
