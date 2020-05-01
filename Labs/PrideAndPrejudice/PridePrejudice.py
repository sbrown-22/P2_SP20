'''
Pride and Prejudice (25pts)

This lab is largely review of: lists, comprehensions, requests, string methods, matplotlib.
The only new item here is using a dictionary (dict).

We will use list, dictionary, and graphing skills to do a basic analysis of Jane Austen's Pride and Prejudice.  Your task is to create a bar graph of the 25 most common words.


A common Python pattern to count objects, produce histograms, or update stats is to make calls to a dictionary as you iterate through a list. For example, given a list of words, you can create a dictionary to store counts and then iterate through the list of words, checking how many times each word has appeared using your dictionary, and updating the dictionary count now that you've seen that word again.
'''


# PSEUDO CODE
# Get text from https://www.gutenberg.org/files/1342/1342-0.txt - Use requests library.
# Split the transcript into words - Use split and strip methods and store results in a list.
# Create a dictionary object to store the word counts
# Iterate through the list/text of Pride and Prejudice
# Update word counts on your dict (10pts)
# Sort words by counts in descending order (5pts)
# Create Bar Graph - the most common 25 words (5pts)
# Include descriptive titles and labels (5pts)

import requests
import operator
import matplotlib.pyplot as plt

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
pride_prejudice = requests.get(url).text
# print(pride_prejudice[:1000])

word_list = pride_prejudice.split()
word_list = [x.upper().strip(' ?.:;!\\<>{}\n\t') for x in word_list]
# print(word_list[:1000])

pp_dictionary = {}

for word in word_list:
    if word in pp_dictionary:
        pp_dictionary[word] += 1
    else:
        pp_dictionary[word] = 1
# print(pp_dictionary)

reverse_list = dict(sorted(pp_dictionary.items(), key=operator.itemgetter(1), reverse=True))

keys = list(reverse_list.keys())
common_keys = keys[:25]

values = list(reverse_list.values())
common_values = values[:25]


plt.figure("Pride and Prejudice Word Frequency Bar Graph", figsize=(18, 6))
plt.bar(common_keys, common_values)

plt.ylabel("Frequency of Appearance")
plt.xlabel("Word")
plt.title("Pride and Prejudice Most Common Words")

plt.show()


'''
OTHER WAYS I TRIED SORTING:

sorted_keys = sorted(dictionary, key=lambda x: dictionary[x])

sorted_list = ([pair[0] for pair in sorted(pp_dictionary.items(), key=lambda item: item[1])])
reverse_list = sorted_list[::-1]
print(reverse_list[:25])

value_list = list(pp_dictionary.values())
sorted_value = sorted(value_list)
print(sorted_value)
'''

# CHALLENGE (OPTIONAL)
# Here is a list of the 1000 most common words in English: https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt
# Make your plot show the 25 most common words in Pride and Prejudice NOT in this list.

# MORE CHALLENGES
# look at Project Gutenberg, and try another book and see if your algorithms hold up.
# HERE IS A LIST OF NEGATIVE WORDS.  Evaluate a text for percentage of negative words. Try the same for positive. Or do both to evaluate the mood of a book. Compare Mark Twain to Edgar Allan Poe. https://gist.githubusercontent.com/mkulakowski2/4289441/raw/dad8b64b307cd6df8068a379079becbb3f91101a/negative-words.txt