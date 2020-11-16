from loadData import loadHousingData
import matplotlib.pyplot as plt

housingData = loadHousingData()

print(housingData.head())
print(housingData.info())
print(housingData.describe())

housingData.hist(bins=100, figsize=(20,15))
plt.show()

