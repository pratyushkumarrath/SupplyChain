# Supply Chain Analytics using Machine Learning

This repository contains two Machine Learning projects built using a Supply Chain dataset:

1. ETA Prediction (Regression)
2. Delivery Delay Prediction (Classification)

These projects focus on improving logistics efficiency and shipment planning using predictive analytics.

---

# Project Overview

## 1. ETA Prediction

### Objective
Predict the Estimated Time of Arrival (ETA) for product shipments.

### Problem Type
Regression

### Target Variable
- `Days for shipping (real)`

### Important Note
`Shipping date` is used only for target generation and NOT as a training feature to avoid data leakage.

### Features Used
- Category Id
- Category Name
- Department Id
- Department Name
- Latitude
- Longitude
- Market
- Order City
- Order Country
- Order Date
- Order Item Quantity
- Order Region
- Order State
- Product Card Id
- Product Category Id
- Product Description
- Product Name
- Product Status
- Shipping Mode
- Days for shipment (scheduled)

### Feature Engineering
- Month
- Day of week
- Weekend flag
- Holiday season
- Week of year

### Algorithms
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor

### Evaluation Metrics
- MAE
- RMSE
- R² Score

---

## 2. Delivery Delay Prediction

### Objective
Predict whether a shipment will be delayed.

### Problem Type
Classification

### Target Variable
- `Late_delivery_risk`

### Features Used
- Days for shipment (scheduled)
- Shipping Mode
- Market
- Order Region
- Order State
- Latitude
- Longitude
- Product Status
- Order Item Quantity
- Product Category Id
- Order Date
- Department Id

### Feature Engineering
- Holiday season
- Weekend order
- Month
- Day of week
- Distance-based features

### Algorithms
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- CatBoost Classifier

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

# Dataset

The dataset contains supply chain and logistics information including:
- customer details
- product information
- shipping details
- geographical data
- order information

---

# Data Preprocessing

The following preprocessing steps were applied:
- Missing value handling
- Categorical encoding
- Date feature extraction
- Feature scaling
- Data leakage prevention
- Feature selection

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- CatBoost
- Matplotlib
- Seaborn

---

# Project Structure

```bash
Supply-Chain-ML/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── eta_prediction.ipynb
│   └── delay_prediction.ipynb
│
├── models/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train_eta.py
│   └── train_delay.py
│
├── requirements.txt
├── README.md
└── .gitignore