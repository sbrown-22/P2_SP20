# Folium train map

# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:

my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))

# If you have extra time, try to put some html into the popup.

import folium
import csv

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

cta_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)  # , titles='Stamen Toner'

print(data.pop(0))

'''
lats = [float(x[-3]) for x in data]
longs =[float(x[-2]) for x in data]
names = [x[2] for x in data]

for i in range (len(data)):
    folium.Marker(location=[lats[i], longs[i]],
                  popup='<b>{}</b></span>'.format(names[i]),
                  icon=folium.Icon(color='orange', icon='paint-brush', prefix='fa')
                  ).add_to(cta_map)
'''


lat_longs = [eval(x[-1]) for x in data]
names = [x[2] for x in data]

red_line = []
red = [x[7] for x in data]
for i in red:
    if i == 'true':
        red_line.append(i)
print(len(red_line))

blue = [x[8] for x in data]
green = [x[9] for x in data]
brown = [x[10] for x in data]
purple = [x[11] for x in data]
purple_express = [x[12] for x in data]
yellow = [x[13] for x in data]
pink = [x[14] for x in data]
orange = [x[15] for x in data]


for i in range(len(data)):
    folium.Marker(location=[lat_longs[i][0], lat_longs[i][1]],
                  popup='<b>{}</b></span>'.format(names[i]),
                  icon=folium.Icon(color='orange', icon='train', prefix='fa')
                  ).add_to(cta_map)

'''
for i in range(len(lat_longs)):
    folium.Marker(location=lat_longs[i], popup='<ahref="http://www.fwparker.org">Parker</a>').add_to(cta_map)
'''
'''
for i in range(len(lat_longs)):
    lats = lat_longs[i][0]
    longs = lat_longs[i][1]
'''

cta_map.save('train-map.html')

