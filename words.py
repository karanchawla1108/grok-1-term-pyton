# You're reading a book by an unfamiliar author and are curious about which country they might be from. You decide to write a program to help you guess this based on the spelling of the words in the book.

# Write a program that reads in a word (e.g. colour or color) and checks if it occurs in the file book.txt, printing out <word> was found in the book. or <word> was not found in the book..

# For example, given the book.txt file:

# book.txt
# He looked out from the top of the mountain .
# The colour of the sky was amazing .
# Reds , oranges and pinks faded into a hazy blue.
# then your program should work like this:

# Word to look for: colour
# colour was found in the book.
# ​
# The provided input word will always be in lowercase, but your program should match in a case insensitive manner. For instance, given the following book.txt file:

# book.txt
# Hypothesize ? How was she going to form a
# hypothesis when she didn't even know what the
# rest of the data looked like ?
# then your program should work like this:

# Word to look for: hypothesize
# hypothesize was found in the book.
# ​
# Punctuation will always be provided as a separate word, so you don't have to do anything special to account for it.


word = input("Word to look for: ").lower()

with open('book.txt', 'r') as file:
  files = file.read()
  
found_word = word in files.lower()

if found_word:
 print (f'{word} was found in the book.')
else:
 print(f'{word} was not found in the book.')
