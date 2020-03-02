'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''

from NBAStats import data  # or could just import data

# if __name__ == "__main__":

# 1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
headers = data.pop(0)
print(headers)

# 2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)

print()
pts_list = sorted(data, key=lambda x: x[-1])
top_ten = pts_list[-10:]

for i in range(len(pts_list) - 11, len(pts_list)):
    print(pts_list[i][2])


# 3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)

print()
print(int(sum([x[-1] for x in data if x[2] == "Kobe Bryant"])))

# 4  What player has the most 3point field goals in a single season. (3pts)

print()
field_goal_list = sorted(data, key=lambda x: x[34])
print(field_goal_list[-1][2])

# 5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)

print()
ws_list = sorted(data, key=lambda x: x[25])
print(ws_list[-1][2])

'''
ws48 = headers.index("WS/48")
print(ws48)
data.sort(key=lambda x: x[ws48])
print()
'''

# 6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".

print()
print("How many players play the small forward position (SF)?")


'''
sf_list = sorted(data, key=lambda x: x[4])
if ws_list[-1][3] == "SF":
    sf_number += 1
'''
sf_numbers = 0
positions = [x[3] for x in data if x[3] == "SF"]
for item in positions:
    sf_numbers += 1

print(sf_numbers, "players played the small forward position.")


# 7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)

pts_list = sorted(data, key=lambda x: x[-1])
top_hundred = pts_list[-100:]
# unfinished