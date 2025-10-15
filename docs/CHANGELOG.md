# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-10-15 [Released]

### Added

- **Two New Gestures** - Extended gesture system with utility operations:
  - 🖖 Middle + Ring fingers: Clear (C) - Reset calculator to initial state
  - 🤘 Index + Pinky fingers: Backspace (<) - Delete last character
- **Complete UI Renderer Module** (`ui/ui_renderer.py`) - Professional rendering system with:
  - Modular drawing functions for all UI components
  - Webcam feed integration with proper positioning
  - Gesture indicator panel with real-time feedback
  - Operation and result display panels
  - Debug panel for development
  - FPS counter for performance monitoring
  - Calculator button grid with proper alignment
- **Visual Feedback System** - Real-time hover effect with green highlight on detected gesture key
- **Improved Text Sizing** - Adjusted font scales to fit correctly within UI boxes and buttons

### Changed

- **README.md** - Comprehensive update with:
  - Complete gesture map with emojis and descriptions
  - Detailed "How It Works" section with practical example
  - Accurate project structure reflecting actual implementation
  - Documentation section with links to all guides
  - Current status and known limitations
  - Updated requirements (Docker now optional)
- **Gesture Guide** (`docs/GESTURE_GUIDE.md`) - Updated with new Clear and Backspace gestures
- **Calculator Logic** (`calculator/calculator_logic.py`) - Added support for Clear and Backspace operations
- **Gesture Mapper** (`gesture/gesture_mapper.py`) - Integrated new MIDDLE_RING and INDEX_PINKY gesture mappings
- **Gesture Recognizer** (`gesture/gesture_recognizer.py`) - Added classification for two new finger combinations
- **Gesture Stabilizer** (`gesture/gesture_stabilizer.py`) - Simplified and optimized confirmation logic
- **Main Application** (`main.py`) - Major refactor to use new UI renderer module
- **Config** (`config.py`) - Extensive additions for UI layout constants:
  - Title, webcam, and display panel coordinates
  - Gesture indicator and debug panel positions
  - Calculator button grid layout
  - Color schemes and styling constants
- **UI Components** (`ui/components.py`) - Enhanced Button class with improved text centering and sizing
- **UI Module** (`ui/__init__.py`) - Updated exports to include UIRenderer

### Fixed

- **Button Text Alignment** - Corrected text positioning to properly center within buttons
- **Font Scaling** - Fixed text overflow issues by adjusting font scales for different UI elements
- **UI Layout** - Aligned calculator interface with original design specifications

### Technical Improvements

- **Code Organization** - Separated UI rendering logic from main application logic
- **Maintainability** - Modular UI system makes updates and customizations easier
- **Visual Consistency** - Unified color scheme and styling across all UI components
- **Performance** - Optimized rendering pipeline with minimal overhead

### Documentation

- **Enhanced README** - Now serves as comprehensive entry point with complete feature overview
- **Updated Gesture Guide** - Includes all 10 gestures with clear usage instructions
- **Accurate Project Structure** - Documentation now matches actual implementation

## [2.0.0] - 2025-10-14 [Released]

### Added

- **Complete Gesture Recognition System** - Full implementation of 8 distinct hand gestures optimized for MediaPipe detection
  - 👊 Fist: Start digit entry mode (cursor at 0)
  - ☝️ Index: Increment digit (+1 per repeat)
  - ✌️ Two fingers: Confirm digit
  - ✋ Open palm: Addition operator (+)
  - 👍 Thumb up: Subtraction operator (−)
  - 🤙 Pinky only: Multiplication operator (×)
  - 🤙 Shaka: Division operator (÷)
  - 👌 OK sign: Equals/Calculate (=)
- **Hand Detector Module** (`gesture/hand_detector.py`) - MediaPipe-based hand tracking and landmark extraction
- **Gesture Recognizer** (`gesture/gesture_recognizer.py`) - Finger position analysis and gesture classification
- **Gesture Stabilizer** (`gesture/gesture_stabilizer.py`) - Advanced gesture confirmation system with:
  - Hold threshold for static gestures (0.5-1s)
  - Increment cooldown for repeated increments
  - Confirmation cooldown to avoid duplicates
  - Temporal smoothing and false positive filtering
