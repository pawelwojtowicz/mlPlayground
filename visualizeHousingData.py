from loadData import loadHousingData
import matplotlib.pyplot as plt

housingData = loadHousingData()

#housingData.plot(kind="scatter", x="longitude", y="latitude")

#alpha gives the possibility of detecting the high density data
#housingData.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)

housingData.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1, s=housingData["population"]/100, label="population", c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True)
housingData["rooms_per_houshold"] = housingData["total_rooms"]/housingData["households"]
housingData["bedrooms_per_rooms"] = housingData["total_bedrooms"]/housingData["total_rooms"]
housingData["population_per_households"] = housingData["population"]/housingData["households"]

correlationMatrix = housingData.corr()

print( correlationMatrix["median_house_value"].sort_values(ascending=False) )

plt.legend()
plt.show()

