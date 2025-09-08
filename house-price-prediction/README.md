# House Price Prediction Using Linear and Polynomial Regression  

## Overview  
This project implements a **machine learning pipeline** to predict housing prices based on various socioeconomic and structural property features.  
The pipeline demonstrates:  

- **Linear Regression** as a baseline model.  
- **Polynomial Regression** with degrees 2, 3, and 4.  
- **Bias–variance tradeoff analysis** using residuals and R² metrics.  
- **Coefficient stability evaluation** via bootstrapping.  
- **Predictions on unseen housing data**.  

This project highlights fundamental concepts in **regression analysis, model evaluation, and ML best practices**.  

---

## Dataset  
The dataset (`house_data.csv`) includes the following features:  

- `Crime` – per capita crime rate  
- `Residential` – proportion of residential land zoned for large lots  
- `NonRetail` – proportion of non-retail business acres per town  
- `NitricOxides` – nitric oxides concentration (parts per 10 million)  
- `Rooms` – average number of rooms per dwelling  
- `Age` – proportion of houses built before 1940  
- `Distance` – weighted distances to employment centres  
- `Accessibility` – index of accessibility to highways  
- `Tax` – full-value property-tax rate per $10,000  
- `PupilTeacher` – pupil–teacher ratio  
- `DisadvantagedPosition` – % lower status of the population  
- `Price` – **target variable** (house price in dollars)  

---

## Methods  

### Linear Regression  
- Train/test split: **80/20**  
- Metrics: **R², MSE, RMSE**  

**Performance:**  
- R² (Train): **0.731**  
- R² (Test): **0.749**  
- RMSE (Test): **4.52**  

Solid baseline with no major overfitting.  

---

### Polynomial Regression  
Tested polynomial features of **degrees 2, 3, and 4**.  

| Degree | R² (Train) | R² (Test) | RMSE (Test) | Verdict |
|--------|------------|------------|--------------|---------|
| **2**  | 0.920      | 0.872      | 3.22         |  Best fit |
| **3**  | 1.000      | -38622.23  | 1771.05      |  Overfit |
| **4**  | 1.000      | -658.56    | 231.44       |  Overfit |

---

### Stability of Coefficients  
- Bootstrapping used to check coefficient variability.  
- **Higher-degree polynomials showed unstable coefficients**, while **degree 2 remained more stable**.  

---

### Bias–Variance Analysis  
- **Linear Regression**: small bias, moderate variance.  
- **Polynomial Degree 2**: optimal balance.  
- **Polynomial Degrees 3 & 4**: severe overfitting, high variance.  

---

### Predictions on Unseen Data  
Generated predictions for new housing records (`house_unseen.csv`).  

Example results:  

| Rooms | Age  | Distance | Tax | Predicted Price |
|-------|------|----------|-----|-----------------|
| 6.44  | 8.9  | 7.39     | 330 | 25.85           |
| 7.87  | 32.0 | 5.65     | 255 | 41.06           |
| 6.40  | 100  | 1.64     | 666 | 17.24           |

---

## Key Insights  
- **Polynomial Degree 2** achieves the best tradeoff between bias and variance.  
- Linear Regression provides interpretable coefficients (e.g., more rooms = higher price, more crime = lower price).  
- Higher-degree polynomials severely overfit, illustrating the **bias–variance tradeoff**.  

---

## Tech Stack  
- **Python**  
- **Pandas, NumPy** for data handling  
- **Matplotlib, Seaborn** for visualization  
- **Scikit-learn** for modeling and evaluation 
