# FORMATTING

import random

# round(n, digits)
print(round(243.38363, 2))

# format method (a string method)
a = 234.342334
b = 297491387434
print("My number is {}!".format(a))
print("my numbers are {} and {}".format(a, b))
print("my numbers are {1} and {0}. {1} is my favorite".format(a, b))  # you can specify the order

# numerical_order:spaceholder+justification+sign+width+commas+precision+datatype+scientificnotation

# justification and spacing
# ^center, >right, <left # determined what the boundaries are
for i in range(20):
    c = random.randrange(2000)
    # print("{:6}".format(c))  # six spaced are reserved for the number, can put number like above on left of :, on right is where formatting goes
    print("hello {:^30} spaces".format(c)) # 30 spaced and centered

# commas
for i in range(20):
    c = random.randrange(10000000)
    print("${:8,}".format(c))  # 8 spaces with commas, if number was more than 8 spaces the entire number would still print

# precision and datatype (d dec/int, f float, b binary)
for i in range(20):
    c = random.random() * 1000
    my_string = "{:14.3f}".format(c)  # 14 spaces, 3 decimals as a float
    print(type(my_string))

for i in range(20):
    c = random.randrange(1000)
    print("{:<10b}". format(c))  # format to binary

# scientific notation
for i in range(20):
    c = random.randrange(1000)
    print("{:.2e}".format(c))

x = 6.77e11  # accepts scientific notation
print(x)

