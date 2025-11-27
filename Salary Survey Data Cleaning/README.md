<h1><center>
  Salary Survey Data Cleaning Project
</h1></center>

## Project Overview
This project focuses on cleaning and preparing a *Salary Survey Dataset* for further exploratory and statistical analysis.  
The goal was to transform a messy, incomplete dataset into a consistent, structured, and analysis-ready form.

This project demonstrates essential real-world data skills:
- Identifying and fixing data quality issues  
- Handling missing and duplicated values  
- Standardizing categorical and numerical fields  
- Cleaning inconsistent column/value formats  
- Ensuring proper data types for analysis

---

## Dataset Description
Columns visible in the dataset include (:contentReference[oaicite:2]{index=2}):

- `company location`
- `company size`
- `company type`
- `experience level`
- `gender`
- `job title`
- `salary`
- `salary currency`
- `salary in usd`  
*(some columns contain missing values as shown in the raw head of the dataset)* 

The raw dataset contained:
- Missing categorical fields  
- Inconsistent formatting in column and raw values  
- Typos and variations in titles  
- Mixed data types  
- Duplicated entries  

---

## Data Cleaning Steps
### 1. **Missing Values**
- Identified missing entries across columns such as job title, company type, and salaries.
- Removed unusable rows and imputed values when appropriate.

### 2. **Duplicate Handling**
- Searched for and removed duplicate rows to ensure integrity.

### 3. **Categorical Cleaning**
- Standardized text formatting (lowercasing, trimming whitespace).
- Normalized inconsistent job titles.
- Unified experience level categories.

### 4. **Salary Cleaning**
- Converted salary values to consistent numeric format.
- Ensured all salaries were properly converted to USD where needed.
- Standardized currency fields.

### 5. **Data Type Fixes**
- Converted salary columns to numeric types.
- Ensured categorical columns were encoded consistently.

---

## Tools & Technologies
- **Python**
- **Pandas**
- **NumPy**
- **Jupyter Notebook / HTML Export**

---

## Output
- Clean, structured dataset ready for EDA.
- Columns standardized and validated.
- Salary information harmonized into USD.
- Missing, duplicated, and inconsistent values handled.

---

## Key Learnings
- Real-world data is messy—cleaning is critical before any analysis.
- Designing a systematic workflow leads to reliable datasets.
- Small cleanup decisions can significantly affect downstream insights.

---

## Next Steps
- Exploratory Data Analysis (EDA)
- Visualization of salary trends across:
  - Job titles  
  - Experience levels  
  - Company sizes  
  - Company locations  
- Building a dashboard with meaningful salary insights.

