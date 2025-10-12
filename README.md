# Sign2Calc

Gesture-based calculator using webcam and hand detection. Perform calculations naturally with hand gestures.

## Features

### Basic Operations

- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (\*)
- **Division** (/)
- **Clear** (C) - Reset calculator
- **Backspace** (<) - Remove last character
- **Equals** (=) - Calculate result
- **Decimal** (.) - Decimal point

### How It Works

1. Show hand gestures to camera
2. System recognizes gesture (numbers/operations)
3. Calculator updates display
4. Visual feedback shows detected gesture
5. Press '=' gesture to calculate

## Project Structure

```
Sign2Calc/
├── src/
│   ├── gest-calc/
│   │   ├── main.py                    # Entry point
│   │   ├── config.py                  # Constants (resolution, colors, etc)
│   │   │
│   │   ├── ui/
│   │   │   ├── components.py          # Button, TextDisplay classes
│   │   │   ├── calculator_display.py  # UI renderer
│   │   │   └── layout_manager.py      # Layout calculations
│   │   │
│   │   ├── gesture/
│   │   │   ├── hand_detector.py       # MediaPipe hand detection
│   │   │   ├── gesture_recognizer.py  # Classify gestures from landmarks
│   │   │   ├── gesture_mapper.py      # Map gestures → buttons
│   │   │   └── gesture_stabilizer.py  # Filter false positives
│   │   │
│   │   ├── calculator/
│   │   │   └── calculator_logic.py    # Operations and state
│   │   │
│   │   └── utils/
│   │       ├── camera_manager.py      # Camera initialization
│   │       └── fps_counter.py         # Performance monitoring
│   │
│   └── test/
│       └── camera_resolution_test.py  # Test utilities
│
├── docs/
├── Dockerfile
├── Makefile
└── requirements.txt                         # Testing utilities
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

- Docker
- Webcam
- X11 (for GUI display)

## Tech Stack

- **Python 3.9**
- **OpenCV** - Image processing and GUI
- **MediaPipe** - Hand landmark detection
- **Docker** - Containerized environment

## Course

Created for Intelligent Interactive Systems (UIE - 4th year).

See [ROADMAP.md](https://claude.ai/chat/docs/ROADMAP.md) for architecture details.

## License

Apache License 2.0
