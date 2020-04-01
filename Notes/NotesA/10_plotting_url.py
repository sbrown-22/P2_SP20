"""
Reading a csv from a url
Comma Separated Values (CSV) from a Uniform Resource Locator (URL)

scatter plot w/ sizes and colors
"""
import csv
import requests
import matplotlib.pyplot as plt


def get_data(url):
    with requests.Session() as s:  # making a class object out of Request library
        download = s.get(url)  # download data
        content = download.content.decode('utf-8')  # way to format text
        reader = csv.reader(download.splitlines(),
                            delimiter=',')  # or content.splitlines(), the comma makes it plit data iby commas
        data = list(reader)
    return data


# so that we can get updated data each time

url = "https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD"
data = get_data(url)
header = data.pop(0)

print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")

valid_data = []
print(len(data))

for building in data:  # rebuilding list
    try:
        float(building[ghg_index])
        float(building[sqft_index])
        if building[type_index] == "K-12 School" and building[0] == "2018":
            valid_data.append(building)
    except:
        pass

print(len(valid_data))

valid_data.sort(key=lambda x: float(x[ghg_index + 1]))

ghg = [float(x[ghg_index]) for x in valid_data]
sqft = [float(x[sqft_index]) for x in valid_data]


colors = ["green" for x in valid_data]
for i in range(37):
    colors[i] = "red"

'''
color = []

for building in valid_data:
    if building > 4000:
        color.append("red")
    else:
        color.append("green")
'''

plt.figure("GHG School Plot")
# plt.figure(1, tight_layout=True)

plt.scatter(ghg, sqft, alpha=0.3, c=colors)  # s for size, c for color (arrays

plt.show()
