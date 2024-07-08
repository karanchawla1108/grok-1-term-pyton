# You and your friends have entered lots of songs into a karaoke machine, and are running out of time to sing them all! The machine plays songs, stored in songlist.txt, in reverse order, so that the most recently added song is the first one to be played.

# Write a program that reads in songlist.txt and how many more songs will be sung. It then prints them out in the correct order.

# Given the provided songlist.txt, your program should work like this:

# How many more songs? 3
# Hotel California, Eagles
# Thriller, Michael Jackson
# Respect, Aretha Franklin
# ​
# Here is another example:

# How many more songs? 6
# Hotel California, Eagles
# Thriller, Michael Jackson
# Respect, Aretha Franklin
# Piano Man, Billy Joel
# Bohemian Rhapsody, Queen
# Hey Jude, The Beatles
# ​

with open ('songlist.txt', 'r') as file:
  files = file.readlines()
  #print(files)
  
  msg = int(input("How many more songs? "))
  
  while msg > 0:
    #print(files.pop())
    print(files.pop().strip())
    msg-=1
    
  
  
