import scipy.stats as stats

def risk_differences_bn_gender(data):
  min_data_points = 5  # Set a threshold
  gender_counts = data['Gender'].value_counts()
  valid_genders = gender_counts[gender_counts >= min_data_points].index
  filtered_data = data[data['Gender'].isin(valid_genders)]

  # Group by Gender and calculate mean TotalClaims
  grouped_data = data.groupby('Gender')['TotalClaims'].mean()
  print(grouped_data)

  # Perform t-test
  t_test_result = stats.ttest_ind(filtered_data[filtered_data['Gender'] == 'Male']['TotalClaims'], filtered_data[filtered_data['Gender'] == 'Not specified']['TotalClaims'])
  
  return t_test_result