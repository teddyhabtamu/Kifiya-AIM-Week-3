# Notebooks Folder

This folder contains Jupyter notebooks for documenting and implementing key tasks for the KAIM Week-3 project. Each notebook serves a specific purpose, ranging from exploratory data analysis to implementing data version control.

---

## Contents

### 1. `DVC_implementation.ipynb`
- **Purpose**: Implements Data Version Control (DVC) to track and manage data versions effectively.
- **Key Highlights**:
  - Initializing DVC:
    ```bash
    dvc init
    ```
  - Setting up remote storage for data:
    ```bash
    dvc remote add -d localstorage /path/to/local/storage
    ```
  - Adding and tracking datasets with DVC:
    ```bash
    dvc add data/raw/insurance_claims.csv
    ```
  - Committing `.dvc` files to Git for version control.
  - Pushing data to the configured remote:
    ```bash
    dvc push
    ```
- **Usage**: This notebook guides the setup and workflow for managing data versions, ensuring reproducibility and efficient collaboration.

---

### 2. `EDA.ipynb`
- **Purpose**: Conducts Exploratory Data Analysis (EDA) to understand the dataset and derive actionable insights.
- **Key Highlights**:
  - **Data Summarization**:
    - Descriptive statistics for numerical columns like `TotalPremium`, `TotalClaims`.
    - Review of data types for proper formatting of categorical and date variables.
  - **Data Quality Assessment**:
    - Identification of missing values.
    - Analysis of data completeness.
  - **Univariate Analysis**:
    - Histograms for numerical features.
    - Bar charts for categorical variables.
  - **Bivariate/Multivariate Analysis**:
    - Correlation matrices for numerical variables.
    - Scatter plots exploring relationships between premiums, claims, and geography.
  - **Outlier Detection**:
    - Box plots for identifying outliers in numerical columns.
  - **Visualization**:
    - Creative and insightful visualizations to showcase trends and patterns.
- **Usage**: This notebook acts as the starting point for understanding the dataset and preparing it for subsequent analysis.

---

## How to Use

1. **Launch Jupyter Notebook**:
   - Activate the virtual environment:
     ```bash
     source .venv/bin/activate
     ```
   - Start Jupyter:
     ```bash
     jupyter notebook
     ```

2. **Run the Notebooks**:
   - Open `EDA.ipynb` to perform exploratory data analysis.
   - Open `DVC_implementation.ipynb` to implement data version control.

3. **Data Paths**:
   - Ensure data files are correctly placed in the `data/` directory or update file paths in the notebooks accordingly.

---

## Contribution Guidelines

- Keep notebooks clean and well-documented.
- Use markdown cells to explain each step and provide context for the analysis.
- Ensure all visualizations are labeled and provide meaningful insights.

---

For further details, refer to the project [README.md](../README.md).
