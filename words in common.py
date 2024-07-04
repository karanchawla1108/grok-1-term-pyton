# You've started learning French, and have noticed that a lot of words are the same in English and French. You're curious about how many words are the same, and have obtained a large list of words in both languages.

# Write a program to read in a list of English words (english.txt) and French words (french.txt), and print out all the words in common. That is, all the words that occur in both of the two files.

# For example, if english.txt contains:

# circle
# table
# year
# competition
# and french.txt contains:

# bien
# competition
# merci
# air
# table
# then your program should print out (in any order):

# competition
# table
# ​
# Hint
# You might want to use set intersection to solve this question.



# Read English words from english.txt
with open("english.txt", "r") as english_file:
    english_words = {line.strip() for line in english_file}

# Read French words from french.txt
with open("french.txt", "r") as french_file:
    french_words = {line.strip() for line in french_file}

# Find common words
common_words = english_words & french_words

# Print the common words
for word in common_words:
    print(word)
