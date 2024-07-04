# Here's something to stop you from getting repetitive when writing essays. Write a program that reads multiple lines of plain text from the user, then prints out each different word in the input with a count of how many times that word occurs. Don't worry about punctuation or case – the input will just be words, all in lower case. Your output should list the words in alphabetical order.

# For example:

# Enter line: which witch
# Enter line: is which
# Enter line: 
# is 1
# which 2
# witch 1
# ​
# Hint
# This code should help — if you build up a dictionary from the input, this will let you print the words in order:

 
# # This is a test dictionary.
# # You will need to build one from the input.
# occurrences = {'swim': 2, 'swan': 1}
# ​
# for word in sorted(occurrences):
#   print(word, occurrences[word])







word_count = {}

while True:
    line = input("Enter line: ")

    if not line:
        break

    words = line.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

for word in sorted(word_count):
    print(word, word_count[word])



