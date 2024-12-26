import seaborn as sns
import matplotlib.pyplot as plt

def data_comprison(data):
  sns.boxplot(x='Province', y='TotalPremium', data=data)
  plt.show()

  sns.boxplot(x='Province', y='TotalClaims', data=data)
  plt.show()