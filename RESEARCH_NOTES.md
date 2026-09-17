# AEON Research Notes

**Updated:** 17 September 2026

This document defines the scientific interpretation boundary for the current AEON browser prototype.

## 1. Measurement-to-construct map

| Current output | Directly supported description | Unsupported without separate validation |
| --- | --- | --- |
| face detection | model detected a face-like region | identity, intent, attention, engagement |
| facial landmarks | model-estimated facial landmark coordinates | emotion, personality, truthfulness |
| expression-category probabilities | face-api.js category scores for the current image | verified emotion or internal affective state |
| horizontal orientation proxy | nose-to-eye landmark geometry changed across frames | eye gaze, attention target, avoidance, deception |
| estimated F0 | rough fundamental-frequency estimate within the implementation's accepted range | stress, arousal, anxiety, deception, diagnosis |
| dBFS signal level | captured microphone level relative to digital full scale | speaking effort, confidence, stress, emotional intensity |
| variability / state changes | numerical variability in the above outputs | psychological instability, masking, cognitive load, incongruence |

## 2. Construct-validity rule

A measured signal and a psychological construct are different variables. A construct may only be added to AEON as an output when there is a defined operationalization, an appropriate ground-truth measure, a study population, a protocol, validation data, known error rates, and stated limits on generalization.

Association is not sufficient. A feature can correlate with a construct in a controlled dataset while remaining unsuitable for inference about a new individual or a different context.

## 3. Facial-expression evidence

Barrett et al. (2019) reviewed evidence on facial movements and emotion inference and found substantial variation across people, situations, and cultures. Similar facial configurations can occur across different emotional and non-emotional contexts. The practical implication for AEON is that expression-model categories should remain model outputs rather than being promoted to verified emotional states.

Bian et al. (2024) review naturalistic facial-expression recognition and emphasize contextual variables and in-the-wild conditions. Rojas Vistorte et al. (2024) likewise identify accuracy, privacy, and cross-cultural validity as continuing challenges for AI-based emotion assessment.

### Failure conditions to preserve

- lighting and camera angle changes
- head pose and occlusion
- cultural and situational variation
- posed versus spontaneous facial behavior
- individual differences
- model-domain mismatch
- multiple faces in the same frame
- no reliable ground-truth emotion label

## 4. Head orientation is not gaze

The current orientation proxy is calculated from the horizontal position of a nose landmark relative to detected eye landmarks. It is therefore a coarse geometric proxy for head orientation in camera coordinates. It does not measure eye rotation, fixation, visual attention, or the object/person being attended to.

The interface should never describe this variable as gaze unless a separately validated eye-tracking method is implemented.

## 5. Voice / acoustic evidence

The current prototype estimates F0 with a simple autocorrelation routine and computes microphone signal level. These are acoustic measurements, not psychological measurements.

de Lacerda Veiga et al. (2025) reported that F0 can increase under stress across experimental studies, but the meta-analysis had substantial heterogeneity and evidence of publication bias; bias adjustment attenuated the pooled effect to nonsignificance. This supports using F0 as a research candidate signal, not as a standalone person-level stress detector.

Low et al. (2020) reviewed automated psychiatric assessment from speech and concluded that speech technology has research potential but requires stronger reproducibility, generalizability, longitudinal validation, and clinically appropriate study design.

### Major acoustic confounds

- speaker anatomy and habitual pitch
- sex/gender and sociolinguistic norms
- age
- language and prosody
- scripted versus spontaneous speech
- microphone hardware and automatic gain control
- room acoustics and background noise
- distance from microphone
- illness, fatigue, hydration, medication, and vocal use
- task demands and conversational context

## 6. Current engineering thresholds

The implementation currently:

- rejects rough F0 estimates outside 60-350 Hz when summarizing a session;
- uses -45 dBFS as a fixed signal-level threshold;
- samples audio approximately every 80 ms;
- samples facial-model output on a roughly 120 ms loop.

These are engineering choices in the prototype. They are not validated clinical or psychological thresholds.

## 7. Multi-person validity

A session summary intended to describe one participant must not pool detections from multiple visible people. Frames containing more than one detected face should therefore be treated as ambiguous for participant-level summary statistics unless identity tracking or explicit participant selection is separately implemented and validated.

Even single-face capture does not establish identity continuity if people enter and leave the frame. The current prototype should therefore be described as a session-level signal observation interface, not a biometric identity tracker.

## 8. Appropriate research questions

The current prototype can legitimately support questions such as:

- How stable are model outputs across repeated sessions under controlled conditions?
- How much do lighting, pose, distance, microphone, and environment change the measurements?
- What is the test-retest variability of the signal features?
- How often do expression-category outputs change under neutral or non-emotional tasks?
- How does a simple head-orientation proxy compare with validated head-pose or eye-tracking measurements?
- How does the simple F0 estimator compare with established acoustic-analysis software?
- What signal-quality criteria are needed before a sample should be included in analysis?

A future study can test psychological hypotheses, but the psychological construct must be measured independently rather than assumed from AEON's sensor/model outputs.

## 9. Explicitly unsupported uses

Do not use AEON to make decisions about:

- deception or truthfulness
- criminality or security threat
- hiring, promotion, or employee suitability
- mental-health diagnosis
- personality
- cognitive ability or cognitive load
- intent or motive
- credibility
- clinical treatment
- legal evidence

## 10. Research anchors

- Barrett LF, Adolphs R, Marsella S, Martinez AM, Pollak SD. *Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Human Facial Movements.* Psychol Sci Public Interest. 2019;20(1):1-68. PMID: 31313636. https://pubmed.ncbi.nlm.nih.gov/31313636/
- Bian Y, Küster D, Liu H, Krumhuber EG. *Understanding Naturalistic Facial Expressions with Deep Learning and Multimodal Large Language Models.* Sensors. 2024;24(1):126. PMID: 38202988. https://pubmed.ncbi.nlm.nih.gov/38202988/
- Rojas Vistorte AO et al. *Integrating artificial intelligence to assess emotions in learning environments: a systematic literature review.* Front Psychol. 2024;15:1387089. PMID: 38966729. https://pubmed.ncbi.nlm.nih.gov/38966729/
- de Lacerda Veiga D et al. *The Fundamental Frequency of Voice as a Potential Stress Biomarker: A Systematic Review and Meta-Analysis.* Stress Health. 2025;41(5):e70112. PMID: 41102940. https://pubmed.ncbi.nlm.nih.gov/41102940/
- Low DM, Bentley KH, Ghosh SS. *Automated assessment of psychiatric disorders using speech: A systematic review.* Laryngoscope Investig Otolaryngol. 2020;5(1):96-116. PMID: 32128436. https://pubmed.ncbi.nlm.nih.gov/32128436/

This is a research-method note, not a systematic review. The references above anchor the current interpretation boundaries; they do not validate AEON itself.
