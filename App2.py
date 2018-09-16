import numpy as np
import matplotlib.pyplot as plt

# Average male height (US): 176.4 cm
# Average female height (US): 162.9 cm
# https://en.wikipedia.org/wiki/List_of_average_human_height_worldwide (2011 - 2014)

# Average male weight (US): 195.8 lb
# Average female weight (US): 168.4 lb
# https://en.wikipedia.org/wiki/Human_body_weight (2011 - 2014)

# *******************
# Male Dataset
# (weight , height)
# *******************
maleAverageWeight = np.array([95.8, 295.8])
maleAverageHeight = np.array([150.4, 202.4])
maleMean = [maleAverageWeight.mean(), maleAverageHeight.mean()]
maleSTD = [maleAverageWeight.std() / 3, maleAverageHeight.std() / 3]
maleCorr = 0.8         # correlation
maleCovs = [[maleSTD[0]**2, maleSTD[0]*maleSTD[1]*maleCorr], [maleSTD[0]*maleSTD[1]*maleCorr, maleSTD[1]**2]]
maleData = np.random.multivariate_normal(maleMean, maleCovs, 2000).T
# Convert to 2 decimal places
np.around(maleData, 2, out=maleData)

# *******************
# Female Dataset
# (weight , height)
# *******************
femaleAverageWeight = np.array([88.4, 248.4])
femaleAverageHeight = np.array([136.9, 188.9])
femaleMean = [femaleAverageWeight.mean(), femaleAverageHeight.mean()]
femaleSTD = [femaleAverageWeight.std() / 3, femaleAverageHeight.std() / 3]
femaleCorr = 0.8         # correlation
femaleCovs = [[femaleSTD[0]**2, femaleSTD[0]*femaleSTD[1]*femaleCorr], [femaleSTD[0]*femaleSTD[1]*femaleCorr, femaleSTD[1]**2]]
femaleData = np.random.multivariate_normal(femaleMean, femaleCovs, 2000).T
# Convert to 2 decimal places
np.around(femaleData, 2, out=femaleData)

# *******************
# Write to SampleData.txt
#   - weight,height,gender [gender: 0 = male, 1 = female]
#   - formatted to 2 decimal places
#   - 4000 rows (2000 male, 2000 female)
# *******************
f = open('SampleData.txt', 'w')
for i in range(len(maleData[0])):
    f.write("%.2f,%.2f,0\n" % (maleData[0][i], maleData[1][i]))
for i in range(len(femaleData[0])):
    f.write("%.2f,%.2f,1\n" % (femaleData[0][i], femaleData[1][i]))
f.close()

# *******************
# Plot Datasets
# *******************
plt.scatter(maleData[0], maleData[1], label='Male')
plt.scatter(femaleData[0], femaleData[1], label='Female')
plt.legend(loc='upper left')
plt.xlabel('Weight (lb)')
plt.ylabel('Height (cm)')
plt.show()

