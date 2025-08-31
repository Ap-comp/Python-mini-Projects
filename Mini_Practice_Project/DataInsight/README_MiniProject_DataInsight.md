
# Mini Project: Data Insight Generator

## 📌 Objective
Analyze a real-world sales dataset using Pandas and NumPy to extract meaningful insights, clean missing data, and compute derived metrics.

## 🧰 Tools & Libraries
- Python 3
- Pandas
- NumPy
- Jupyter Notebook or any Python IDE

## 📁 Dataset Used
`sales_data_with_missing.csv` — Contains columns like `Region`, `Product`, `Sales`, `Units`, `Price`, including missing values and formatting issues.

## 🧠 Key Operations Performed
- Loaded the dataset and inspected missing values
- Cleaned data using `.isnull()`, `.fillna()`, and `.astype()`
- Computed a new column: `TotalValue = Units * Price`
- Used `groupby()` to aggregate total sales by region
- Sorted and displayed the top 5 highest value entries
- Exported the cleaned and transformed data

## 📊 Sample Output
```
  Region Product  Units  Price  TotalValue
0  North       A   10.0  250.0      2500.0
3   West       B   16.0  250.0      4000.0
4  North       C   11.0  245.5      2700.5
5  South       C   13.0  246.2      3200.6
8   East       C   14.0  260.0      3640.0
```

## 🚀 How to Run
1. Clone the repo or upload the `.ipynb` or `.py` file to your own GitHub
2. Install required libraries (if not already):
```bash
pip install pandas numpy
```
3. Run the notebook or script

## 🙌 Author
Abhishek Patil — transitioning into AI/ML with 4+ years of SQL experience.

---

