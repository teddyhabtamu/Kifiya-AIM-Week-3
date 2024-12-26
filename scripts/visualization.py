import matplotlib.pyplot as plt
import seaborn as sns

def visualize(data):
    # Sample the data for faster plotting
    sample_data = data.sample(frac=0.1, random_state=1)  # Adjust the fraction as needed

    # Plot 1: Distribution of TotalPremium
    sns.histplot(sample_data['TotalPremium'], kde=True)
    plt.title('Distribution of TotalPremium')
    plt.show()

    # Plot 2: Scatter plot with regression line for TotalPremium vs TotalClaim
    sns.lmplot(x='TotalPremium', y='TotalClaims', data=sample_data, aspect=2)
    plt.title('TotalPremium vs TotalClaim')
    plt.show()

    # Plot 3: Heatmap of correlation matrix
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = data[numeric_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()