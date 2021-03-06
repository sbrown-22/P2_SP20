import csv
import matplotlib.pyplot as plt
import numpy as np

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

header = data.pop(0)
print(header)

# make a scatter plot of firearms_per_100 vs homicides_per_100k

homicide_100k = []
firearm_100 = []
names = []
similar = ["Canada", "Norway", "Australia", "Iceland", "Finland", "Denmark", "Sweden",
           "Germany", "Japan", "Taiwan", "Singapore", "Netherlands", "Italy", "Spain",
           "England and Wales", "United States", "South Korea"]  # if add "El Salvador", will change A LOT

data = [x for x in data if x[0] in similar]  # comment this out to get original graphs with all countries

for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        name = country[0]
        homicide_100k.append(homicides)
        firearm_100.append(firearms)
        names.append(name)
    except:
        print(country[0], "invalid data")  # countries that maybe don't have data or has space

print(names)  # the countries that have valid data for both categories

plt.figure("Firearm Plot", figsize=(12, 6))
plt.scatter(firearm_100, homicide_100k)

plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")
plt.title("Homicides vs. Gun Ownership")

# plt.annotate("My text", xy=(50, 50))

for i in range(len(names)):
    plt.annotate(names[i], xy=(firearm_100[i], homicide_100k[i]))

p = np.polyfit(firearm_100, homicide_100k, 1)  # (x, y, poly_order) 1st order is linear
print(p)  # returns (m, b) (slope, y intercept)

# line of best fit - can kind of predict
x = [x for x in range(100)]  # 0 to 99, make data to plot
y = [p[0] * y + p[1] for y in x]  # this is the equation of the line, for every y in the x

plt.plot(x, y)

plt.show()
