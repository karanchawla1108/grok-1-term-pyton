# You are learning a new language, and are having a competition to see how many unique words you know in it to test your vocabulary learning.

# Write a program where you can enter one word at a time, and be told how many unique words you have entered. You should not count duplicates. The program should stop asking for more words when you enter a blank line.

# For example:

# Word: Chat
# Word: Chien
# Word: Chat
# Word: Escargot
# Word: 
# You know 3 unique word(s)!
# ​
# and

# Word: Katze
# Word: Hund
# Word: Maus
# Word: Papagei
# Word: Schlange
# Word: 
# You know 5 unique word(s)!
# ​
# and

# Word: Salam
# Word: 
# You know 1 unique word(s)!
# ​



word = set()

words = input("Word: ")
while words != '':
  word.add(words)
  words = input("Word: ")
  

print(f"You know {len(word)} unique word(s)!")
  
