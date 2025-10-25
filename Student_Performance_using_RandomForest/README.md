# Student Exam Performance Prediction

<div align="center">
  <img src=https://github.com/kovacikostanca/Data-Science-Portfolio/blob/main/Student_Performance_using_RandomForest/student_exam_performance.jpg" alt="Student Exam Performance" width="400"/>
</div>

## Overview
This project predicts whether a student will pass or fail based on demographic, behavioral, and academic features using the **Student Performance Dataset**. The workflow includes **data preprocessing, feature engineering, model training, evaluation, and interpretability**, giving insights not only on which students are at risk but also **why** they are predicted to pass or fail.

---

## Dataset
Columns included in the dataset:

- **StudentID** – unique identifier (not used for modeling)  
- **Age** – student age  
- **Gender** – male/female  
- **Ethnicity** – ethnic background  
- **ParentalEducation** – highest parental education level  
- **StudyTimeWeekly** – hours of study per week  
- **Absences** – number of school absences  
- **Tutoring** – whether the student receives tutoring  
- **ParentalSupport** – level of parental support  
- **Extracurricular, Sports, Music, Volunteering** – participation in activities  
- **GPA** – grade point average (used to define target)  
- **GradeClass** – letter grade  

**Target Variable:**  
- `pass` = 1 if GPA ≥ 2.5, else 0  

**Dataset**

| Category | Column | Description |
|-----------|---------|-------------|
| Identifier | `StudentID` | Unique identifier for each student (1001–3392) |
| Demographics | `Age` | Student age (15–18 years) |
| Demographics | `Gender` | 0 = Male, 1 = Female |
| Demographics | `Ethnicity` | 0 = Caucasian, 1 = African American, 2 = Asian, 3 = Other |
| Family Background | `ParentalEducation` | 0=None, 1=High School, 2=Some College, 3=Bachelor’s, 4=Higher |
| Study Habits | `StudyTimeWeekly` | Weekly study time (0–20 hours) |
| Study Habits | `Absences` | Number of absences (0–30) |
| Academic Support | `Tutoring` | 0=No, 1=Yes |
| Parental Involvement | `ParentalSupport` | 0=None, 1=Low, 2=Moderate, 3=High, 4=Very High |
| Activities | `Extracurricular`, `Sports`, `Music`, `Volunteering` | 0=No, 1=Yes |
| Academic Performance | `GPA` | Grade Point Average (2.0–4.0) |
| Academic Performance | `GradeClass` | 0='A' (≥3.5), 1='B' (3.0–3.5), 2='C' (2.5–3.0), 3='D' (2.0–2.5), 4='F' (<2.0) |

---

## Methodology

1. **Data Preprocessing**
   - Label Encoding applied to categorical variables.
   - Standard Scaling applied to numerical variables (Age, StudyTimeWeekly, Absences).
   - Removed non-predictive (StudentID) and target-related (GPA, GradeClass) columns.
     
2. **Model Training**
   - Trained a Random Forest Classifier for robust predictions.
   - Optionally compared results using Logistic Regression.
   - Performed Stratified Train/Test Split to maintain pass/fail balance. 

3. **Evaluation**
   - Metrics: Accuracy, Confusion Matrix, Precision, Recall, and F1-score.
   - Achieved accuracy: ~0.93 (93%).
  
   Accuracy: 0.929
   Confusion Matrix:
   [[320  18]
   [ 16 125]]

4. **Feature Engineering**
   - Identified key features influencing prediction outcomes:
 
  | Rank	| Feature | Influence |
  |------|---------|-----------|
  |   1	| StudyTimeWeekly	| ⬆️ Strong Positive |
  |   2	| ParentalSupport	| ⬆️ Strong Positive |
  |   3	| Tutoring	| ⬆️ Positive |
  |   4	| Absences	| ⬇️ Negative |
     
5. **Interpretability**
   - Used SHAP (SHapley Additive exPlanations) to understand individual-level predictions.
   - For each student, we list:
       - Actual outcome (Pass/Fail)
       - Predicted outcome
       - Probability of passing
       - Top 3 key drivers of prediction
     
   Example SHAP-based explanation table:

| Actual |	Predicted |	Probability_pass |	Key Drivers |
|--------|------------|------------------|---------------|
| pass |	pass | 	0.92	| Absences ↑ (-1.59), StudyTimeWeekly ↑ (1.63), Tutoring ↓ (0) |
| fail |	fail |	0.01  | Absences ↓ (1.12), ParentalSupport ↓ (0), StudyTimeWeekly ↓ (-0.65) |

---

## Findings
- **Key Predictors:** Weekly study time, parental support, tutoring, and attendance strongly influence passing.  
- **Lesser Impact:** Extracurricular activities, sports, and volunteering have minimal influence.  
- **Implication:** Both academic effort and parental involvement are critical; educators can focus interventions on students with low study time or low parental support.  

---

## Libraries Used

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import shap
import matplotlib.pyplot as plt

---

## Model Results Summary

| Metric | 	Score |
|--------|--------|
| Accuracy |	0.93 |
| Precision (Pass) |	0.87 |
| Recall (Pass) |	0.89 |
| F1-Score (Pass) |	0.88 |

---

## Conclusion

   Using the Student Exam Performance Dataset, we built a predictive model capable of identifying students at risk of failing.
The Random Forest model achieved high accuracy and interpretability using SHAP. Findings emphasize that study time, attendance, and parental involvement are strong predictors of success.

These insights are valuable for educators, policymakers, and parents to create data-driven interventions that improve student outcomes.

---

## Future Work

- Integrate additional features (e.g., socioeconomic status, teacher quality).

- Deploy model as a web dashboard (e.g., with Streamlit or Dash).

- Implement real-time student risk prediction using new data.
