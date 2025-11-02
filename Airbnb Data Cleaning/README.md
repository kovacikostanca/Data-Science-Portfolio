<h1 align="center">Airbnb Reviews Data Analysis Project</h1>
<h3 align="center">Data Cleaning and Preprocessing of Airbnb Reviews: Insights from Inside Airbnb Datasets</h3>

<p align="center">
  <img src="Airbnb_image.jpg" alt="Description" width="400">
</p>

## Project Overview
This project performs a comprehensive **Data cleaning, preprocessing, and exploratory analysis** of Airbnb listings and reviews using the [Inside Airbnb](http://insideairbnb.com/get-the-data.html) datasets. The goal is to understand guest sentiment, review patterns, and listing characteristics to extract actionable insights about Airbnb listings and host performance.

---

## Dataset
We use two datasets provided by Inside Airbnb:

1. **Listings dataset** (`listings.csv`)  
   - Contains information about Airbnb listings, including location, property type, price, host information, availability, and ratings.

2. **Reviews dataset** (`reviews.csv`)  
   - Contains user reviews, review dates, and reviewer information.

### Key Columns
- `comments`, `cleaned_comments`, `review_length`, `avg_review_length`  
- `review_scores_rating`, `review_scores_accuracy`, `review_scores_cleanliness`, `review_scores_checkin`, `review_scores_communication`, `review_scores_location`, `review_scores_value`  
- `neighbourhood`, `property_type`, `price`, `reviews_per_month`  

---

## Project Steps

### 1. Data Loading
- Loaded listings and reviews CSV files using `pandas`.
- Verified dataset structure and column names.

### 2. Data Cleaning
- Dropped irrelevant or heavily missing columns such as host biography, profile images, license info, and calendar metadata.
- Handled missing values:
  - Filled numeric features (e.g., ratings, price, bedrooms, bathrooms) with median.
  - Filled review-derived metrics (e.g., `avg_review_length`, `reviews_per_month`) with 0 for listings with no reviews.
  - Filled categorical fields (`neighbourhood`, `property_type`) with `"Unknown"`.
- Removed duplicate or unnecessary columns (e.g., `listing_id_x`, `listing_id_y`).

### 3. Feature Engineering
- Calculated review-derived metrics:
  - `avg_review_length` — average number of words per review.
  - `reviews_per_month` — average reviews per month per listing.
- Prepared sentiment metrics (if sentiment analysis applied).

### 4. Exploratory Data Analysis
Visualizations created using **Matplotlib** and **Seaborn**:

- **Price Analysis**
  - Price distribution across all listings.
  - Price distribution by property type.
- **Review Analysis**
  - Average reviews per month by neighborhood.
  - Review length vs review rating.
- **Correlation Analysis**
  - Correlation heatmap for numeric features such as price, ratings, reviews, and sentiment.

### 5. Potential Next Steps
- **Text Analysis**
  - Word clouds for positive vs negative reviews.
  - N-gram analysis of review content.
- **Predictive Modeling**
  - Predict review scores or listing price.
  - Predict listing popularity based on review activity and features.
- **Interactive Dashboard**
  - Use Plotly or Streamlit to create a live dashboard for listing insights.

---

## Technologies Used
- Python 
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `nltk` (for text analysis)
- Jupyter Notebook for workflow and visualization
