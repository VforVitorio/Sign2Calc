"""
Gesture stabilization module with advanced detection heuristics
Implements hold thresholds, cooldowns, and timeout handling
"""

import time


class GestureStabilizer:
    """
    Stabilizes gesture recognition with configurable time-based thresholds
    """

    def __init__(self, fps=30):
        """
        Initialize gesture stabilizer

        Args:
            fps: Target frames per second for time-to-frame conversion
        """
        self.fps = fps

        # Configuration (in seconds, converted to frames internally)
        # Time to hold gesture before confirming (0.5-1s)
        self.hold_threshold_s = 0.7
        self.increment_cooldown_s = 0.5  # Cooldown between increments
        self.confirmation_cooldown_s = 0.5  # Cooldown after confirmation gestures
        self.input_timeout_s = 6.0  # Inactivity timeout (5-8s)

        # Convert to frames
        self._update_frame_thresholds()

        # Tracking state
        self.current_gesture = None
        self.gesture_count = 0
        self.cooldown_counter = 0
        self.last_confirmed_gesture = None
        self.inactivity_counter = 0

        # Special handling for INDEX (increment) gesture
        self.increment_cooldown_counter = 0
        self.last_increment_time = 0

    def _update_frame_thresholds(self):
        """
        Convert time-based thresholds to frame counts
        """
        self.hold_threshold_frames = int(self.hold_threshold_s * self.fps)
        self.increment_cooldown_frames = int(
            self.increment_cooldown_s * self.fps)
        self.confirmation_cooldown_frames = int(
            self.confirmation_cooldown_s * self.fps)
        self.input_timeout_frames = int(self.input_timeout_s * self.fps)

    def update(self, detected_gesture):
        """
        Update stabilizer with newly detected gesture

        Args:
            detected_gesture: Gesture name detected in current frame (or None)

        Returns:
            dict: {
                'gesture': str or None,  # Confirmed gesture
                'timeout': bool          # True if input timeout occurred
            }
        """
        result = {
            'gesture': None,
            'timeout': False
        }

        # Check for input timeout
        if self._check_timeout(detected_gesture):
            result['timeout'] = True
            return result

        # Handle cooldown period (blocks all gestures)
        if self._is_in_cooldown():
            self._decrement_cooldown()
            self._increment_inactivity()
            return result

        # Special handling for INDEX gesture (increments)
        if detected_gesture == "INDEX":
            confirmed = self._handle_increment_gesture()
            if confirmed:
                result['gesture'] = "INDEX"
                self._reset_inactivity()
            return result

        # Handle increment cooldown separately
        if self._is_in_increment_cooldown():
            self._decrement_increment_cooldown()

        # Standard gesture handling
        if self._is_new_gesture(detected_gesture):
            self._reset_gesture_tracking(detected_gesture)
            return result

        # Increment count for consistent gesture
        if self._is_consistent_gesture(detected_gesture):
            self._increment_gesture_count()

        # Check if gesture should be confirmed
        if self._should_confirm_gesture():
            confirmed_gesture = self._confirm_gesture(detected_gesture)
            result['gesture'] = confirmed_gesture
            self._reset_inactivity()

        return result

    def _check_timeout(self, detected_gesture):
        """
        Check if input timeout has been reached

        Args:
            detected_gesture: Current detected gesture

        Returns:
            bool: True if timeout occurred
        """
        if detected_gesture is None:
            self._increment_inactivity()

            if self.inactivity_counter >= self.input_timeout_frames:
                self.reset()
                return True
        else:
            self._reset_inactivity()

        return False

    def _handle_increment_gesture(self):
        """
        Special handling for INDEX gesture (repeatable increments)

        Returns:
            bool: True if increment should be confirmed
        """
        # If in increment cooldown, don't confirm
        if self._is_in_increment_cooldown():
            return False

        # First time seeing INDEX or after cooldown
        if self.current_gesture != "INDEX":
            self.current_gesture = "INDEX"
            self.gesture_count = 1
            return False

        # Increment count
        self.gesture_count += 1

        # Check if held long enough
        if self.gesture_count >= self.hold_threshold_frames:
            # Confirm and start increment cooldown
            self.last_confirmed_gesture = "INDEX"  # ← AÑADIDO
            self.increment_cooldown_counter = self.increment_cooldown_frames
            self.gesture_count = 0  # Reset but keep tracking INDEX
            return True

        return False

    def _is_in_cooldown(self):
        """
        Check if stabilizer is in general cooldown period

        Returns:
            bool: True if in cooldown
        """
        return self.cooldown_counter > 0

    def _is_in_increment_cooldown(self):
        """
        Check if stabilizer is in increment-specific cooldown

        Returns:
            bool: True if in increment cooldown
        """
        return self.increment_cooldown_counter > 0

    def _decrement_cooldown(self):
        """
        Decrement general cooldown counter
        """
        self.cooldown_counter -= 1

    def _decrement_increment_cooldown(self):
        """
        Decrement increment cooldown counter
        """
        self.increment_cooldown_counter -= 1

    def _increment_inactivity(self):
        """
        Increment inactivity counter
        """
        self.inactivity_counter += 1

    def _reset_inactivity(self):
        """
        Reset inactivity counter
        """
        self.inactivity_counter = 0

    def _is_new_gesture(self, detected_gesture):
        """
        Check if detected gesture is different from current tracked gesture

        Args:
            detected_gesture: Newly detected gesture

        Returns:
            bool: True if gesture changed
        """
        return detected_gesture != self.current_gesture

    def _reset_gesture_tracking(self, new_gesture):
        """
        Reset tracking when gesture changes

        Args:
            new_gesture: New gesture to start tracking
        """
        self.current_gesture = new_gesture
        self.gesture_count = 1 if new_gesture is not None else 0

    def _is_consistent_gesture(self, detected_gesture):
        """
        Check if detected gesture matches current tracked gesture

        Args:
            detected_gesture: Newly detected gesture

        Returns:
            bool: True if gesture is consistent
        """
        return detected_gesture == self.current_gesture and detected_gesture is not None

    def _increment_gesture_count(self):
        """
        Increment count of consecutive frames with same gesture
        """
        self.gesture_count += 1

    def _should_confirm_gesture(self):
        """
        Check if gesture has been stable long enough to confirm

        Returns:
            bool: True if gesture should be confirmed
        """
        return self.gesture_count >= self.hold_threshold_frames

    def _confirm_gesture(self, gesture_name):
        """
        Confirm gesture and start appropriate cooldown

        Args:
            gesture_name: Name of gesture to confirm

        Returns:
            str: Confirmed gesture name
        """
        self.last_confirmed_gesture = gesture_name

        # Confirmation gestures (TWO_FINGERS) get shorter cooldown
        if gesture_name == "TWO_FINGERS":
            self.cooldown_counter = self.confirmation_cooldown_frames
        else:
            # All other gestures get standard cooldown
            self.cooldown_counter = self.hold_threshold_frames

        self.gesture_count = 0
        self.current_gesture = None

        return self.last_confirmed_gesture

    def reset(self):
        """
        Reset stabilizer to initial state
        """
        self.current_gesture = None
        self.gesture_count = 0
        self.cooldown_counter = 0
        self.last_confirmed_gesture = None
        self.inactivity_counter = 0
        self.increment_cooldown_counter = 0

    def configure(self, hold_threshold_s=None, increment_cooldown_s=None,
                  confirmation_cooldown_s=None, input_timeout_s=None):
        """
        Update configuration parameters

        Args:
            hold_threshold_s: Time to hold gesture before confirming (seconds)
            increment_cooldown_s: Cooldown between increments (seconds)
            confirmation_cooldown_s: Cooldown after confirmation (seconds)
            input_timeout_s: Inactivity timeout (seconds)
        """
        if hold_threshold_s is not None:
            self.hold_threshold_s = hold_threshold_s
        if increment_cooldown_s is not None:
            self.increment_cooldown_s = increment_cooldown_s
        if confirmation_cooldown_s is not None:
            self.confirmation_cooldown_s = confirmation_cooldown_s
        if input_timeout_s is not None:
            self.input_timeout_s = input_timeout_s

        self._update_frame_thresholds()

    def get_status(self):
        """
        Get current stabilizer status for debugging

        Returns:
            dict: Current state information
        """
        return {
            "current_gesture": self.current_gesture,
            "gesture_count": self.gesture_count,
            "last_confirmed": self.last_confirmed_gesture,
            "cooldown": self.cooldown_counter,
            "increment_cooldown": self.increment_cooldown_counter,
            "inactivity": self.inactivity_counter,
            "progress": f"{self.gesture_count}/{self.hold_threshold_frames}" if self.current_gesture else "None",
            "timeout_in": f"{(self.input_timeout_frames - self.inactivity_counter) / self.fps:.1f}s" if self.inactivity_counter > 0 else "N/A"
        }
