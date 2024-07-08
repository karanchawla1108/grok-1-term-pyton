# The aim in this question is to find the main characters in a novel by doing textual analysis. We will hypothesise that the most frequent capitalised words in a novel are likely to be the character names.

# You should write a program to open a file called novel.txt and read in all the words. For this purpose let's assume that words are groups of letters and punctuation separated by spaces.

# Your program should then count the number of times each word appears and print out the top 3 words which start with a capital letter. For example, for our first sample file which you can download here:

# Jellicle Cats are black and white,
# Jellicle Cats are rather small;
# Jellicle Cats are merry and bright,
# And pleasant to hear when they caterwaul.
# Jellicle Cats have cheerful faces,
# Jellicle Cats have bright black eyes;
# They like to practise their airs and graces
# And wait for the Jellicle Moon to rise.
# Your program should print out:

# 6 Jellicle
# 5 Cats
# 2 And
# ​
# because the word Jellicle is the most frequently capitalised word (occurring 6 times), followed by Cats and then And.

# Once you've got it working on that simple example, lets try something really ambitious and run it on a novel – Pride and Prejudice. You can download a large chunk of text here. Your program should output:

# 899 I
# 521 Mr.
# 210 Elizabeth
# ​
# You can experiment on other novels freely available from Project Gutenberg.

# Hint
# In this question we treat a word as a group of letters and punctuation separated by spaces. This means that Dr and Dr. would count as different words, as would Grok and Grok,. Correctly normalising these examples to the same word is part of the process of tokenisation, but we're not going to worry about that here.





# Open the file and read its content
with open('novel.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split the text into words
words = text.split()

# Create an empty dictionary to store word counts
word_counts = {}

# Loop through each word and count its occurrences
for word in words:
    # Check if the word starts with a capital letter
    if word[0].isupper():
        # Increment the count for the word in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

# Get the top 3 capitalized words
sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)
top_words = sorted_words[:3]

# Print the results
for word in top_words:
    count = word_counts[word]
    print(f"{count} {word}")

