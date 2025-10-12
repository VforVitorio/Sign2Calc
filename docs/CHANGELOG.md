# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-10-12

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
