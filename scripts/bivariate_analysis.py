import matplotlib.pyplot as plt
import seaborn as sns

def bivariate_analyze_and_correlation(data):
    # Scatter plot for TotalPremium vs TotalClaims with hue as Province
    sns.scatterplot(x='TotalPremium', y='TotalClaims', hue='Province', data=data)
    plt.title('TotalPremium vs TotalClaims by Province')
    plt.show()

    # Correlation matrix
    correlation_matrix = data[['TotalPremium', 'TotalClaims']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()