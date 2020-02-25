'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


file = open("dictionary.txt")

dictionary_list = []
for line in file:
    line = line.strip()
    dictionary_list.append(line)


file.close()

# --- Linear search


file = open("AliceInWonderland200.txt")
line_number = 0
for line in file:
    line = line.strip()
    line_number += 1
    words = split_line(line)
    for word in words:
        i = 0
        word_found = False
        while i < len(dictionary_list) and dictionary_list[i] != word.upper():
            i += 1

        if i < len(dictionary_list) - 1:
            word_found = True
        else:
            print(line_number, word.upper())

file.close()



# --- Binary search

file = open("AliceInWonderland200.txt")
line_number = 0
for line in file:
    line = line.strip()
    line_number += 1
    words = split_line(line)
    for word in words:
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        i = 0
        found = False

        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2

            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print(line_number, word.upper())

file.close()

# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.

