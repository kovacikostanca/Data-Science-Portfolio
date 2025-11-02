<h1 align="center">Airbnb Data Cleaning & EDA</h1>
<h3 align="center">Data Cleaning and Preprocessing of Airbnb Reviews: Insights from Inside Airbnb Datasets</h3>

<p align="center">
  <img src="Airbnb_image.jpg" alt="Description" width="400">
</p>

---

## Project Objective
The primary objective of this project is to **clean, preprocess, and integrate Airbnb listings and reviews datasets** from Inside Airbnb to enable meaningful analysis.

This includes preparing the data for tasks such as **sentiment analysis, host performance evaluation, and market trend analysis**.

By addressing **missing values, inconsistencies, and data quality issues**, the project aims to provide a **reliable and structured dataset** for actionable insights.

---

## Datasets
**Source:** [Inside Airbnb](https://insideairbnb.com/get-the-data/)

The project uses two main datasets:

### 1. Listings Dataset
Contains information about Airbnb properties, including:

- Listing ID  
- Host ID and details  
- Property type  
- Location (latitude, longitude, neighborhood)  
- Price, availability, minimum stay  
- Ratings and review scores  

### 2. Reviews Dataset
Contains historical reviews for listings:

- Review ID  
- Listing ID  
- Reviewer ID and name  
- Date of review  
- Review text  

**Timeframe:** The latest available dataset for the selected city (e.g., New York, London, etc.)

---

## Project Scope
The project encompasses the following main tasks:

### A. Data Cleaning
- **Handling Missing Values:** Identify and impute or remove missing values in critical columns (e.g., price, review text, listing ID).  
- **Removing Duplicates:** Ensure unique entries for listings and reviews.  
- **Data Type Corrections:** Convert columns to appropriate types (e.g., dates to datetime, prices to numeric).  
- **Consistency Checks:** Standardize categorical variables (e.g., property types, neighborhoods).

### B. Data Preprocessing
**Text Preprocessing (Reviews):**
- Remove punctuation, special characters, and stopwords  
- Normalize text (lowercasing, stemming/lemmatization)  
- Handle emojis or special symbols if required  

**Date Processing:**
- Convert review dates to datetime objects  
- Extract features like month, year, or day of the week  

**Price Normalization:**
- Remove currency symbols, commas, and convert to float  

**Feature Engineering:**
- Average rating per host or listing  
- Review length (number of words/characters)  
- Sentiment score of reviews using NLP techniques  

**Merging Datasets:**
- Combine listings and reviews datasets on `listing_id` to create an enriched dataset for analysis

### C. Data Quality Assurance
- Identify outliers (e.g., extremely high prices, unrealistic review counts)  
- Validate merged datasets maintain integrity (no mismatched or missing IDs)

---

## Tools and Technologies
- **Programming Language:** Python  
- **Libraries:**  
  - Data manipulation: `pandas`, `numpy`  
  - Text preprocessing: `nltk`, `spaCy`, `re`  
  - Visualization & EDA: `matplotlib`, `seaborn`, `plotly`  
- **Optional:** Jupyter Notebook or Google Colab for interactive workflow

---

## Expected Outcomes
- A **cleaned and preprocessed dataset** ready for analysis and modeling  
- Insights on:  
  - Listing distribution across neighborhoods and property types  
  - Review patterns and trends  
  - Host performance and guest satisfaction  
  - Textual insights from reviews, including sentiment and keywords  
- Documentation of **data cleaning steps** for reproducibility

---

## Extensions (Optional Future Work)
- Sentiment analysis on review text  
- Predictive modeling (e.g., predicting listing ratings or price)  
- Market analysis and trends over time  
- Visualization dashboards for Airbnb trends in the selected city

