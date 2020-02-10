# more on loops

# basic FOR loop
for i in range(5, 51, 5):
    print(i, end=" ")  # doesn't return each thing
print()

# RANGE function (alternative for comprehension
my_list = [x for x in range(100)]
print(my_list)

my_list = list(range(100))  # iterable (interval cast as list)
print(my_list)

# BREAK (breaks out of the loop)
for number in my_list:
    if number > 10:
        break  # new
    print(number, end=" ")

print("End of loop")

# CONTINUE (skipts to the end of that loop for that iteration - doesn't print multiples of 7)
for number in my_list:
    if number % 7 == 0:
        continue
    print(number, end=" ")

# FOR ELSE
for number in my_list:
    print(number, end=" ")
    if number == 80:
        break
else:
    print("The loop completed naturally")

