import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Average male height (US): 5.78 ft
# Average female height (US): 5.34 ft
# https://en.wikipedia.org/wiki/List_of_average_human_height_worldwide (2011 - 2014)

# Average male weight (US): 195.8 lb
# Average female weight (US): 168.4 lb
# https://en.wikipedia.org/wiki/Human_body_weight (2011 - 2014)

maleAverageHeight = 5.78
maleAverageWeight = 195.8
maleHeight = []
maleWeight = []

femaleAverageHeight = 5.34
femaleAverageWeight = 168.4
femaleHeight = []
femaleWeight = []

separationLineA = pd.read_csv("sep_line_a.txt", header=None)
separationLineB = pd.read_csv("sep_line_b.txt", header=None)
# *******************
# Generates random data and writes to text file
# *******************
file = open('SampleData.txt', 'w')
for x in range(0, 2):
    for y in range(0, 2000):
        if x == 0:
            height = np.random.normal(maleAverageHeight, 0.3)
            weight = np.random.normal(maleAverageWeight, 20)
            maleHeight.append(height)
            maleWeight.append(weight)
            file.write(str(maleHeight[y]) + "," + str(maleWeight[y]) + "," + str(x) + "\n")
        else:
            height = np.random.normal(femaleAverageHeight, 0.3)
            weight = np.random.normal(femaleAverageWeight, 20)
            gender = 0
            femaleHeight.append(height)
            femaleWeight.append(weight)
            file.write(str(femaleHeight[y]) + "," + str(femaleWeight[y]) + "," + str(x) + "\n")
file.close()

# *******************
# Plot Datasets for part A (Only height)
# *******************
plt.figure(1)
plt.subplot(211)
convertedMaleHeight = np.array(maleHeight)
convertedFemaleHeight = np.array(maleHeight)
maleGraphA = plt.scatter(maleHeight, np.full(convertedMaleHeight.shape, -0.001), alpha=.25, s=35, label='Male')
femaleGraphA = plt.scatter(femaleHeight, np.full(convertedFemaleHeight.shape, -0.001), alpha=.25, s=35, label='Female')
separationLine = pd.read_csv("sep_line_a.txt", header=None)
plt.legend(loc='upper right')
plt.xlabel("Height(ft)")
xLine = separationLineA[0][1] / separationLineA[0][0]
plt.plot([xLine, xLine], [-1, 1])
plt.gca().axes.get_yaxis().set_visible(False)

# *******************
# Plot Datasets for part B (Both height and weight)
# *******************
plt.subplot(212)
maleGraphB = plt.scatter(maleHeight, maleWeight, alpha=.25, s=35, label='Male')
femaleGraphB = plt.scatter(femaleHeight, femaleWeight, alpha=.25, s=35, label='Female')
plt.legend(loc='upper right')
plt.xlabel("Height(ft)")
plt.ylabel("Weight(lbs)")

bias = separationLineB[0][2]
heightWeight = separationLineB[0][0]
weightWeight = separationLineB[0][1]
plt.plot([4.5, 7], [(bias / weightWeight) + ((heightWeight * 4.5) / weightWeight),
                    (bias / weightWeight) + ((heightWeight * 7) / weightWeight)])
plt.show()

allHeight = np.concatenate((maleHeight, femaleHeight), axis=0)
allWeight = np.concatenate((maleWeight, femaleWeight), axis=0)

# *******************
# Height only stats
# *******************
TP = 0
TN = 0
FP = 0
FN = 0
for x in range(len(allHeight)):
    height = allHeight[x]
    weight = allWeight[x]

    if x < 2000:
        gender = 0
    else:
        gender = 1

    heightWeight = separationLineA[0][0]
    b = separationLineA[0][1]

    total = heightWeight * height - b * 1

    if total < 0:
        if gender == 0:
            FP += 1
        else:
            TP += 1
    else:
        if gender == 0:
            TN += 1
        else:
            FN += 1
print("** A) Where only the first feature (height) is considered **")
print("Error: " + str(1 - ((TN + TP) / 4000)))
print("Accuracy: " + str((TN + TP) / 4000))
print("True Positive: " + str(TN / 2000))
print("True Negative: " + str(TP / 2000))
print("False Positive: " + str(FN / 2000))
print("False Negative: " + str(FP / 2000))
print("")

# *******************
# Height & weight stats
# *******************
TP = 0
TN = 0
FP = 0
FN = 0
for x in range(len(allHeight)):
        height = allHeight[x]
        weight = allWeight[x]
        if x < 2000:
            gender = 0
        else:
            gender = 1
        heightWeight = separationLineB[0][0]
        weightWeight = separationLineB[0][1]
        b = separationLineB[0][2]

        total = (heightWeight * height) + b - (weightWeight * weight)

        if total >= 0:
            if gender == 0:
                FP += 1
            else:
                TP += 1
        else:
            if gender == 0:
                TN += 1
            else:
                FN += 1

print("** B) Where both features (height and weight) are considered. **")
print("Error: " + str(1 - ((TN + TP) / 4000)))
print("Accuracy: " + str((TN + TP) / 4000))
print("True Positive: " + str(TN / 2000))
print("True Negative: " + str(TP / 2000))
print("False Positive: " + str(FN / 2000))
print("False Negative: " + str(FP / 2000))
print("")
print("Completed at:", datetime.datetime.now().time())




