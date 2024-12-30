import scipy.stats as stats


def risk_difference_bn_postalcodes(data):
  grouped_data = data.groupby('PostalCode')['TotalClaims'].mean()
  print(grouped_data)

  # Perform ANOVA test
  anova_result = stats.f_oneway(*[data[data['PostalCode'] == postalcode]['TotalClaims'] for postalcode in data['PostalCode'].unique()])
 
  return anova_result