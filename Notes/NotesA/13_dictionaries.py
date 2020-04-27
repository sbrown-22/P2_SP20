# Dictionaries (dict)

# str, int, bool ,list, tuple, set, object


# Quick look at sets
# not used widely in Python
# sets store UNIQUE values as unordered group

my_set = {1, 2, 3, 4, 4, 5}  # eliminated duplicates
print(my_set)

# one very specific use of a set
my_list = {6, 7, 8, 9, 8, 7}  # list with duplicates
print(set(my_list))

my_list = list(set(my_list))  # list minus the duplicates
print(my_list)


# Dictionaries are just unordered collections of key: value info

# Why use a dict over list (how to make one)
mr_lee = ['Aaron', 'Lee', 46, ['Python', 'SOL']]
mr_lee_d = {'first': 'Aaron', 'last': 'Lee', 'age': 46, 'fav_prog_lang': ['Python', 'SOL']}

# structure {key1: val1, key2: val2...}
# (keys can also be ints, etc. not just strings

# Accessing values
print(mr_lee_d['age'])  # index a dictionary using a key
print(mr_lee_d['fav_prog_lang'][1])

# iterable
for key in mr_lee_d:
    print(mr_lee_d[key])

# adding to a dict
mr_lee_d['spoken_langs'] = ['English', 'Pig Latin']
print(mr_lee_d)

# cannot be accessed by index number
# print(mr_lee_d[0])  # gives a keyerror if you don't know the key

# Build a simple dict object (community is a tv show)
community = {'genre': ['Comedy'],
             'creators': ['Dan Harmon'],
             'starring': ['Joel McHale', 'Gillian Jacobs', 'Danny Pudi'],
             'no_seasons': 6
             }

community['no_episodes'] = 110
print(community['no_episodes'])

# change items in a dict
community['starring'].append('Alison Brie')
print(community['starring'])

# increment item
community['no_episodes'] += 1
print(community['no_episodes'])

# keys method
print(community.keys())
print(list(community.keys()))

# values method
print(community.values())
print(list(community.values()))

# dictionary to tract values

