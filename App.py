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
maleAverageWeight = 195.8
maleAverageHeight = 176.4
maleMean = [maleAverageWeight, maleAverageHeight]
maleCov = [[1, 0], [0, 100]]
maleX, maleY = np.random.multivariate_normal(maleMean, maleCov, 2000).T

# Convert to 2 decimal places
np.around(maleX, 2, out=maleX)
np.around(maleY, 2, out=maleY)


# *******************
# Female Dataset
# (weight , height)
# *******************
femaleAverageWeight = 168.4
femaleAverageHeight = 162.9
femaleMean = [femaleAverageWeight, femaleAverageHeight]
femaleCov = [[1, 0], [0, 100]]
femaleX, femaleY = np.random.multivariate_normal(femaleMean, femaleCov, 2000).T

# Convert to 2 decimal places
np.around(femaleX, 2, out=femaleX)
np.around(femaleY, 2, out=femaleY)

# Write to SampleData.txt
#       - weight,height,gender [gender: 0 = male, 1 = female]
#       - formatted to 2 decimal places
#       - 4000 rows (2000 male, 2000 female)
f = open('SampleData.txt', 'w')
for i in range(len(maleX)):
    f.write("%.2f,%.2f,0\n" % (maleX[i], maleY[i]))
for i in range(len(maleX)):
    f.write("%.2f,%.2f,1\n" % (femaleX[i], femaleY[i]))
f.close()


a = np.hstack((maleX, maleY))
plt.hist(a, bins=100)  # arguments are passed to np.histogram
plt.title("Histogram")
plt.xlabel('Weight')
plt.ylabel('Height')
plt.show()
