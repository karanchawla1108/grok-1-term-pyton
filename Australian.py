# You've decided to travel around Australia, and as an avid polyglot you want to learn as many Australian Aboriginal languages as you can before you go! There are quite a few though, so you decide to write a rudimentary machine translation program to help you.

# Write a program that reads from a file called dictionary.txt which contains pairs of English and translated words separated by a comma (,) and builds a dictionary with them. Your program should then read in lines of text from the user (until a blank line) and print out a translated sentence, where each word has been looked up in the dictionary.

# The data in dictionary.txt will look like this:

# dictionary.txt
# afternoon,wuraji-wuraji
# I,ngaju
# bird,jirripirdi
# like,kuja-piya
# dance,juka-pinyi
# python,malilyi
# laugh,ngarlarrimi
# we,ngalipa
# The first line in this dictionary.txt file means that the English word afternoon should be translated as wuraji-wuraji.

# Your program should work like this:

# English: I like python
# ngaju kuja-piya malilyi
# English: we laugh
# ngalipa ngarlarrimi
# English: 
# ​
# The dictionary provided will have all the words required for the translation in the correct case, and include no punctuation. The contents of dictionary.txt will change between test cases, so be sure you don't hard code in these example translations into your program!

# Hint
# The split method on a string takes an optional argument – the value on which to split.

 
# sentence = 'I saw a cat climb the tree.'
# print(sentence.split())
# print(sentence.split('a'))
# ['I', 'saw', 'a', 'cat', 'climb', 'the', 'tree.']
# ['I s', 'w ', ' c', 't climb the tree.']
# ​
# Info
# Aboriginal languages are a lot more interesting than a word by word translation from English! You can learn more about Warlpiri, Iwaidja, and Burarra language and culture and here.


 # its gonna take the dictionary, replace and while loop.

# fisrt txt open and dictionary.

dict = {}

with open('dictionary.txt', 'r') as file:
   for line in file:
      english, abro = map(str.strip, line.split(','))
      dict[english] = abro
#print (dict['I'])

#while loop
eng = input("English: ").strip()
while eng != "":
 # so the line = full data , dict[english] =  abro,
 # and english = english language.
 # english replace to dict[english].
  words = eng.split()
  translations = [dict.get(word, word) for word in words]

  print(' '.join(translations))
 
  eng = input("English: ").strip()

  
  
