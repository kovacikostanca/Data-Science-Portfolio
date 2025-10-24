# House Price Prediction Using Linear and Polynomial Regression

<img src="https://github.com/kovacikostanca/Data-Science-Portfolio/blob/main/house-price-prediction/housingcosts.jpg" alt="House Price Prediction" width="400" style="display: block; margin-left: auto; margin-right: auto;">


## Overview

This project implements a machine learning pipeline to predict housing prices based on various socioeconomic and structural property features.  
It demonstrates fundamental concepts in regression analysis, model evaluation, and ML best practices.

The pipeline highlights:

- **Linear Regression** as a baseline model.  
- **Polynomial Regression** with degrees 2, 3, and 4.  
- **Bias–variance tradeoff analysis** using residuals and R² metrics.  
- **Coefficient stability evaluation** via bootstrapping.  
- **Predictions on unseen housing data**.

---

## Dataset

The dataset (`house_data.zip`) contains **400 houses** and **11 features** with the following features:

| Feature               | Description                                  |
|-----------------------|----------------------------------------------|
| Crime                 | Per capita crime rate                         |
| Residential           | Proportion of residential land zoned for large lots |
| NonRetail             | Proportion of non-retail business acres per town |
| NitricOxides          | Nitric oxides concentration (parts per 10 million) |
| Rooms                 | Average number of rooms per dwelling         |
| Age                   | Proportion of houses built before 1940      |
| Distance              | Weighted distances to employment centres     |
| Accessibility         | Index of accessibility to highways           |
| Tax                   | Full-value property-tax rate per $10,000     |
| PupilTeacher          | Pupil–teacher ratio                          |
| DisadvantagedPosition | % lower status of the population             |
| Price                 | Target variable (house price in dollars)    |

> The dataset is already cleaned and ready for modeling.

---

## Methods

### 1. Linear Regression

- **Train/Test Split:** 80/20  
- **Metrics:** R², MSE, RMSE  

**Performance:**

| Metric | Training | Testing |
|--------|----------|---------|
| R²     | 0.731    | 0.749   |
| MSE    | 25.906   | 20.392  |
| RMSE   | 5.090    | 4.516   |

**Feature Impact:**

| Feature               | Coefficient | Interpretation                              |
|-----------------------|------------|--------------------------------------------|
| Rooms                 | +3.5       | Each additional room increases price       |
| Age                   | +0.0026    | Older houses slightly increase price       |
| Distance              | -1.38      | Further from employment lowers price       |
| Accessibility         | +0.26      | Better access slightly increases price     |
| Tax                   | -0.011     | Higher taxes slightly reduce price         |
| DisadvantagedPosition | -0.64      | Houses in disadvantaged areas are cheaper |
| Crime                 | -0.124     | Higher crime lowers prices                 |
| NitricOxides          | -16.6      | Pollution significantly lowers prices      |
| PupilTeacher          | -1.09      | Poor school quality reduces price          |
| Residential           | +0.04      | Higher residential area slightly increases price |
| NonRetail             | +0.073     | More non-retail areas slightly increase price |

> Linear regression provides a solid baseline with interpretable coefficients.

---

### 2. Polynomial Regression

Tested polynomial degrees: 2, 3, 4.  

**Performance:**

| Degree | R² (Train/Test) | RMSE (Test) | Verdict            |
|--------|----------------|-------------|------------------|
| 2      | 0.920 / 0.872  | 3.22        | Best fit          |
| 3      | 1.000 / -38622 | 1771.05     | Overfit           |
| 4      | 1.000 / -658   | 231.44      | Overfit           |

**Takeaways:**

- Degree 2 polynomial achieves **optimal bias-variance tradeoff**.  
- Degrees 3 and 4 severely overfit, showing **high variance**.  
- Coefficient stability via **bootstrapping** confirms degree 2 as reliable.  

---

### 3. Bias–Variance Analysis

| Model                  | Bias | Variance | Comment                           |
|------------------------|------|----------|----------------------------------|
| Linear Regression      | Low  | Moderate | Solid baseline                   |
| Polynomial Degree 2    | Low  | Low      | Optimal tradeoff                 |
| Polynomial Degrees 3-4 | Low  | Very High| Overfitting, unstable coefficients |

---

### 4. Predictions on Unseen Data

Predictions generated for new housing records (`house_unseen.csv`):

| Rooms | Age  | Distance | Tax | Predicted Price |
|-------|------|----------|-----|----------------|
| 6.44  | 8.9  | 7.39     | 330 | 25.85          |
| 7.87  | 32.0 | 5.65     | 255 | 41.06          |
| 6.40  | 100  | 1.64     | 666 | 17.24          |

---

## Visualizations

### 1. Actual vs Predicted Prices

![Actual vs Predicted](https://github.com/kovacikostanca/Data-Science-Portfolio/blob/main/house-price-prediction/actual_vs_predicted.png)

### 2. Training vs Testing Comparison

![Training vs Testing](https://github.com/kovacikostanca/Data-Science-Portfolio/blob/main/house-price-prediction/train_test_comparison.png)

> Visualizations show how close the models are to real house prices.

---

## Key Insights

- **Polynomial Degree 2** gives best tradeoff between bias and variance.  
- **Linear Regression** is interpretable: more rooms → higher price, more crime → lower price.  
- Higher-degree polynomials overfit, highlighting the **bias–variance tradeoff**.  
- Most impactful features: **Rooms, Nitric Oxides, Crime, Distance**.  

---

## Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  

---

## Future Work

- Include additional features: location, amenities, property age.  
- Explore advanced models: Random Forest, Gradient Boosting, Neural Networks.  
- Deploy a web app for real-time housing predictions.

---

## References

- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)  
- [Kaggle Housing Datasets](https://www.kaggle.com/)  

