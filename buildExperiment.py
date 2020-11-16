from loadData import loadHousingData
from prepareMLSets import splitData_stable_withArtificialIndex
from sklearn.impute import SimpleImputer
import pandas as pd


housingData = loadHousingData()

#we should take care of getting rid of NANs
#either by removing them:
## housingData.dropna(subset=["total_bedrooms"])
## housingData.drop("total_bedrooms", axis=1)
#-----------------------------------------------------------------
# or by filling the nans with the median
## median = housingData["total_bedrooms"].median()
## housingData["total_bedrooms"].fillna(median)
#-----------------------------------------------------------------
#or using the imputer with one of three strategies: 
#If “mean”, then replace missing values using the mean along the axis.
#If “median”, then replace missing values using the median along the axis.
#If “most_frequent”, then replace missing using the most frequent value along the axis.

imputer = SimpleImputer(strategy ="median")

housingData_num = housingData.drop("ocean_proximity", axis=1) # make a copy of removed column - impputer does know how to transform non numerical fields
imputer.fit(housingData_num) # initialize imputer to calculate the medium
print("Imputer parameters:" , imputer.statistics_)
processedData = imputer.transform(housingData_num) # transform it according to newly statistics

housingCompleteData = pd.DataFrame(processedData, columns = housingData_num.columns) # put the 

trainData, testData = splitData_stable_withArtificialIndex(housingCompleteData, 0.2)


print( len(trainData), " testDataLenghth=", len(testData))
