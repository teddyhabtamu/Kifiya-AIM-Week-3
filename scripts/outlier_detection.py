import matplotlib.pyplot as plt
import seaborn as sns

def outlier(data):
  sns.boxplot(x='TotalPremium', data=data)
  plt.show()

  sns.boxplot(x='TotalClaims', data=data)
  plt.show()