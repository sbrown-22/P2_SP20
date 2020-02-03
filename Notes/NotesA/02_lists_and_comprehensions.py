# LISTS

import random

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_num_list = [5, 9, 12, 6, 3, -3, 4]

print(my_list[1])  # Bev
print(my_list[-1])  # Gus
print(my_list[:4])  # Abe to Dan
print(my_list[-3:])  # Eve to Gus

my_copy = my_list  # does not create a copy, just another link to the original
my_copy.append("Hal")
print(my_copy)
print(my_list)

my_copy = my_list[:]  # DO THIS!
my_copy.append("Ida")
print(my_copy)
print(my_list)

# 2d lists
my_2d = [["Abe", 8], ["Bev", 7], ["Cam", 4]]
print(my_2d[1])  # Bev, 7
print(my_2d[1][1])  # 7
# print(my_2d[1][2])  # out of range
my_2d[2].append("Wilson")
print(my_2d)

# If in
if "Abe" in my_list:
    print("Abe is there")
if "abe" in my_list:
    print("abe is there")

if random.randrange(10) in [3, 5, 6, 8, 9]:
    print("yay!")

# LIST FUNCTIONS
print(len(my_list))  # returns the length of a list
print(min(my_num_list))  # returns the lowest
print(max(my_num_list))  # highest value
print(max(my_list))  # highest alphabetically
print(sum(my_num_list))  # sums the list

# LIST METHODS
print(my_list.index("Cam"))  # returns the index (# in list) of the found object
my_list.append("Cam")  # two Cams?
print(my_list.index("Cam"))  # only returns first one
print(my_list.count("Abe"))  # counts them

my_list.append("Deb")
my_list.sort()  # orders the list
print(my_list)
my_list.reverse()  # reverse the current order
print(my_list)

# manipulating the list
my_list.pop()  # pops one off the end of the list
print(my_list)
my_person = my_list.pop()  # returns the popped item
print(my_person)
print(my_list)
front_of_line = my_list.pop(0)
print(front_of_line)
print(my_list)

# destroy an item
del my_list[1]
print(my_list)

# concatenation
first = "Francis"
last = "Parker"
print(first, last)
print(first + last)  # squished 2 strings together

print(my_list + my_num_list)

# ITERATING THROUGH A LIST
# FOR EACH LOOP (works with a copy of the item)
for name in my_list:
    print(name)

# INDEX VARIABLE LOOP (works directly with the list using indexes)
for i in range(len(my_list)):
    my_list[i] = my_list[i].upper()  # or .lower
    print(my_list[i])

print(my_list)

# LIST COMPREHENSIONS
# [returned_item FOR iterator IN list/range IF filter]

# make a list from 50 to 100

my_list = []

for i in range(50, 101):  # can make it count by certain number
    my_list.append(i)

print(my_list)

my_list = [x for x in range(50, 101)]
print(my_list)  # same as code above

# make a list of powers of 2 from 0 to 100
my_list = []

for i in range(51):
    my_list.append(2 ** i)

print(my_list)


my_list = [2 ** x for x in range(51)]


# same list, but filter out any results greater than 100000
my_list = []

for i in range(51):
    if 2 ** i < 100000:
        my_list.append(2 ** i)

print(my_list)

my_list = [2 ** x for x in range(51) if 2 ** x < 100000]
print(my_list)


# roll a single die 100 times and add it to a list
roll = random.randrange(1, 7)

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)

# roll two die 100 times and add it to a list (ex: [1, 6])
my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)

# filter out so we only show doubles ([1, 1] etc.)
my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)

print()
# all at once: create a list of two die rolls, filter out the doubles - same as b4 but in 1 line, created new list
my_doubles = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]
# generates two die rolls and filters out for doubles
print(my_doubles)


# working with strings is similar to lists
first = "Francis"
last = "Parker"
print(first[0])  # F
first = first.upper()  # all caps
print(first)
print(first + last)
print(last[-3:])

if "Par" in last:  # checks if in list
    print("YEP")

for letter in first:
    print(letter)

