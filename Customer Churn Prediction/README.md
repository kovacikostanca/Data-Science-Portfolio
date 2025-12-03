<h1 align="center">Customer Churn Prediction</h1>
<h3 align="center">Telco BMI Dataset</h3>

<p align="center">
  <img src="customer_churn.jpg" alt="Description" width="400">
</p>

### Project Objective

Predict customer churn and provide actionable business insights to reduce attrition and increase retention.

---

### Dataset

Telco Customer Churn dataset (7,049 customers, 21 features).
- Link: https://github.com/IBM/telco-customer-churn-on-icp4d/tree/master/data

---

### 1. Data Understanding
#### 1.1 Overview

|Metric|Value|
|------|--------|
|Number of rows|7,043|
|Number of features|21|
|Target variable|Churn(Yes/No)|
|Churn rate|26.5% Yes, 73.5% No|

#### 1.2 Feature Types
- **Categorical**:
  - gender
  - Partner
  - Dependents
  - PhoneService
  - MultipleLines
  - InternetService
  - OnlineSecurity
  - OnlineBackup
  - DeviceProtection
  - TechSupport
  - StreamingTV
  - StreamingMovies
  - Contract
  - PaperlessBilling
  - PaymentMethod
  - Churn

- **Numerical**:
  - tenure
  - MonthlyCharges
  - TotalCharges (converted to numerical after cleaning)
 
#### 1.3 Missing Values

- Initial missing values in TotalCharges fixed by conversion to numeric and imputation.
- No other missing values detected.

#### 1.4 Observations

- Dataset is imbalanced (churners ~27%).
- Categorical features need encoding for ML models.
- customerID is unique identifier and not used as a feature.

---

### 2. Data Preprocessing and Feature Engineering
#### 2.1 Preprocessing Steps

- Converted TotalCharges from object to float after handling empty strings.
- Encoded categorical variables:
  - Binary categories: Label Encoding (e.g., Yes=1, No=0)
  - Multi-class categories: One-Hot Encoding (e.g., InternetService, PaymentMethod)
- Dropped customerID as it is non-predictive.

#### 2.2 Feature Engineering

- Created dummy variables for categorical features.
- Checked for outliers → none significant.
- Split data into train (80%) / test (20%) sets.

#### 2.3 Optional Steps Considered

- Scaling numerical features → optional for tree-based models (XGBoost).
- SMOTE or class weighting → considered for future improvement.

---

### 3. Model Development
#### 3.1 Logistic Regression 

|Metric|Value|
|------|-----|
|Accuracy|	0.80|
|Churn Precision|	0.64|
|Churn Recall|	0.54|
|F1-score (Churn)|	0.58|

**Confusion Matrix**

|Actual \ Predicted|	No churn (0)|	Churn (1)|
|------------------|--------------|----------|
|No churn (0)|	917|	116|
|Churn (1)|	172|	202|

- **Strengths**: Interpretable, good overall accuracy.
- **Weakness**: Misses many churners (high false negatives).

---

#### 3.2 XGBoost

|Metric|	Value|
|------|-------|
|Accuracy|	0.74|
|Churn Precision|	0.51|
|Churn Recall|	0.69|
|F1-score (Churn)|	0.59|

**Confusion Matrix**

|Actual \ Predicted|	No churn (0)|	Churn (1)|
|------------------|--------------|----------|
|No churn (0)|	782|	251|
|Churn (1)|	115|	259|

**Top 10 Features (Importance)**
1. Contract type (Month-to-month)
2. Tenure
3. MonthlyCharges
4. Fiber optic InternetService
5. TechSupport
6. OnlineSecurity
7. OnlineBackup
8. StreamingTV
9. DeviceProtection
10. PaymentMethod

**Insights:**

- XGBoost captures more churners (higher recall) → better for retention campaigns.
- Slightly lower precision → some false positives (non-churners targeted).
- Important features align with business intuition.

---

### 4. Business Recommendations

**1. Target high-risk customers:**
- Month-to-month contracts, short tenure (<12 months), high MonthlyCharges.

**2. Retention campaigns:**
- Personalized offers: discounts, loyalty rewards, service bundles.
- Upsell TechSupport and OnlineSecurity services.

**3. Service improvements:**
- Improve fiber optic internet quality.
- Enhance support responsiveness.

**4. Monitoring & Continuous Improvement:**
- Track campaign success and customer response.
- Retrain models quarterly with updated data.

**Expected Impact:**
- Reduces missed churners, maximizes retention ROI.
- Helps prioritize marketing resources efficiently.

---

### Conclusion 

The project successfully identifies high-risk customers and key drivers of churn. XGBoost is the recommended model for retention efforts. By combining predictive insights with actionable strategies, the company can proactively reduce churn and increase customer lifetime value.

### Customer Churn Analysis

Our analysis of the telecom customer base reveals that churn is primarily driven by a combination of service-related and contractual factors. Using Logistic Regression and XGBoost models, we achieved strong predictive performance, with XGBoost identifying key churn drivers such as contract type, tenure, monthly charges, and fiber-optic internet service. Customers on month-to-month contracts, with shorter tenure and higher monthly charges, show the highest risk of churn. These insights highlight clear business opportunities: strengthening retention incentives for early-tenure customers, promoting longer-term contract options, and optimizing pricing or service bundles for high-cost segments. Implementing these targeted strategies is expected to improve customer retention efficiency and reduce churn-related revenue loss.
