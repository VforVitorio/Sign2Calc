# Sign2Calc

Gesture-based calculator using webcam and hand detection. Perform calculations naturally with hand gestures through an innovative incremental digit entry system.

## Features

### Gesture-Controlled Operations

Sign2Calc uses **10 distinct hand gestures** optimized for MediaPipe detection:

#### Digit Entry
- 👊 **Fist** - Start digit entry mode (cursor at 0)
- ☝️ **Index** - Increment digit (+1 per repeat)
- ✌️ **Two Fingers** - Confirm digit

#### Operations
- ✋ **Open Palm** - Addition (+)
- 👍 **Thumb Up** - Subtraction (−)
- 🤙 **Pinky Only** - Multiplication (×)
- 🤙 **Shaka** - Division (÷)
- 👌 **OK Sign** - Equals/Calculate (=)

#### Editing
- 🖖 **Middle + Ring** - Clear (C)
- 🤘 **Index + Pinky** - Backspace (<)

### How It Works

1. **Make a fist** (👊) to start entering a digit
2. **Raise index finger** (☝️) to increment the digit (0→1→2→3...)
   - Repeat the gesture for each increment
3. **Show two fingers** (✌️) to confirm the digit
4. **Select an operation** using the corresponding gesture (✋ for +, 👍 for -, etc.)
5. **Repeat steps 1-3** to enter the next number
6. **Make OK sign** (👌) to calculate the result

**Additional Controls:**
- Use **Middle + Ring** (🖖) to clear everything
- Use **Index + Pinky** (🤘) to delete the last character

**Example:** To compute `15 + 8`:

- 👊 → ☝️ (repeat to reach 1) → ✌️ → 👊 → ☝️ (repeat to reach 5) → ✌️ → ✋ → 👊 → ☝️ (repeat to reach 8) → ✌️ → 👌

**Example with correction:** To compute `23 + 5` (but you entered `24` by mistake):

- 👊 → ☝️ (repeat to reach 2) → ✌️ → 👊 → ☝️ (repeat to reach 4) → ✌️ → 🤘 (backspace) → 👊 → ☝️ (repeat to reach 3) → ✌️ → ✋ → 👊 → ☝️ (repeat to reach 5) → ✌️ → 👌

For more details, see [GESTURE_GUIDE.md](docs/GESTURE_GUIDE.md).

## Project Structure

```
Sign2Calc/
├── src/
│   ├── gest-calc/
│   │   ├── main.py                    # Entry point
│   │   ├── config.py                  # Constants (resolution, colors, etc)
│   │   │
│   │   ├── ui/
│   │   │   └── components.py          # Button class for UI elements
│   │   │
│   │   ├── gesture/
│   │   │   ├── hand_detector.py       # MediaPipe hand detection
│   │   │   ├── gesture_recognizer.py  # Classify gestures from landmarks
│   │   │   ├── gesture_mapper.py      # Map gestures → calculator actions
│   │   │   └── gesture_stabilizer.py  # Temporal smoothing & false positive filtering
│   │   │
│   │   ├── calculator/
│   │   │   └── calculator_logic.py    # Calculator state & operations
│   │   │
│   │   └── utils/                     # (Reserved for future utilities)
│   │
│   └── test/
│       ├── camera_resolution_test.py  # Camera capability testing
│       └── webcam_test.py             # Basic webcam functionality test
│
├── docs/
│   ├── CHANGELOG.md                   # Version history
│   ├── GESTURE_GUIDE.md               # Complete gesture documentation
│   └── ROADMAP.md                     # Architecture & future plans
│
├── Dockerfile
├── Makefile
├── requirements.txt
└── LICENSE
```

## Quick Start

### Build

```bash
make build
```

### Test Camera

```bash
make camtest
```

### Run Calculator

```bash
make run
```

### Development Shell

```bash
make shell
```

## Requirements

- Python 3.9+
- Webcam
- (Optional) Docker for containerized environment

## Tech Stack

- **Python 3.9**
- **OpenCV** - Image processing and GUI
- **MediaPipe** - Hand landmark detection and tracking
- **Docker** - Containerized environment (optional)

## Documentation

- **[GESTURE_GUIDE.md](docs/GESTURE_GUIDE.md)** - Complete gesture system documentation with design principles and usage examples
- **[ROADMAP.md](docs/ROADMAP.md)** - Architecture details and future development plans
- **[CHANGELOG.md](docs/CHANGELOG.md)** - Version history and release notes

## Current Status

**Version 2.0.0** - First functional release with complete gesture recognition system.

### Recent Improvements

- ✅ UI redesigned with larger buttons and better alignment
- ✅ Separate OPERATION and RESULT displays for clearer feedback
- ✅ Visual progress bar showing gesture hold duration
- ✅ Added Clear (C) and Backspace (<) gesture controls
- ✅ Enhanced gesture recognition with 10 distinct gestures

See [CHANGELOG.md](docs/CHANGELOG.md) for detailed release notes.

## Course

Created for Intelligent Interactive Systems (UIE - 4th year).

## License

Apache License 2.0
