# Gesture Controls (single-hand)

This section documents the single-hand gesture design used by Sign2Calc. It aims to be concise, implementation-ready, and focuses on robustness, accessibility and simple UX.

**Note:** These specific gestures were chosen because they are the ones MediaPipe detects most reliably and consistently based on testing.

### Design principles

- **Single hand only** to reduce occlusion and detection complexity.
- **Minimal and highly distinct gestures** that lower classification errors that could occur with one-to-ten finger counting.
- **Incremental digit entry**, following `activate -> increment -> confirm`.
- **Visual feedback** in UI to close the interaction loop.
- **MediaPipe-optimized gestures** selected for maximum detection accuracy.

---

## Gesture map

### Digit Entry
|          Gesture | Action                    |
| ---------------: | ------------------------- |
|         👊*Fist* | Start digit (cursor at 0) |
|        ☝️*Index* | Increment (+1 per repeat) |
|  ✌️*Two fingers* | Confirm digit             |

### Operations
|          Gesture | Action                    |
| ---------------: | ------------------------- |
|    ✋*Open palm* | Addition (+)              |
|     👍*Thumb up* | Subtraction (−)           |
| 🤙*Pinky (only)* | Multiplication (×)        |
|        🤙*Shaka* | Division (÷)              |
|      👌*OK sign* | Equals (=)                |

### Editing Controls
|            Gesture | Action        |
| -----------------: | ------------- |
| 🖖*Middle + Ring*  | Clear (C)     |
| 🤘*Index + Pinky*  | Backspace (<) |

## Interaction flow examples

### Example 1: Basic calculation `15 + 8`

1. `👊` → enter digit mode (digit = 0)
2. `☝️` ×1 → digit = 1
3. `✌️` → confirm → first operand = `1`
4. `👊` → enter digit mode
5. `☝️` ×5 → digit = 5
6. `✌️` → confirm → operand = `15`
7. `✋` → select addition (+)
8. `👊` → enter digit mode
9. `☝️` ×8 → digit = 8
10. `✌️` → confirm → second operand = `8`
11. `👌` → compute → UI shows `23`

### Example 2: Using backspace `23 + 5` (after entering `24` by mistake)

1. `👊` → enter digit mode
2. `☝️` ×2 → digit = 2
3. `✌️` → confirm → first operand = `2`
4. `👊` → enter digit mode
5. `☝️` ×4 → digit = 4
6. `✌️` → confirm → operand = `24`
7. `🤘` → backspace → operand = `2`
8. `👊` → enter digit mode
9. `☝️` ×3 → digit = 3
10. `✌️` → confirm → operand = `23`
11. `✋` → select addition (+)
12. `👊` → enter digit mode
13. `☝️` ×5 → digit = 5
14. `✌️` → confirm → second operand = `5`
15. `👌` → compute → UI shows `28`

### Example 3: Using clear

1. After any operation, use `🖖` (Middle + Ring) to clear everything and start fresh

## Detection heuristics

- **Hold threshold for static gestures** 0.5-1s to accept in order to reduce false positives due to hand movements.
- **Increment cooldown**: allow one increment per 0.5s while holding index for repeated increments.
- **Confirmation cooldown:** 0.5 s after confirm gestures to avoid duplicates.
- **Input timeout:** 5–8 s inactivity → auto-save or cancel digit entry.
- **Swipe threshold:** minimum speed/distance to qualify as delete.

---

## UI & feedback

<div align="center">
  <img src="UI_Design.png" alt="Sign2Calc UI Design" width="400"/>
</div>

- Show current digit, full operand, and active operation clearly on screen.
- Provide instant visual affordance when a gesture is detected (icon + brief animation + optional sound).
- Include an on-screen fallback control (button/keyboard) for accessibility and robustness.

## Why this approach

This gesture system prioritizes reliability and accessibility by using a small set of highly distinctive hand shapes that are easy to detect and hard to confuse.

**MediaPipe Detection Optimization:** Through testing, these specific gestures were found to be the most reliably detected by MediaPipe's hand landmark detection system:

- **Digit entry gestures:** Fist, Index, Two Fingers
- **Operation gestures:** Palm, Thumb Up, Pinky Only, Shaka, OK Sign
- **Editing gestures:** Middle + Ring, Index + Pinky

These gestures provide clear finger position patterns that minimize false positives and confusion between gestures. The editing gestures (Middle + Ring for Clear, Index + Pinky for Backspace) were specifically chosen to be:
- **Easy to perform** - Natural hand positions that don't require difficult finger isolation
- **Highly distinctive** - Cannot be confused with operation gestures or digit entry gestures
- **Non-offensive** - Appropriate for all contexts and cultures

By relying on a single hand, we avoid occlusion issues while keeping interactions simple and natural. The incremental entry pattern scales to any number without adding complexity, and the straightforward gestures work well for users with varying levels of hand mobility, making the calculator genuinely more inclusive.
