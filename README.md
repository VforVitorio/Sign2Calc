# Sign2Calc

Gesture-based calculator using webcam and hand detection. Perform calculations naturally with hand gestures through an innovative incremental digit entry system.

<p align="center">
  <a href="https://deepwiki.com/VforVitorio/Sign2Calc">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki">
  </a>
</p>

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

For complete usage instructions and examples, see [GESTURE_GUIDE.md](docs/GESTURE_GUIDE.md).

## Project Structure

```
Sign2Calc/
├── src/
│   ├── gest-calc/
│   │   ├── main.py                    # Application entry point
│   │   ├── config.py                  # Configuration constants
│   │   ├── ui/
│   │   │   ├── components.py          # UI components (Button class)
│   │   │   └── ui_renderer.py         # UI rendering system
│   │   ├── gesture/
│   │   │   ├── hand_detector.py       # Hand tracking (MediaPipe)
│   │   │   ├── gesture_recognizer.py  # Gesture classification
│   │   │   ├── gesture_mapper.py      # Gesture → action mapping
│   │   │   └── gesture_stabilizer.py  # Temporal filtering
│   │   └── calculator/
│   │       └── calculator_logic.py    # Calculator operations
│   └── test/
│       ├── camera_resolution_test.py  # Camera testing
│       └── webcam_test.py             # Webcam testing
├── docs/                              # Documentation
├── Dockerfile                         # Container configuration
├── Makefile                           # Build & run commands
└── requirements.txt                   # Python dependencies
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
