"""
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The data set at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intensity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Chicago_Energy_Benchmarking (2).csv") as f:
    reader = csv.reader(f)
    data = list(reader)

header = data.pop(0)
print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")
# intensity_index = header.index("GHG Intensity (kg CO2e/sq ft)")

valid_data = []
print(len(data))


for building in data:
    try:
        float(building[ghg_index])
        float(building[sqft_index])
        if building[type_index] == "K-12 School" and building[0] == "2018":
            valid_data.append(building)

    except:
        pass

valid_data.sort(key=lambda x: float(x[ghg_index + 1]))

ghg = [float(x[ghg_index]) for x in valid_data]
sqft = [float(x[sqft_index]) for x in valid_data]

ghg_intensity = [float(x[25]) for x in valid_data]

top_ten_intensity = ghg_intensity[-10:]
bottom_ten_intensity = ghg_intensity[:10]

print(bottom_ten_intensity)

colors = ["gray" for x in valid_data]
for i in range(len(top_ten_intensity)):
    colors[i] = "green"
for i in range(len(bottom_ten_intensity)):  # fix all this
    colors[-i - 1] = "red"


plt.figure(1, figsize=(14, 7))

plt.scatter(sqft, ghg, alpha=0.3, c=colors)

plt.ylabel("GHG Emissions")
plt.xlabel("Square Footage")
plt.title("GHG Emissions vs. Square Footage (K-12 schools in 2018)")


name_index = header.index("Property Name")
parker_index = [x[name_index] for x in valid_data].index("Francis W Parker School")


# annotate Parker's name
for data in valid_data:
    if data[name_index] == "Francis W Parker School":
        plt.annotate(data[name_index], xy=(sqft[parker_index], ghg[parker_index]))
        plt.scatter(sqft[parker_index], ghg[parker_index])

# line of best fit
p = np.polyfit(sqft, ghg, 1)
print(p)

x = [x for x in range(700000)]
y = [p[0] * y + p[1] for y in x]

plt.plot(x, y)


plt.show()



'''
WHAT I TRIED BEFORE LEARNING THE NEW WAY:

school = ["K-12 School"]  # probably a better way to do this
year = ["2018"]

ghg_emissions = []
square_footage = []

school_data = [x for x in data if x[9] in school]
# print(school_data)

year_school = [x for x in school_data if x[0] in year]
# print(year_school)


for school in year_school:
    try:
        emissions = float(school[24])
        footage = float(school[10])
        emissions.append(ghg_emissions)
        footage.append(square_footage)
    except:
        print(school[9], "invalid data")  # idk

plt.figure("GHG Lab", figsize=(12, 6))
plt.scatter(square_footage, ghg_emissions)

plt.ylabel("GHG Emissions")
plt.xlabel("Square Footage")
plt.title("GHG Emissions vs. Square Footage (K-12 schools)")

plt.show()

'''
