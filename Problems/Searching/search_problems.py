'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

longest = 0
longest_word = ""

with open('dictionary.txt') as file:
    for word in file:
        line = word.strip().upper()
        if len(word) > longest:
            longest = len(word)
            longest_word = word
print(longest_word)


# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

file = open('AliceInWonderland.txt')

total_words = []

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        total_words.append(word)

word_lens = [len(x) for x in total_words]
average = sum(word_lens) // len(word_lens)
print(len(total_words))
print(average)


# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_count = 0
with open('AliceInWonderland.txt') as file:
    for line in file:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            if word.upper() == "ALICE":
                alice_count += 1
print(alice_count)


# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
# use comprehension

seven_word_list = []
count = 0
answer = 0

with open('AliceInWonderland.txt') as file:
    for line in file:
        line = line.strip().upper()
        words = split_line(line)  # how to get rid of apostrophes
        for word in words:
            if len(word) == 7:
                seven_word_list.append(word)

    count_list = [seven_word_list.count(seven_word) for seven_word in seven_word_list]
    print(seven_word_list[count_list.index(max(count_list))])

'''
------ without comprehension ------

    for seven_word in seven_word_list:
        if seven_word_list.count(seven_word) > count:
            count = seven_word_list.count(seven_word)
            answer = seven_word

print(answer)
'''

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?

frequency_cheshire = 0

with open('AliceInWonderland.txt') as file:
    for line in file:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            if word.upper() == "CHESHIRE":
                frequency_cheshire += 1

print(frequency_cheshire)

# How many times does "Cat" occur?

frequency_cat = 0

with open('AliceInWonderland.txt') as file:
    for line in file:
        line = line.strip().upper()
        words = split_line(line)
        for word in words:
            if word.upper() == "CAT":
                frequency_cat += 1

print(frequency_cat)

# How many times does "Cheshire" immediately followed by "Cat" occur?

# frequency_cheshire_cat = 0
with open('AliceInWonderland.txt') as file:
    for line in file:
        line = line.strip().upper()
        words = split_line(line)

'''
        for word in words:
            if word.upper() == "CHESHIRE" and word.upper()[-1] == "CAT":
                frequency_cheshire_cat += 1

print(frequency_cheshire_cat)
'''


