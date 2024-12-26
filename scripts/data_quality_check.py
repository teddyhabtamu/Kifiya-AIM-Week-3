def check_missing(data):
  missing_values = data.isnull().sum()
  return missing_values