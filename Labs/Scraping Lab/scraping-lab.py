# SCRAPING PROBLEMS

# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweets located on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

# There was some difficulty scraping a tweet.
# After a closer look, you can't do it from the dynamic webpage any longer
# I will give you some separate code to show you how to scrape a dynamic page.
# Feel free to skip if you don't want to try it.  (no penalty)

from bs4 import BeautifulSoup
import requests

'''
from selenium import webdriver
import time

# I inspected a tweet and saw this span tag...
# <span class="class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">FINE LINE. THE ALBUM. OUT NOW. </span>

harry_url = "https://twitter.com/harry_styles?lang=en"

page = requests.get(harry_url)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

tweets = soup.find_all('span', class_="css-901oao")

print(tweets)

'''
# print("{} {}!".format("Hello", "World"))


# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()

url = "https://weather.com/weather/tenday/l/69bedc6a5b6e977993fb3e5344e3c06d8bc36a1fb6754c3ddfb5310a3c6d6c87"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

print("\n" * 5)

day_tags = soup.find_all("span", class_="date-time")  # is it okay
day_list = [x.text for x in day_tags]
print(day_list[:10])

date_tags = soup.find_all("span", class_="day-detail clearfix")
date_list = [x.text for x in date_tags]
print(date_list[:10])

description_tags = soup.find_all("td", class_="description")
description_list = [x.text for x in description_tags]
print(description_list[:10])

high_low_tags = soup.find_all("td", class_="temp")
high_low_list = [x.text.replace("°", "°/", 1) for x in high_low_tags]
print(high_low_list[:10])

rain_tags = soup.find_all("td", class_="precip")
rain_list = [x.text for x in rain_tags]
print(rain_list[:10])

wind_tags = soup.find_all("td", class_="wind")
wind_list = [x.text for x in wind_tags]
print(wind_list[:10])

humidity_tags = soup.find_all("td", class_="humidity")
humidity_list = [x.text for x in humidity_tags]
print(humidity_list[:10])

print("\n" * 5)

print("San Fransisco, CA, 10 Day Weather")
print("_______________________________________")
for i in range(len(day_list)):  # when to use .format?
    print(day_list[i] + ",", date_list[i], "will be", description_list[i],
          "with a high and low of", high_low_list[i], ", humidity at", humidity_list[i] + ". There is a", rain_list[i], "chance of rain with winds of", wind_list[i]+".")
    print()

    # fix high and low temp & winds

