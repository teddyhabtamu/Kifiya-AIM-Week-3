import scipy.stats as stats

# Group by Province and calculate mean TotalClaims

def risk_difference_accross_province(data):
  
  grouped_data = data.groupby('Province')['TotalClaims'].mean()
  print(grouped_data)

  # Perform ANOVA test
  anova_result = stats.f_oneway(*[data[data['Province'] == province]['TotalClaims'] for province in data['Province'].unique()])
  return anova_result