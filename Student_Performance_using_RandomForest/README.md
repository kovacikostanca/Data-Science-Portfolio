# Student Exam Performance Prediction

## Project Overview
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

---

## Methodology

1. **Data Preprocessing**
   - Categorical variables encoded using `LabelEncoder`.  
   - Numerical features scaled using `StandardScaler` (for Logistic Regression).  
   - Removed non-predictive columns (`StudentID`) and target-related columns (`GPA`, `GradeClass`) from features.  

2. **Model Training**
   - Random Forest Classifier used for robust predictions.  
   - Logistic Regression can be used optionally for comparison.  

3. **Evaluation**
   - Metrics: Accuracy, Confusion Matrix, Precision, Recall, F1-score.  
   - Stratified train/test split preserves pass/fail ratio.  

4. **Interpretability**
   - SHAP (SHapley Additive exPlanations) used to identify **key drivers** of predictions for each student.  
   - Each student in the test set has:  
     - Actual outcome (Pass / No Pass)  
     - Predicted outcome  
     - Probability of passing  
     - Top 3 features influencing the prediction  

---

## Findings
- **Key Predictors:** Weekly study time, parental support, tutoring, and attendance strongly influence passing.  
- **Lesser Impact:** Extracurricular activities, sports, and volunteering have minimal influence.  
- **Implication:** Both academic effort and parental involvement are critical; educators can focus interventions on students with low study time or low parental support.  
