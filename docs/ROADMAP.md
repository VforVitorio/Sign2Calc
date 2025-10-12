# Development Roadmap

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
└── requirements.txt
```

## What Each Module Does

### `ui/`

- **components.py** : Reusable UI classes (Button, display areas)
- **calculator_display.py** : Draws calculator on screen
- **layout_manager.py** : Calculates button positions for any resolution

### `gesture/`

- **hand_detector.py** : Uses MediaPipe to detect hand landmarks
- **gesture_recognizer.py** : Analyzes landmarks to identify gestures (numbers, operations)
- **gesture_mapper.py** : Converts recognized gestures to calculator inputs
- **gesture_stabilizer.py** : Prevents accidental triggers (debouncing, confidence threshold)

### `calculator/`

- **calculator_logic.py** : Handles calculation operations, maintains state

### `utils/`

- **camera_manager.py** : Camera setup and frame capture
- **fps_counter.py** : Displays FPS for performance monitoring

## Implementation Plan

1. **Phase 1** : Migrate existing code to modular structure
2. **Phase 2** : Integrate MediaPipe hand detection
3. **Phase 3** : Implement gesture recognition (finger counting, pinch, etc)
4. **Phase 4** : Add stabilization and visual feedback
5. **Phase 5** : Testing and optimization
