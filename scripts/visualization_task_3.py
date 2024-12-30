import matplotlib.pyplot as plt
import seaborn as sns


def mean_totalClaims_by_province(data):
  # Calculate mean TotalClaims by Province
  grouped_provinces = data.groupby('Province')['TotalClaims'].mean().sort_values()

  # Plot
  plt.figure(figsize=(12, 6))
  grouped_provinces.plot(kind='barh', color='skyblue')
  plt.title("Mean Total Claims by Province", fontsize=16)
  plt.xlabel("Mean Total Claims", fontsize=12)
  plt.ylabel("Province", fontsize=12)
  plt.tight_layout()
  plt.show()


def pivot_table_postal_heatmap(data):
  # Create a pivot table for PostalCode and TotalClaims
  postal_heatmap = data.pivot_table(values='TotalClaims', index='PostalCode', aggfunc='mean')

  # Plot
  plt.figure(figsize=(10, 8))
  sns.heatmap(postal_heatmap, cmap="coolwarm", annot=False)
  plt.title("Heatmap of Mean Total Claims by Postal Code", fontsize=16)
  plt.xlabel("Postal Code", fontsize=12)
  plt.tight_layout()
  plt.show()
  
def distribution_of_totalClaims_by_gender(data):
  sns.set(style="whitegrid")
  plt.figure(figsize=(8, 6))
  sns.boxplot(x='Gender', y='TotalClaims', data=data, palette="Set2")
  plt.title("Distribution of Total Claims by Gender", fontsize=16)
  plt.xlabel("Gender", fontsize=12)
  plt.ylabel("Total Claims", fontsize=12)
  plt.tight_layout()
  plt.show()
  
def margin_differences_by_postalCode(data):
  plt.figure(figsize=(12, 6))
  sns.scatterplot(data=data, x='PostalCode', y='Margin', hue='Province', palette='viridis', alpha=0.7)
  plt.title("Scatter Plot of Margin Across Postal Codes", fontsize=16)
  plt.xlabel("Postal Code", fontsize=12)
  plt.ylabel("Margin", fontsize=12)
  plt.tight_layout()
  plt.show()
  
def Risk_Differences_Across_Provinces(data):
  grouped = data.groupby('Province').agg({'TotalClaims': 'mean', 'Margin': 'mean'}).reset_index()

  # Plot
  grouped.plot(x='Province', kind='bar', figsize=(14, 7), color=['orange', 'blue'], edgecolor='black')
  plt.title("Comparison of Mean Total Claims and Margin by Province", fontsize=16)
  plt.xlabel("Province", fontsize=12)
  plt.ylabel("Mean Values", fontsize=12)
  plt.legend(["Total Claims", "Margin"])
  plt.tight_layout()
  plt.show()
  
def correlationMatrix(data):
  # Compute correlation matrix
  corr_matrix = data[['TotalClaims', 'TotalPremium', 'Margin']].corr()

  # Plot heatmap
  plt.figure(figsize=(8, 6))
  sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
  plt.title("Correlation Matrix", fontsize=16)
  plt.tight_layout()
  plt.show()
  
def totalPremium_vs_totalClaims(data):
  plt.figure(figsize=(10, 6))
  bubble_chart = sns.scatterplot(data=data, x='TotalPremium', y='TotalClaims', size='Margin', hue='Province', alpha=0.6, sizes=(20, 200))
  bubble_chart.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
  plt.title("Bubble Chart: Total Premium vs. Total Claims by Province", fontsize=16)
  plt.xlabel("Total Premium", fontsize=12)
  plt.ylabel("Total Claims", fontsize=12)
  plt.tight_layout()
  plt.show()
  
def distribution_of_margins(data):
  plt.figure(figsize=(10, 6))
  sns.histplot(data['Margin'], kde=True, color='purple', bins=30)
  plt.title("Distribution of Margins", fontsize=16)
  plt.xlabel("Margin", fontsize=12)
  plt.ylabel("Frequency", fontsize=12)
  plt.tight_layout()
  plt.show()

