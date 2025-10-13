"""
Hand detection module using MediaPipe
Detects hands in images and extracts landmark positions
"""

import cv2
import mediapipe as mp


class HandDetector:
    """
    Detects hands in images using MediaPipe Hands solution
    """

    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        """
        Initialize MediaPipe hand detector

        Args:
            mode: If False, treats images as video stream (faster). If True, treats each as independent image
            max_hands: Maximum number of hands to detect
            detection_confidence: Minimum confidence for hand detection (0.0 to 1.0)
            tracking_confidence: Minimum confidence for hand tracking (0.0 to 1.0)
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_draw_styles = mp.solutions.drawing_styles

    def find_hands(self, img, draw=True):
        """
        Detect hands in the image

        Args:
            img: Input image (BGR format from OpenCV)
            draw: If True, draw hand landmarks on the image

        Returns:
            img: Image with landmarks drawn (if draw=True)
        """
        # Convert BGR to RGB for MediaPipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image and detect hands
        self.results = self.hands.process(img_rgb)

        # Draw hand landmarks if requested and hands are detected
        if self.results.multi_hand_landmarks and draw:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_draw_styles.get_default_hand_landmarks_style(),
                    self.mp_draw_styles.get_default_hand_connections_style()
                )

        return img

    def find_position(self, img, hand_no=0):
        """
        Get landmark positions for a specific hand

        Args:
            img: Input image
            hand_no: Which hand to get landmarks from (0 = first hand, 1 = second hand)

        Returns:
            list: List of landmarks in format [(id, x, y), ...] where x, y are pixel coordinates
                  Returns empty list if no hands detected
        """
        landmark_list = []

        # Check if hands were detected
        if self.results.multi_hand_landmarks:
            # Check if the requested hand exists
            if hand_no < len(self.results.multi_hand_landmarks):
                hand = self.results.multi_hand_landmarks[hand_no]

                # Get image dimensions
                h, w, c = img.shape

                # Extract landmark positions
                for id, landmark in enumerate(hand.landmark):
                    # Convert normalized coordinates to pixel coordinates
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    landmark_list.append((id, cx, cy))

        return landmark_list

    def get_hand_type(self, hand_no=0):
        """
        Get the type of hand (Left or Right)

        Args:
            hand_no: Which hand to check (0 = first hand, 1 = second hand)

        Returns:
            str: "Left" or "Right", or None if hand not detected
        """
        if self.results.multi_hand_landmarks:
            if hand_no < len(self.results.multi_handedness):
                return self.results.multi_handedness[hand_no].classification[0].label

        return None

    def hands_detected(self):
        """
        Check if any hands are currently detected

        Returns:
            bool: True if at least one hand is detected, False otherwise
        """
        return self.results.multi_hand_landmarks is not None

    def get_num_hands(self):
        """
        Get the number of hands currently detected

        Returns:
            int: Number of hands detected (0, 1, or 2)
        """
        if self.results.multi_hand_landmarks:
            return len(self.results.multi_hand_landmarks)
        return 0
