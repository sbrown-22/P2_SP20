# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1, 101)]
print(my_list)

# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20, 41, 2)]
print(my_list)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(1, 101)]
print(my_list)

# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]

my_list = [x for x in my_list if x % 2 == 0]
print(my_list)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list

from number_list import num_list  # CHECK THIS, also what does it mean find vs print?

if __name__ == "__main__":
    print(num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))

# Find and print the lowest number in num_list (1pt)
print(min(num_list))

# Find and print the average of num_list (2pts)
print(sum(num_list) / len(num_list))

# Remove the lowest number from num_list (2pt)
num_list.remove(min(num_list))

# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list (2pts)
top_ten = []
num_list.sort()
top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?

from statistics import mode

def most_common(num_list):
    return (mode(num_list))

print(most_common(num_list))

'''
Other stuff I tried that didn't work:

#1 
num_list.sort()
for num in num_list:
    print([[x, num_list.count(x)] for x in set(num_list)])
print(max(num_list[1]))

#2
new_list = num_list
num_mode = new_list[0]
previous_frequency = 0

for num in new_list:
    current_frequency = new_list.count(num)
    if current_frequency > previous_frequency:
        num_mode = num
        previous_frequency = current_frequency
print(num_mode)
'''

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

num_list.sort()
for i in range(2, 9993):
    for num in num_list:
        if num % i == 0:
            del num_list[num_list.index(num)]

prime_numbers = len(num_list)
print(prime_numbers)

'''
Also tried:

for num in range(min(num_list), max(num_list)):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                break
            else:
                print(num)
'''

# Find the number of palindromes
# Hint: This may be easier to do with strings
'''
palindrome_list = []
for num in num_list:
    num.reverse()
    print(num)
'''






