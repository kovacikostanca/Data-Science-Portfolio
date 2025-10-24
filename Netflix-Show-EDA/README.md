# Netflix Titles EDA

<div align="center">
  <img src="https://github.com/kovacikostanca/Data-Science-Portfolio/blob/main/Netflix-Show-EDA/Netflix-EDA.png" alt="Netflix EDA" width="400"/>
</div>

---

## Overview
This project performs **Exploratory Data Analysis (EDA)** on the Netflix Shows Dataset to uncover trends in content by **country, year, genre, and type** (Movies vs TV Shows).  

**Key Highlights:**

- Movies vs TV Shows distribution  
- Content growth over years and Netflix release year  
- Top countries producing Netflix content  
- Genre popularity analysis  
- Ratings and duration trends  
- KPI dashboard summarizing the dataset  

---

## Dataset
- **Source:** [Kaggle – Netflix Shows Dataset](https://www.kaggle.com/datasets/infamouscoder/dataset-netflix-shows)  
- **Rows:** 8,807 (Movies & TV Shows)  
- **Columns:** 12  

**Sample Columns:**

| Column | Description |
|--------|-------------|
| type | Movie / TV Show |
| title | Name of the content |
| country | Country of production |
| release_year | Original release year |
| rating | TV/Film rating |
| duration | Minutes (movies) / Seasons (TV shows) |
| listed_in | Genre categories |
| description | Content synopsis |

---

## Dataset KPIs

<div align="center">
  <img src="images/netflix_kpis.png" alt="Netflix KPIs" width="600"/>
</div>

- **Total Titles:** 8,706  
- **Movies:** 6,131  
- **TV Shows:** 2,578  
- **Countries:** 746  
- **Unique Genres:** 36  

---

## Exploratory Data Analysis

### 1. Movies vs TV Shows
<div align="center">
  <img src="images/type_distribution.png" alt="Movies vs TV Shows" width="600"/>
</div>

- Movies dominate the Netflix catalog (~70%)  
- TV shows growth is accelerating, especially in **2019–2020**  

---

### 2. Content Growth Over Time

**By Original Release Year**

<div align="center">
  <img src="images/release_year_trends.png" alt="Release Year Trends" width="600"/>
</div>

**By Netflix Addition Year**

<div align="center">
  <img src="images/year_added_trends.png" alt="Netflix Release Year Trends" width="600"/>
</div>

- Sharp increase in content added during **pandemic years**  

---

### 3. Top Content-Producing Countries

<div align="center">
  <img src="images/top_countries.png" alt="Top Countries" width="600"/>
</div>

- **United States** and **India** lead content production  

---

### 4. Genre Analysis

<div align="center">
  <img src="images/top_genres.png" alt="Top Genres" width="600"/>
</div>

- Most popular genres: **Dramas, Comedies, Documentaries, Action & Adventure**  

---

### 5. Ratings & Durations

**Rating Distribution**

<div align="center">
  <img src="images/rating_distribution.png" alt="Rating Distribution" width="600"/>
</div>

**Movie Duration Distribution**

<div align="center">
  <img src="images/movie_duration.png" alt="Movie Duration Distribution" width="600"/>
</div>

- Most content is **TV-MA or TV-14**  
- Movie durations peak around **90–110 minutes**  

---

## Key Insights
- Netflix catalog is **movie-heavy**, but TV shows are rapidly increasing  
- **United States** and **India** dominate production  
- **Dramas, Comedies, and Documentaries** are the most popular genres  
- Ratings and durations reflect targeted audience segments  
- **Pandemic years (2019–2021)** show significant content growth  

---

## Tech Stack
- **Python** – data analysis and visualization  
- **Pandas & NumPy** – data manipulation  
- **Matplotlib & Seaborn** – visualizations  
