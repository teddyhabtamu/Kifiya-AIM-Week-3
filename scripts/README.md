# Scripts Folder

This folder contains modular Python scripts designed for various data processing, analysis, and quality assurance tasks related to the KAIM Week-3 project. Each script is focused on a specific functionality to enhance code maintainability and reusability.

---

## Contents

### 1. `bivariate_analysis.py`
- **Purpose**: Performs bivariate or multivariate analysis to explore relationships between different variables.
- **Key Functions**:
  - `plot_correlation_matrix(data, columns)`: Generates a correlation matrix heatmap for numerical variables.
  - `scatter_plot(x, y, data, title)`: Creates scatter plots to visualize relationships between two variables.

### 2. `data_comparison.py`
- **Purpose**: Compares data across different categories or groups to identify trends and patterns.
- **Key Functions**:
  - `compare_premiums_by_geography(data)`: Analyzes premium trends across geographic regions.
  - `compare_claims_by_vehicle_type(data)`: Examines claim amounts based on vehicle types.

### 3. `data_quality_check.py`
- **Purpose**: Ensures data quality by identifying and addressing issues like missing values and incorrect data types.
- **Key Functions**:
  - `check_missing_values(data)`: Summarizes missing values in each column.
  - `check_data_types(data)`: Validates the data types of each column.

### 4. `handle_missing.py`
- **Purpose**: Handles missing values in the dataset using appropriate imputation techniques.
- **Key Functions**:
  - `handle_missing(data)`: 
    - Imputes missing values for numerical columns with the mean.
    - Fills missing values for categorical columns with the most frequent value.

### 5. `load_data.py`
- **Purpose**: Handles data loading tasks from various file formats.
- **Key Functions**:
  - `load_txt(filepath, delimiter)`: Reads data from a `.txt` file with a specified delimiter and returns a DataFrame.
  - `load_csv(filepath)`: Reads data from a `.csv` file and returns a DataFrame.

### 6. `outlier_detection.py`
- **Purpose**: Detects and handles outliers in the dataset.
- **Key Functions**:
  - `detect_outliers(data, column)`: Identifies outliers in a numerical column using the IQR method.
  - `remove_outliers(data, column)`: Removes outliers from a numerical column based on specified thresholds.

---

## How to Use

1. **Import Specific Scripts**:
   - Example:
     ```python
     from handle_missing import handle_missing
     from bivariate_analysis import plot_correlation_matrix
     ```

2. **Ensure Proper File Paths**:
   - Update file paths for data loading scripts to align with the project structure.

3. **Execute Scripts as Needed**:
   - Example:
     ```python
     data = load_data.load_txt('data/raw/insurance_claims.txt', delimiter='|')
     clean_data = handle_missing(data)
     ```

---

## Contribution Guidelines

- Follow PEP 8 standards for Python coding.
- Ensure all functions are properly documented.
- Write unit tests for new functionality in the `tests/` folder.

---

For additional queries or contributions, please refer to the main project [README.md](../README.md).
