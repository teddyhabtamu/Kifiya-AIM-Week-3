import matplotlib.pyplot as plt
import seaborn as sns

# Plot histograms for numerical columns
def univariate_analze(data):
    numerical_columns = ['TotalPremium', 'TotalClaims']  # Ensure the column names match exactly
    data[numerical_columns].hist(bins=30, figsize=(10, 5))
    plt.show()

    # Plot bar charts for categorical columns
    categorical_columns = [
        'Citizenship', 'LegalType', 'Title', 'Language', 'Bank', 'AccountType', 
        'MaritalStatus', 'Gender', 'Country', 'Province', 'PostalCode', 
        'MainCrestaZone', 'SubCrestaZone', 'ItemType', 'VehicleType', 'make', 
        'Model', 'bodytype', 'NumberOfDoors', 'AlarmImmobiliser', 'TrackingDevice', 
        'NewVehicle', 'WrittenOff', 'Rebuilt', 'Converted', 'CrossBorder', 
        'NumberOfVehiclesInFleet', 'TermFrequency', 'ExcessSelected', 
        'CoverCategory', 'CoverType', 'CoverGroup', 'Section', 'Product', 
        'StatutoryClass', 'StatutoryRiskType'
    ]
    for col in categorical_columns:
        if col in data.columns:
            sns.countplot(y=col, data=data)
            plt.title(col)
            plt.show()
  