import scipy.stats as stats

def margin_differences_bn_postalcode(data):
  data['Margin'] = data['TotalPremium'] - data['TotalClaims']

  # Group by PostalCode and calculate mean Margin
  grouped_data = data.groupby('PostalCode')['Margin'].mean()
  print(grouped_data)

  # Perform ANOVA test
  anova_result = stats.f_oneway(*[data[data['PostalCode'] == postalcode]['Margin'] for postalcode in data['PostalCode'].unique()])
  
  return anova_result