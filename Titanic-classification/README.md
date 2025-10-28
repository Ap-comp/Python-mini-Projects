# 🚢 Titanic Survival Prediction — Machine Learning Project

### 📌 Author: Abhishek Patil  
### 🗓️ Date: Oct 2025  
### 🏆 Kaggle Competition: Titanic — Machine Learning from Disaster

## 🎯 Project Objective
Predict whether a passenger survived the Titanic disaster using:
- Feature Engineering
- Classification Algorithms
- Model Evaluation & Selection

Goal: Build a high-accuracy model for Kaggle submission ✅

## ✅ Work Completed

| Stage | Status |
|------|:---:|
| Data Collection & Setup | ✅ |
| Exploratory Data Analysis (EDA) | ✅ |
| Feature Engineering (FamilySize, IsAlone, etc.) | ✅ |
| Baseline Model — RandomForest | ✅ |
| Hyperparameter Tuning (GridSearchCV) | ✅ |
| Logistic Regression Baseline | ✅ |
| Model Comparison | ✅ |
| Final Kaggle Submission CSV | ✅ |

## 🧠 Feature Engineering Highlights

| Feature Name | Description |
|-------------|-------------|
| `FamilySize` | SibSp + Parch + 1 |
| `IsAlone` | Traveling alone survival pattern |
| `Pclass` | Converted to categorical |

Preprocessing handled by **Pipeline + ColumnTransformer** ✅  
Imputation + Scaling + OneHotEncoding integrated inside model pipeline.

## 🤖 Models Used

| Model | Validation Accuracy |
|------|-------------------|
| RandomForest (Tuned) | 0.8100558659217877 |
| Logistic Regression | 0.8156424581005587 |

✅ Final Model selected: LogisticRegression

## 📈 Evaluation Artifacts (Saved in `/reports`)
- Confusion Matrices (RF & LR)
- Model Comparison Chart
- Metrics JSON Summary

## 📂 Folder Structure
titanic_project/
│
├── data/
├── notebooks/
│ ├── 01_EDA.ipynb
│ ├── 02_Feature_Engineering_Model.ipynb
│ ├── 03_Tuning_RandomForest.ipynb
│ ├── 04_Logistic_Regression.ipynb
│ └── 05_Model_Comparison.ipynb
├── models/
├── output/
├── reports/
└── README.md

## 📤 Final Submission File
✅ `output/titanic_final_submission.csv`

## 🔮 Future Enhancements
- Title extraction (Mr/Mrs/Miss etc.)
- Gradient Boosting Models — XGBoost / LightGBM
- Class Imbalance Handling
- Deployment using Flask + AWS

---

⭐ If you like the project, please consider giving a star!  
📍 More ML projects coming soon…