<h1 align='center'>Netflix Content Exploratory Data Analysis (EDA)</h1>

<div align="center">
  <img src="https://github.com/kovacikostanca/Data-Science-Portfolio/blob/main/Netflix-Show-EDA/Netflix-EDA.png" alt="Netflix EDA" width="400"/>
</div>

**From Basic Analysis to Professional Data Storytelling**

A complete end-to-end data analytics project analyzing Netflix's global content catalog to uncover insights about content distribution, trends, and strategic patterns. This project demonstrates professional-level data cleaning, exploratory analysis, and business-focused visual storytelling using Python.

---

# Project Overview

Netflix is one of the world’s leading streaming platforms, offering thousands of movies and TV shows globally. Understanding content distribution and trends can help drive strategic decisions such as:

- Content acquisition strategy  
- Market expansion planning  
- Audience targeting  
- Genre investment prioritization  

This project transforms raw Netflix dataset into actionable insights through structured data analysis and professional visualizations.

---

# Project Objectives

The main goals of this project were to:

- Inspect and understand raw dataset structure  
- Clean and preprocess real-world messy data  
- Perform exploratory data analysis (EDA)  
- Identify key content trends and patterns  
- Create professional visualizations  
- Build portfolio-ready dashboards  
- Present insights clearly for technical and non-technical audiences  

---

# Dataset Information

**Dataset:** Netflix Movies and TV Shows Dataset  
**Source:** [Public dataset (Kaggle)](https://www.kaggle.com/datasets/infamouscoder/dataset-netflix-shows)

### Dataset Features

| Column | Description |
|------|-------------|
| show_id | Unique content identifier |
| type | Movie or TV Show |
| title | Content title |
| director | Director name |
| cast | Actors |
| country | Country of production |
| date_added | Date added to Netflix |
| release_year | Original release year |
| rating | Content maturity rating |
| duration | Length or number of seasons |
| listed_in | Genre categories |
| description | Content summary |

---

# Tools and Technologies Used

**Programming Language**
- Python

**Libraries**
- Pandas → Data manipulation
- NumPy → Numerical operations
- Matplotlib → Visualization
- Seaborn → Advanced visualization

**Environment**
- Jupyter Notebook

---

# Project Workflow

This project follows a professional data analytics pipeline:

---

## 1️⃣ Data Inspection

Initial exploration included:

- Checking dataset shape
- Reviewing column types
- Identifying missing values
- Understanding overall structure

Example:

```python
df.shape
df.info()
df.head()
df.isnull().sum()
```

---

## 2️⃣ Data Cleaning

Cleaning steps included:

- Handling missing values
- Converting date formats
- Standardizing columns
- Removing inconsistencies

Example:

```python
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
```

---

## 3️⃣ Feature Engineering

New features were created to enhance analysis:

Examples:

- year_added
- content_age
- duration categories
- genre grouping

Purpose: Enable deeper insights and trend discovery.

---

## 4️⃣ Exploratory Data Analysis (EDA)

Key business questions explored:

- Movies vs TV Shows distribution
- Content growth over time
- Top content producing countries
- Most common genres
- Rating distribution
- Content addition trends

Example visualization:

```python
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows Distribution")
```

---

## 5️⃣ Data Visualization & Storytelling

Professional visualizations were created to communicate insights clearly.

Visualizations include:

- Content distribution charts
- Yearly growth trends
- Country analysis
- Genre popularity
- Rating distribution

---

# Key Insights

Important findings from the analysis:

- Movies dominate Netflix’s catalog
- Content growth accelerated after 2015
- Certain countries produce significantly more content
- Netflix has rapidly expanded its content library
- Clear trends exist in content type and genre distribution

---

# Business Value

This project demonstrates how data analysis can help streaming platforms:

- Understand content strategy
- Identify growth opportunities
- Support investment decisions
- Improve strategic planning

---

# Skills Demonstrated

- Data Cleaning  
- Exploratory Data Analysis (EDA)  
- Data Visualization  
- Python Programming  
- Data Storytelling  
- Feature Engineering  
- Business Insight Generation  

---

# How to Run This Project

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/netflix-content-eda.git
```

## Step 2: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

## Step 3: Run Notebook

Open the notebook:

```
Netflix_Content_EDA.ipynb
```

---

# Portfolio Purpose

This project was originally created as a basic analysis. It has now been redesigned using professional data analytics standards to demonstrate:

- Professional data analysis workflow  
- Portfolio-ready presentation  
- Business-focused insights  
- Real-world dataset handling  

---

# Future Improvements

Potential enhancements:

- Interactive dashboards (Power BI / Tableau)
- Predictive analysis
- Advanced trend analysis
- Recommendation system exploration

---

# 👤 Author

**Kostanca Kovaci**

Data Analyst | Data Science Enthusiast  

LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/kostanca-kovaci/)  
GitHub: [DataScience_Portfolio](https://github.com/kovacikostanca) 

---

# ⭐ If you found this project useful, please consider starring the repository!
