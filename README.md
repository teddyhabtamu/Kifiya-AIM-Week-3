# Week-3: KAIM - Marketing Analytics for Car Insurance

## Business Objective

AlphaCare Insurance Solutions (ACIS) aims to enhance risk and predictive analytics in car insurance for South Africa. As a marketing analytics engineer, your first project involves analyzing historical insurance claim data to optimize marketing strategies and identify “low-risk” clients. This analysis will support ACIS in attracting new clients by offering reduced premiums.

---

## Project Tasks and Objectives

### Task 1: Git and GitHub

#### Key Activities:

- Set up a Git repository for the project with a comprehensive README file.
- Use Git for version control and set up CI/CD pipelines using GitHub Actions.

#### Key Deliverables:

1. **Repository Setup**:

   - Create a branch named `task-1` for day 1 analysis.
   - Make at least 3 descriptive commits daily.

2. **Exploratory Data Analysis (EDA)**:
   - **Data Summarization**:
     - Calculate variability for numerical features like `TotalPremium` and `TotalClaim`.
     - Ensure proper formatting of data types (e.g., categorical variables and dates).
   - **Data Quality Assessment**:
     - Identify missing values.
   - **Univariate Analysis**:
     - Visualize numerical data using histograms and categorical data with bar charts.
   - **Bivariate/Multivariate Analysis**:
     - Explore relationships between monthly changes in `TotalPremium` and `TotalClaims` by `ZipCode` using scatter plots and correlation matrices.
   - **Geographical Trends**:
     - Compare changes in insurance cover types, premiums, auto makes, etc.
   - **Outlier Detection**:
     - Detect outliers in numerical data using box plots.
   - **Visualization**:
     - Produce three creative and insightful plots based on the EDA findings.

---

### Task 2: Data Version Control (DVC)

#### Key Activities:

1. **Install and Set Up DVC**:

   - Install DVC: `pip install dvc`
   - Initialize DVC in the project: `dvc init`

2. **Configure Local Remote Storage**:

   - Create a directory for local remote storage:
     ```bash
     mkdir /path/to/your/local/storage
     ```
   - Add the storage as a DVC remote:
     ```bash
     dvc remote add -d localstorage /path/to/your/local/storage
     ```

3. **Add and Track Data**:

   - Place datasets into the project directory.
   - Track datasets using DVC:
     ```bash
     dvc add <data.csv>
     ```

4. **Version Control**:

   - Commit the `.dvc` files to Git:
     ```bash
     git add data.csv.dvc .gitignore
     git commit -m "Track dataset with DVC"
     ```

5. **Push Data to Remote**:
   - Push data to the local remote storage:
     ```bash
     dvc push
     ```

Installation and Setup

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/KAIM-week3.git
   cd KAIM-week3
   ```
2. Set Up Virtual Environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
