# Searching

# use forward slashes to go into folders and .. to go "up" a folder
# can do control click then copy path, not always what we want though
file = open('../resources/super_villains.txt', 'r')  # open to read
print(file)

for line in file:
    print(line.strip())

file.close()

# .strip() method removes extra characters on either side of text
print("    Hello ".strip())
print("World\n".strip())  # took away double space
print("!")


# 'w' open to write & overrides file
file = open('../resources/super_villains.txt', 'a')  # 'a' opens to append to file
file.write('Lee the Merciless\n')
file.write('Rohan the Destroyer\n')
file.close()

file = open('../resources/heroes.txt', 'w')
file.write('Owen the Valiant\n')
file.close()

# Better way to open close a file (syntactic sugar)
# file automatically closes after execution of with
with open('../resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())

# .read() method just imports whole file as a string
with open('../resources/super_villains.txt') as f:
    read_data = f.read()  # big string

print("\n\nRead method:")
print(read_data)

# Reading data into an array (list)
with open('../resources/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# Linear Search (not very efficient but easy)

key = "Vidar the Manic".upper()

i = 0
while i < (len(villains) - 1) and key != villains[i]:  # stay in list, if the key not equal to i then keep going thru loop
    i += 1

if i < len(villains):
    print("Found it at position", i)
else:
    print(key, "is not in list")

# try to make this into a function


def linear_search(key, list):
    """
    :param key: what you are looking for
    :param list: where you are looking
    :return: bool did you find it?
    """


print(linear_search())


