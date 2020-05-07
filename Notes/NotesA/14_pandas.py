# Pandas!

import pandas as pd
import random

# lists > dicts > dataframes(series)

# Series are just pandas arrays (1d arrays)
s = [random.randrange(100) for x in range(10)]
my_series = pd.Series(s)
print(my_series)
print(type(my_series))  # pd.Series type
print(list(my_series))  # conversion to list is simple

# make a df (DataFrame) from a dictionary
d = {'col1': [1, 2, 3],
     'col2': [4, 5, 6]}
df = pd.DataFrame(data=d)
print(df)

# from an array/list
d2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # each item is a row
cols = ["A", "B", "C"]
df2 = pd.DataFrame(data=d2)
print(df2)

# read from a csv (or other datafile)
df3 = pd.read_csv('World firearms murders and ownership - Sheet 1.tsv', sep='\t')
print(df3)

# useful methods
print(df3.head())  # first 5 rows/items
print(df3.tail())  # last 5 rows/items
print(df3.info())  # datatypes (null values)
print(df3.describe())  # basic stats

# useful attributes
print(df3.index)  # index numbers
print(df3.columns)
print(df3.dtypes)
print(df3.shape)  # rows/indexes and columns

# simple column selection (NaN = Not a Number)
rank_ownership = (df3['Rank by rate of ownership'])
print(type(rank_ownership))
print(rank_ownership)  # or just print(df3['Rank by rate of ownership'])

# slicing dataframe using iloc[]  (index location)
print(df3.iloc[:5, 2])  # slice by row column (first 5 of 2 index)
print(df3.iloc[:, [1, 6]])  # select by sending in a list of columns or rows

# slicing dataframe using loc[]
print(df3.loc[:, ['ISO code', 'Rank by rate of ownership']])
iso_and_rank = df3.loc[:, ['ISO code', 'Rank by rate of ownership']]
print(type(iso_and_rank))


# CONSOLE WORK - WORLD CUP

import pandas as pd
x = 5
x  # in ipython/console, this automatically prints

df = pd.read_csv('/Users/alee/PycharmProjects/P2_SP20/Notes/NotesB/world_cup_matches.csv')  # use full path when working in console


# iloc (only useful for index number)
df.iloc[3:6]  # look at 3, 4, 5 matches
df.iloc[3:6, [4, 7]]   # cols 4 and 7 for index/rows 3to5

# loc
df.loc[3:6, ['Home Team Name', 'Away Team Name']] # use col names to slice

# all games from 1950
df_1950 = df.loc[df['Year'] == 1950]

# all games from 1950 Group 3
df_1950.loc[df['Stage'] == 'Group 3']

# alternately we could do both filters at once
df.loc[(df['Year'] == 1950) & (df['Stage'] == 'Group 3')]  # loc[(cond1) & (cond2)]

# Number of home games played by Netherlands
df.loc[df['Home Team Name'] == 'Netherlands'].count()

# All games by Netherlands
df.loc[(df['Home Team Name'] == "Netherlands") | (df['Away Team Name'] == "Netherlands")]

# All games by USA in 2014
df.loc[((df['Home Team Name'] == "USA") | (df['Away Team Name'] == "USA")) & (df['Year'] == 2014)]  # ["MatchID"].unique()
df_US14 = df.loc[((df['Home Team Name'] == "USA") | (df['Away Team Name'] == "USA")) & (df['Year'] == 2014)]

# Number of countries that were in 1986 world cup
df.loc[df['Year'] == 1986]['Home Team Name'].unique()
df.loc(list[df['Year'] == 1986]['Home Team Name'].unique())

# get rest from portal

