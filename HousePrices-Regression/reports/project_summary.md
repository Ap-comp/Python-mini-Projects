# 🏠 House Prices Regression Project

📅 **Completed on:** 14 October 2025\
👨‍💻 **Author:** Abhishek Patil

------------------------------------------------------------------------

## 🎯 Project Objective

The goal of this project was to predict house prices using a dataset of
property characteristics.\
This end-to-end regression pipeline demonstrates feature engineering,
data preprocessing, model training, hyperparameter tuning, and final
predictions for Kaggle submission.

------------------------------------------------------------------------

## 🧩 Workflow Summary

  ------------------------------------------------------------------------
  Stage          Description                   Tools Used
  -------------- ----------------------------- ---------------------------
  1\. Data       Cleaned and transformed raw   pandas, scikit-learn
  Preparation    housing data, handled missing 
                 values, standardized          
                 numerical columns, and        
                 encoded categorical columns.  

  2\. Feature    Added derived columns such as pandas
  Engineering    `TotalSF`, `Age`, `RemodAge`, 
                 and `TotalPorchSF` to enhance 
                 model performance.            

  3\. Model      Implemented Linear            scikit-learn, xgboost
  Building       Regression, Random Forest,    
                 and XGBoost for baseline      
                 comparisons.                  

  4\. Model      Used `RandomizedSearchCV` to  scikit-learn
  Tuning         find optimal hyperparameters  
                 for XGBoost.                  

  5\. Final      Retrained the tuned model on  scikit-learn Pipeline
  Training       full data and generated       
                 predictions for the test      
                 dataset.                      

  6\. Evaluation Compared models using RMSE on numpy, scikit-learn
                 validation data; XGBoost      
                 delivered the best            
                 performance.                  

  7\. Output     Saved final predictions to    joblib, json
                 `submission.csv` and deployed 
                 results to GitHub for         
                 portfolio presentation.       
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## ⚙️ Model Performance

  Model                 Validation RMSE   Remarks
  --------------------- ----------------- -----------------------
  Linear Regression     \~0.152           Baseline model
  Random Forest         \~0.145           Good generalization
  **XGBoost (Tuned)**   **\~0.140**       Best performing model

> 🧠 Note: Actual RMSE values may vary slightly based on the random
> state and data cleaning choices.

------------------------------------------------------------------------

## 📊 Key Parameters (Best Model)

``` json
{
  "n_estimators": 600,
  "max_depth": 5,
  "learning_rate": 0.05,
  "subsample": 0.8,
  "colsample_bytree": 0.8,
  "min_child_weight": 3
}
```

------------------------------------------------------------------------

## 📁 Artifacts Generated

  File                                Description
  ----------------------------------- -----------------------------------------
  `models/xgb_best.joblib`            Trained model (tuned version)
  `models/xgb_final_model.joblib`     Final model trained on full data
  `reports/best_params.json`          Hyperparameters used for final training
  `output/submission.csv`             Final Kaggle-style submission file
  `reports/project_summary.md`        This file (final project summary)

------------------------------------------------------------------------

## 💡 Key Learnings

-   Building modular pipelines keeps code reproducible and easy to
    debug.\
-   Hyperparameter tuning significantly improves performance (XGBoost vs
    baseline).\
-   Log-transforming target variables (`np.log1p()`) improves model
    stability.\
-   OneHotEncoder with `handle_unknown='ignore'` prevents
    unseen-category errors.\
-   RMSE is a better metric than accuracy for regression-based ML
    problems.

------------------------------------------------------------------------

## 🧠 Next Steps

-   Apply the same pipeline design to a **Classification Problem
    (Titanic)**.\
-   Experiment with **feature importance visualization** using
    `xgb.plot_importance()`.\
-   Try deploying this model to **AWS SageMaker** during the AWS ML
    Foundations phase (Nov 2025).

------------------------------------------------------------------------

## 🏁 Project Status

✅ Completed --- **House Prices Regression Project** (End-to-End)\
📦 Ready for Portfolio Showcase (GitHub + LinkedIn)
