# Medical Student Mental Health - Domain Knowledge & Data Dictionary

This document serves as a quick reference guide explaining the clinical, psychometric, and demographic variables in the dataset collected by **Carrard et al. (2022)**.

---

## 1. Primary Targets

### `cesd_depression_score` & `cesd_depression_risk`
* **Full Name:** Center for Epidemiologic Studies Depression Scale (**CES-D**)
* **What it measures:** Frequency and severity of depressive symptoms over the past week (sadness, feelings of worthlessness, fatigue, sleep disturbances).
* **Scale Range:** `0 to 60`
* **Clinical Cutoff ($\ge 16$):**
  - **High Risk ($\ge 16$):** Standard clinical benchmark indicating clinically significant depressive distress.
  - **Normal ($< 16$):** Below clinical depression screening threshold.
* **Target Usage:**
  - **Classification Target:** `cesd_depression_risk` (`High Risk (>=16)` vs `Normal (<16)`).
  - **Regression Target:** `cesd_depression_score` (continuous 0–60).

---

## 2. Psychological & Mental Health Scales (Key Predictors)

### `stai_trait_anxiety_score`
* **Full Name:** State-Trait Anxiety Inventory (**STAI-T**)
* **What it measures:** **Trait Anxiety** — a student's baseline disposition to experience anxiety, tension, nervousness, and worry as a stable personality trait (rather than temporary situational panic).
* **Clinical Interpretation:** Higher score = higher chronic anxiety. Often strongly co-morbid with depression.

### `mbi_burnout_emotional_exhaustion`
* **Full Name:** Maslach Burnout Inventory — Emotional Exhaustion (**MBI-EE**)
* **What it measures:** Feelings of being emotionally overextended and depleted by study/clinical demands. Core hallmark of medical burnout.
* **Interpretation:** Higher score = severe emotional fatigue.

### `mbi_burnout_cynicism`
* **Full Name:** Maslach Burnout Inventory — Cynicism / Depersonalization (**MBI-CY**)
* **What it measures:** An indifferent, detached, or callous attitude toward medical studies, peers, and patients.
* **Interpretation:** Higher score = higher detachment and loss of idealism.

### `mbi_burnout_academic_efficacy`
* **Full Name:** Maslach Burnout Inventory — Academic Efficacy (**MBI-EA**)
* **What it measures:** Feelings of competence, academic achievement, and self-belief in medical school.
* **Interpretation:** **Higher score is healthy/protective**. Lower score indicates feeling incompetent or ineffective.

---

## 3. Empathy & Cognitive Emotional Measures

### `jspe_empathy_score`
* **Full Name:** Jefferson Scale of Physician Empathy (**JSPE**)
* **What it measures:** Attitudes toward empathy specifically within the doctor-patient relationship in patient-care situations.
* **Interpretation:** Higher score = higher orientation toward empathic patient care.

### `qcae_cognitive_empathy` & `qcae_affective_empathy`
* **Full Name:** Questionnaire of Cognitive and Affective Empathy (**QCAE**)
* **Two subscales:**
  1. **Cognitive Empathy (`qcae_cognitive_empathy`):** The intellectual ability to understand another person's perspective or emotional state without necessarily feeling it ("I can see why you feel that way").
  2. **Affective Empathy (`qcae_affective_empathy`):** The automatic emotional resonance with someone else's feelings ("I feel your distress inside myself"). High affective empathy without coping skills can lead to compassion fatigue.

### `gert_emotion_recognition_rate`
* **Full Name:** Geneva Emotion Recognition Test (**GERT**)
* **What it measures:** Objective ability to accurately recognize human emotions from dynamic, multimodal video clips (facial expressions, vocal cues, body postures).
* **Value:** Percentage accuracy from `0.0 to 1.0` (e.g. `0.7381` = 73.81% accuracy).

### `amsp_meaning_in_patient_care`
* **Full Name:** Appraisal of "Meaning" in Patient Care (**AMSP**)
* **What it measures:** How much personal meaning, motivation, and satisfaction the student derives from caring for patients.
* **Interpretation:** Higher score = higher sense of purpose in the medical vocation.

---

## 4. Academic, Demographic & Lifestyle Factors

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `student_id` | Identifier | Unique anonymized participant ID. |
| `age` | Numeric | Age of the student at the time of the survey. |
| `curriculum_year` | Categorical | Pre-clinical to clinical stages: `Bachelor 1 (Bmed1)` to `Master 3 (Mmed3)`. |
| `gender` | Categorical | `Male`, `Female`, `Non-binary`. |
| `native_language` | Categorical | Mother tongue (French, German, English, Arabic, etc.). |
| `has_partner` | Binary (`Yes`/`No`) | Relationship status. |
| `has_job` | Binary (`Yes`/`No`) | Whether the student maintains paid employment alongside medical studies. |
| `weekly_study_hours` | Numeric | Self-reported extra study hours per week outside of formal lectures/rotations. |
| `health_satisfaction` | Categorical | 5-point Likert scale from `Very dissatisfied` to `Very satisfied`. |
| `health_satisfaction_score` | Numeric (1–5) | Numeric version of health satisfaction for regression/correlation models. |
| `consulted_psychotherapist_past_year` | Binary (`Yes`/`No`) | Whether the student visited a therapist/psychiatrist in the past 12 months. |

---

## 5. Quick Hypotheses to Investigate in EDA

1. **Anxiety & Depression Link:** Does `stai_trait_anxiety_score` show the strongest correlation with `cesd_depression_score`?
2. **Burnout Profile:** Are students in `Bmed1` (1st year Bachelor) experiencing high exhaustion, or do clinical students (`Mmed3`) suffer more from cynicism?
3. **Protective Factors:** Does high `mbi_burnout_academic_efficacy` or `amsp_meaning_in_patient_care` correlate with significantly lower depression risk?
4. **Empathy Vulnerability:** Does high `qcae_affective_empathy` correlate with higher emotional exhaustion?

