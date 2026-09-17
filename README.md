# Facial Gesture Interpretation Engine

**Author:** Joe Nasr  
**Identity:** https://joe-nasr-signals.vercel.app/v2/  
**Live prototype:** https://facial-gesture-interpretation-engin.vercel.app

This repository is an experimental browser prototype for observing camera and microphone signals during an interview style session. It uses face detection, facial expression probabilities, landmark geometry, basic gaze direction heuristics, pitch estimation, volume measurements, and simple derived scores.

## What it actually measures

The browser can estimate or calculate:

1. Face detection and landmark positions.
2. Expression probabilities produced by face-api.js.
3. A rough lateral gaze state derived from facial landmarks.
4. Audio level and estimated fundamental frequency.
5. Session level variability derived from those signals.

## What it does not establish

The interface must not be treated as a forensic instrument, lie detector, psychological assessment, clinical tool, hiring decision system, or validated biometric diagnostic system.

The current derived labels such as stress, arousal, congruence, masking, and cognitive load are experimental heuristics. They have not been validated here against a controlled ground truth dataset. Facial expression probabilities and vocal variation cannot establish intent, deception, personality, mental state, or truthfulness on their own.

## Status

Experimental interface prototype.

The current implementation is useful for testing interaction design, signal visualization, browser media capture, and the limits of multimodal inference. It is not presented as scientific validation of the psychological meanings suggested by the interface labels.

## Technical notes

The prototype uses:

1. face-api.js for face detection, landmarks, and expression probabilities.
2. WebRTC media access for camera and microphone input.
3. Web Audio API analysis for volume and rough pitch estimation.
4. Client side JavaScript for derived session metrics and text export.

No claim of forensic, medical, employment, legal, or behavioral diagnostic validity should be inferred from this prototype.

Repository: https://github.com/Joenasriani/facial-gesture-interpretation-engine
