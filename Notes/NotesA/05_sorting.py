# Sorting

# swap values
a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a

# make a random list of 100 number with values of 1 to 99
# use list comp
import random

random_list = [random.randrange(1, 100) for x in range(100)]
random_list2 = random_list[:]
print(random_list)


# SELECTION SORT

# total_iterations = 0
for current_pos in range(len(random_list)):  # goes through whole list
    minimum_pos = current_pos  # recorded what position is (cycling through), minimum will change, current is just us walking through the loop
    for scan_pos in range(current_pos + 1, len(random_list)):  # going from one right of current through end of list
        # total_iterations += 1
        if random_list[scan_pos] < random_list[minimum_pos]:  # go through, if look to the right and it's smaller than what we started with, make it new position
            minimum_pos = scan_pos
    random_list[current_pos], random_list[minimum_pos] = random_list[minimum_pos], random_list[current_pos]  # swapping values
print(random_list)
# print(total_iterations)


# INSERTION SORT

# total_iterations = 0
for key_pos in range(1, len(random_list2)):
    key_val = random_list2[key_pos]  # value of key position
    scan_pos = key_pos - 1  # scanning to the left (look to dancer on the left)
    while scan_pos >= 0 and random_list2[scan_pos] > key_val:  # not off the list, then continue checking
        # total_iterations += 1
        random_list2[scan_pos + 1] = random_list2[scan_pos]
        scan_pos -= 1
        random_list2[scan_pos + 1] = key_val
print(random_list2)
# print(total_iterations)


# MORE WITH FUNCTIONS

print("Hello", end=" ")  # uses an optional parameter which has a default value of "\n"
print("World", end="!\n")


def hello(name, time_of_day="morning"): # or: def hello(name, time_of_day): then later below write "afternoon" after Owen
    print("Hello", name, "good", time_of_day)

hello("Owen")  # morning is the default value


# Lambda functions (anonymous function on a single line)

double_me = lambda x: x * 2  # sending in: returning
# double_me is a function that returns the value x * 2
print(double_me(5))

sum_product = lambda a, b: [a + b, a * b]
print(sum_product(3, 2))


# Real world sorting with python
my_list = [random.randrange(1, 100) for x in range(100)]

# sort method (changed the list in place)
print(my_list)
my_list.sort()  # default is to sort alphabetically small to large
print(my_list)

my_list.sort(reverse=True)
print(my_list)


