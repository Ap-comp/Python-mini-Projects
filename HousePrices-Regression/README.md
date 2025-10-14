# 🏠 House Prices Regression Project

> Predicting house prices using advanced regression models and
> end-to-end ML pipelines.

------------------------------------------------------------------------

## 📘 Overview

This project is part of my AI/ML Engineer learning journey (October
2025).\
It demonstrates the **complete lifecycle of a regression problem**,
including data preprocessing, feature engineering, model tuning, and
generating final predictions for Kaggle-style submission.

The dataset used is the **Ames Housing Dataset**, known for its detailed
property attributes and price data.

------------------------------------------------------------------------

## 🎯 Objective

To build a robust and explainable regression model that predicts
`SalePrice` of houses using numerical and categorical features.

------------------------------------------------------------------------

## 🧱 Project Structure

    house-prices-regression/
    │
    ├── data/
    │   ├── train.csv
    │   ├── test.csv
    │   
    │   
    │
    ├── notebooks/
    │   ├── 01_Linear_Regression.ipynb
    │   ├── 02_RandomForest_Model.ipynb
    │   ├── 03_Model_Comparison.ipynb
    │   ├── 04_Hyperparameter_Tuning.ipynb
    │   └── 05_Final_Prediction.ipynb
    │
    ├── models/
    │   ├── xgb_best.joblib
    │   └── xgb_final_model.joblib
    │
    ├── reports/
    │   ├── best_params.json
    │   ├── project_summary.md
    │
    │
    ├── output/
    │   └── submission.csv
    │
    ├
    └── README.md

------------------------------------------------------------------------

## ⚙️ Technologies Used

  Category                Tools
  ----------------------- --------------------------------------
  Language                Python 3.13.5
  Libraries               pandas, numpy, scikit-learn, xgboost
  Visualization           matplotlib, seaborn
  Model Tuning            RandomizedSearchCV
  Deployment (upcoming)   AWS SageMaker (Nov 2025 phase)

------------------------------------------------------------------------

## 🚀 Key Steps

1.  **Data Cleaning**
    -   Imputed missing values using median and mode strategies.
    -   Encoded categorical variables via OneHotEncoder.
2.  **Feature Engineering**
    -   Created new derived features like:
        -   `TotalSF` = 1stFlrSF + 2ndFlrSF + TotalBsmtSF
        -   `Age` = YrSold - YearBuilt
        -   `RemodAge` = YrSold - YearRemodAdd
3.  **Model Development**
    -   Linear Regression (baseline)
    -   Random Forest Regressor
    -   XGBoost Regressor (final)
4.  **Hyperparameter Tuning**
    -   Used RandomizedSearchCV on XGBoost.
    -   Evaluated models with RMSE metric.
5.  **Final Submission**
    -   Trained final model on full dataset.
    -   Generated `submission.csv` for Kaggle upload.

------------------------------------------------------------------------

## 📊 Model Performance

  Model                 Validation RMSE   Remarks
  --------------------- ----------------- -------------------------
  Linear Regression     \~0.152           Baseline
  Random Forest         \~0.145           Improved generalization
  **XGBoost (Tuned)**   **\~0.140**       Best overall model

------------------------------------------------------------------------

## 🧠 Key Learnings

-   Importance of end-to-end modular pipelines for reproducibility.\
-   Feature engineering and log transformation drastically affect RMSE.\
-   Tuning hyperparameters using RandomizedSearchCV improved model by
    \~20%.\
-   Validation splits and consistent preprocessing are critical to model
    fairness.\
-   Handling categorical columns safely using `handle_unknown='ignore'`.

------------------------------------------------------------------------

## 🧩 Next Steps

-   Extend this workflow to classification (Titanic / Churn projects).\
-   Deploy the trained XGBoost model on **AWS SageMaker** in the **AWS
    ML Foundations** phase.\
-   Build a dashboard using **Power BI** or **Streamlit** for
    visualization.

------------------------------------------------------------------------

## 🏁 Status

✅ Completed on **14 October 2025**\
📦 Repository ready for **GitHub Portfolio Upload**\

------------------------------------------------------------------------

## 👨‍💻 Author

**Abhishek Patil**\
*Data Analyst → Aspiring AI/ML Engineer*\
📧 [LinkedIn](https://www.linkedin.com/in/abhishek-patil-062153148/) \| [GitHub](https://github.com/Ap-comp)
