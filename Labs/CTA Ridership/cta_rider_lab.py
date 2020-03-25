'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)

In the last 10 years, there is a general downward trend in CTA usage. This is the same with both rail usage and bus
usage. This is likely due to the fact that newer transportation programs such as Divy bikes, Uber, and Lyft have become
much more popular, and cars are being manufactured at higher quality. Though their usage numbers have gotten much more
similar, Buses seam generally more popular than trains. This is likely because they're easier to access and are much
more flexible with the amount of buses and locations offered.
'''


import csv
import matplotlib.pyplot as plt

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)

# LINE PLOT OF RAIL USAGE & BUS USAGE IN LAST 10 YEARS
header = data.pop(0)
print(header)

years = [int(x[0]) for x in data]
last_ten_years = years[-10:]

rail_usage = [int(x[3]) for x in data]
last_ten_rail_usage = rail_usage[-10:]

bus_usage = [int(x[1]) for x in data]
last_ten_bus_usage = bus_usage[-10:]

total_usage = [int(x[4]) for x in data]
last_ten_total_usage = total_usage[-10:]

plt.figure(1, tight_layout=True)
plt.plot(last_ten_years, last_ten_rail_usage, label="Rail Usage")
plt.plot(last_ten_years, last_ten_bus_usage, label="Bus Usage")
plt.plot(last_ten_years, last_ten_total_usage, label="Total CTA Usage")


plt.title("Transportation Usage Over the Last 10 Years", fontsize=10, color='blue')
plt.ylabel("# of People")  # change?
plt.xlabel("Year")
plt.legend(fancybox=True, shadow=True)

plt.show()



