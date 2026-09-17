# Facial Gesture Interpretation Engine

**Author:** Joe Nasr  
**Identity:** https://joe-nasr-signals.vercel.app/v2/  
**Live prototype:** https://facial-gesture-interpretation-engin.vercel.app

AEON is a browser-based multimodal signal-observation prototype for studying what can and cannot be inferred from camera and microphone measurements during an interview-style session.

## What the current build measures

The browser can estimate or calculate:

1. Face detections and facial landmark positions using face-api.js.
2. Expression-category model probabilities produced by face-api.js.
3. A horizontal **head-orientation proxy** derived from nose position relative to detected eye landmarks. This is not eye tracking or gaze estimation.
4. A rough estimate of vocal fundamental frequency (F0) using autocorrelation.
5. Microphone signal level in dBFS and the proportion of sampled frames above a fixed -45 dBFS level threshold.
6. Session-level variability derived from those model outputs and sensor signals.

The current build does **not** calculate stress, arousal, congruence, masking, cognitive load, deception, truthfulness, personality, or diagnostic scores.

## Measurement boundary

These outputs are observations or model outputs, not direct measurements of private psychological states.

- An expression-model label is not a verified emotion.
- Facial movement is not a unique diagnostic signature of a specific emotion.
- The landmark-based orientation measure is a coarse head-orientation proxy, not gaze tracking.
- Fundamental frequency and level can vary with stress in some controlled studies, but also vary with speaker, sex/gender, speech task, language, physiology, microphone processing, environment, and other factors.
- A fixed audio-level threshold is not a validated speech detector.
- Correlation between a signal and a construct does not establish that the construct can be inferred for an individual session.

## Research integrity rules

1. Separate sensor/model output from interpretation.
2. Do not infer intent, deception, personality, cognition, mental state, diagnosis, or truthfulness from these signals.
3. Do not use AEON for clinical, legal, employment, hiring, security, or psychological decision making.
4. Preserve uncertainty, context, alternative explanations, and signal-quality limitations.
5. Validate any proposed psychological construct against an appropriate ground-truth protocol before presenting it as a measured variable.
6. Do not pool measurements from multiple visible people as though they belong to one participant.

## Current implementation notes

- face-api.js provides face detection, landmarks, and expression-category model probabilities.
- WebRTC requests camera and microphone access.
- Web Audio API supplies waveform data for level and rough F0 estimation.
- Processing of captured media occurs in the active browser session; the page does not upload captured camera or microphone content.
- Model/script assets are loaded from external web hosts, so network requests still occur for application dependencies.
- Session traces contain aggregate signal/model-output summaries rather than raw camera or microphone recordings.

## Research basis

The repository's interpretation boundary is informed by evidence including:

- Barrett LF, Adolphs R, Marsella S, Martinez AM, Pollak SD. *Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Human Facial Movements.* Psychological Science in the Public Interest (2019). PMID 31313636. https://pubmed.ncbi.nlm.nih.gov/31313636/
- Bian Y, Küster D, Liu H, Krumhuber EG. *Understanding Naturalistic Facial Expressions with Deep Learning and Multimodal Large Language Models.* Sensors (2024). PMID 38202988. https://pubmed.ncbi.nlm.nih.gov/38202988/
- Rojas Vistorte AO et al. *Integrating artificial intelligence to assess emotions in learning environments: a systematic literature review.* Frontiers in Psychology (2024). PMID 38966729. https://pubmed.ncbi.nlm.nih.gov/38966729/
- de Lacerda Veiga D et al. *The Fundamental Frequency of Voice as a Potential Stress Biomarker: A Systematic Review and Meta-Analysis.* Stress and Health (2025). PMID 41102940. https://pubmed.ncbi.nlm.nih.gov/41102940/
- Low DM, Bentley KH, Ghosh SS. *Automated assessment of psychiatric disorders using speech: A systematic review.* Laryngoscope Investigative Otolaryngology (2020). PMID 32128436. https://pubmed.ncbi.nlm.nih.gov/32128436/

See [RESEARCH_NOTES.md](RESEARCH_NOTES.md) for the measurement-to-construct map and failure conditions.

## Status

Browser prototype and research artifact. The current implementation is useful for studying interaction design, multimodal signal visualization, measurement reliability, and the limits of inference. It is not presented as a validated psychological, forensic, biometric-diagnostic, or deception-detection instrument.

Repository: https://github.com/Joenasriani/facial-gesture-interpretation-engine
