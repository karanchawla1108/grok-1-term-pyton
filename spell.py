# You are practicing for the grand final of the school spelling bee!

# A spelling bee works like this:

# You get told a word
# You repeat the word
# Spell out the word one letter at a time
# Repeat the word again
# Write a program that asks you for a word to spell and then helps you practice what to say!

# For example:

# Word: challenge
# challenge
# c
# h
# a
# l
# l
# e
# n
# g
# e
# challenge
# ​
# Here is another example:

# Word: origami
# origami
# o
# r
# i
# g
# a
# m
# i
# origami
# ​
# 1.
# Ask the user for a word.

# 2.
# Print the full word.

# 3.
# Use a for loop to print out each letter, one per line.

# 4.
# Print the full word again at the end.

# Run your code to test it, then hit Mark when you're done!





word = input("Word: ")
print (word)
for letter in word:

  print(letter)
  
print(word)