# Fake Job Post Detector

A machine learning project that detects **fraudulent job postings** using natural language processing (NLP). The system helps job seekers and platforms identify fake or scam job posts in real time.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Data Preprocessing](#data-preprocessing)
- [Modeling](#modeling)
- [Evaluation & Results](#evaluation--results)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Technologies](#technologies)
- [Author](#author)

---

## Project Overview
Many job seekers fall victim to fake job postings that ask for money, personal information, or mislead candidates. This project uses **NLP and machine learning** to automatically classify job postings as **real** or **fake**.

**Objective:** Predict whether a job posting is fraudulent.

---

## Dataset
- **Source:** [Fake Job Postings Dataset - Kaggle](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)  
- **Rows:** 17,880 job postings  
- **Columns:** 18 features including `title`, `description`, `requirements`, `company_profile`, `telecommuting`, and `fraudulent` (target)  

---

## Features
- **Text Features:** `title`, `description`, `requirements`, `company_profile`, `benefits`  
- **Binary Features:** `telecommuting`, `has_company_logo`, `has_questions`  
- **Target:** `fraudulent` (0 = real, 1 = fake)

---

## Data Preprocessing
- Filled missing text fields with empty strings.  
- Combined relevant text columns into a single `combined_text` column.  
- Text cleaning:
  - Lowercasing  
  - Removing punctuation and numbers  
  - Stopword removal  
  - Lemmatization  
- Vectorized text using **TF-IDF** (1-2 grams, max_features=5000).  
- Included binary features in the final dataset.

---

## Modeling
- **Algorithms Used:**
  - Multinomial Naive Bayes  
  - Logistic Regression  

- **Pipeline:**
  1. Train-test split (80/20)  
  2. Feature extraction (TF-IDF + binary features)  
  3. Model training  
  4. Prediction and evaluation  

---

## Evaluation & Results

### **1. Logistic Regression**

| Class | Description | Precision | Recall | F1-score | Support |
|-------|------------|-----------|--------|----------|--------|
| 0     | Real Job   | 0.97      | 1.00   | 0.99     | 3403   |
| 1     | Fake Job   | 1.00      | 0.41   | 0.58     | 173    |

**Overall Metrics:**  
- Accuracy: 0.97  
- Macro Average: Precision = 0.99, Recall = 0.71, F1-score = 0.78  
- Weighted Average: Precision = 0.97, Recall = 0.97, F1-score = 0.97  

**Interpretation:**  
- **Real jobs (0):** Almost all real jobs are correctly classified (Recall = 1.00).  
- **Fake jobs (1):** Only 41% of fake jobs are detected, but predictions are highly precise (Precision = 1.00).  
- Model is conservative due to **class imbalance** (more real than fake jobs).

---

### **2. Naive Bayes**

| Class | Description | Precision | Recall | F1-score | Support |
|-------|------------|-----------|--------|----------|--------|
| 0     | Real Job   | 0.97      | 0.99   | 0.98     | 3403   |
| 1     | Fake Job   | 0.66      | 0.39   | 0.49     | 173    |

**Overall Metrics:**  
- Accuracy: 0.96  
- Macro Average: Precision = 0.81, Recall = 0.69, F1-score = 0.74  
- Weighted Average: Precision = 0.95, Recall = 0.96, F1-score = 0.96  

**Interpretation:**  
- **Real jobs (0):** Very high precision and recall.  
- **Fake jobs (1):** Lower recall (0.39) and moderate precision (0.66).  
- Naive Bayes is less effective at detecting fake posts due to **feature independence assumptions**.

---

### **Key Insights**
1. Both models perform **very well on real jobs** because it is the majority class.  
2. **Fake job detection is challenging**:
   - Fake posts often mimic real job language.  
   - Imbalanced dataset (3403 real vs 173 fake).  
3. **Logistic Regression outperforms Naive Bayes** for fake job detection, especially in precision.  
4. Misclassifications suggest improvements like **advanced NLP embeddings**, **class balancing**, or **threshold tuning**.
