import pandas as pd

def load_data():
  data = pd.read_csv('../datas/MachineLearningRating_v3.txt', delimiter='|')
  return data