- **Gesture Mapper** (`gesture/gesture_mapper.py`) - Maps confirmed gestures to calculator actions
- **Gesture Package** - Added `__init__.py` with proper exports for gesture module
- **Comprehensive Gesture Guide** (`docs/GESTURE_GUIDE.md`) - Complete documentation with:
  - Design principles and rationale
  - Full gesture map and interaction flow examples
  - Detection heuristics and UI feedback guidelines
  - MediaPipe optimization notes
- **MediaPipe Integration** - Added `mediapipe` dependency to `requirements.txt`
- **Real-time Visual Feedback** - Display of current operation and last detected gesture in UI

### Changed

- **Calculator Logic** - Updated `calculator_logic.py` to integrate with gesture recognition system
- **Main Application** - Enhanced `main.py` with full gesture detection pipeline and visual feedback
- **Interaction Model** - Implemented incremental digit entry system (activate → increment → confirm)

### Technical Improvements

- **Single-Hand Detection** - Optimized for single hand to reduce occlusion and complexity
- **Robust Gesture Classification** - Selected gestures with highest MediaPipe detection accuracy
- **Temporal Consistency** - Added smoothing algorithms to prevent false positives during hand movements

### Known Limitations

- **Gesture Retention Issue** - Maintaining a gesture after detection may trigger duplicate actions without requiring gesture change
- **UI Design Pending** - Current interface is functional but requires refinement to match planned design specifications
- **Stabilizer Fine-tuning** - Cooldown timers and hold thresholds may need adjustment for optimal UX

## [1.2.0] - 2025-10-13 [Released]

### Added

- **Modular Architecture** - Implemented complete modular structure following ROADMAP design
- **Configuration System** (`config.py`) - Centralized configuration for camera, display, UI colors, layout, and button definitions
- **UI Components Module** (`ui/components.py`) - Reusable Button class with constructor and draw methods
- **Calculator Logic Module** (`calculator/calculator_logic.py`) - Complete calculator state management and operations handler
- **Main Application** (`main.py`) - New entry point with proper imports and application flow
- **Module Structure** - Added `__init__.py` files for `ui` and `calculator` packages
- **Project Structure** - Established directory structure with `.gitkeep` files for empty directories (`gesture/`, `utils/`)

### Changed

- **Makefile** - Updated `run` target to execute `main.py` instead of `sample_main.py`
- **Project Organization** - Restructured codebase to follow modular design pattern

### Fixed

- **Button Text Positioning** - Corrected `text_y` calculation in `components.py` (line 69) from width to height
- **Font Configuration** - Fixed FONT constant in `config.py` from `FONT = 0` to `FONT = cv2.FONT_HERSHEY_PLAIN`

### Removed

- **sample_main.py** - Removed in favor of modular `main.py`
- **webcam_test.py** from gest-calc - Already moved to test directory in v1.1.0

## [1.1.0] - 2025-10-12 [Released]

### Added

- Camera resolution test script (`src/test/camera_resolution_test.py`) for testing camera hardware capabilities
- Fullscreen mode support for better user experience
- Comprehensive documentation structure with CHANGELOG, ROADMAP, and UI design assets
- UI design PNG documentation in docs folder
- Support for 640x480 camera resolution with 1080p display scaling

### Changed

- Moved `webcam_test.py` from `src/gest-calc/` to `src/test/` directory for better organization
- Updated calculator UI to adapt for 640x480 camera with 1080p fullscreen display
- Improved frame resizing from 640x480 to 1920x1080 before drawing UI elements
- Updated all button coordinates and display area to use 1080p resolution
- Enhanced code documentation with English comments
- Modified camera index from 2 to 0 for better hardware compatibility
- Adjusted display positioning to correctly show calculator on the image with new resolution

### Fixed

- Calculator UI positioning issues when using different camera resolutions
- Camera capture resolution mismatch with display resolution
- Screen display configuration for fullscreen mode

### Removed

- Eliminated deprecated claude code folder

## [1.0.0] - 2024-10-10

### Added

- Initial project setup
- Basic project structure with src/gest-calc directory
- Sample main.py and webcam_test.py files
- Docker configuration
- Requirements file
- License and README documentation

### Changed

- Updated README with project description for UIE course assignment
