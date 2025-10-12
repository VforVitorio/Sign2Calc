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
src/
├── gest-calc/
│   ├── main.py                    # Application entry
│   ├── ui/                        # User interface components
│   ├── gesture/                   # Gesture recognition system
│   ├── calculator/                # Calculator logic
│   └── utils/                     # Helper utilities
└── test/                          # Testing utilities
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
