# You're interested in looking at trending Twitter hashtags, but you notice that people aren't very consistent with how they use them. Specifically, the capitalisation and punctuation in hashtags is inconsistent. You decide to write a program to read in tweets, normalise any hashtags present, and print out a tally of frequencies.

# Hashtags should only include words starting with #. All punctuation should be removed from the end of a hashtag, and the letters should be converted to lowercase. For instance, #Python! should be normalised to #python, and #Today_I_Learned... should be #today_i_learned.

# Your program should work like this. The tally of hashtags can be printed out in any order.

# Tweet: #Python is #AWESOME!
# Tweet: This is #So_much_fun #awesome
# Tweet: 
# #python 1
# #awesome 2
# #so_much_fun 1
# ​

import string
import collections
count = collections.defaultdict(int)
tweet = input("Tweet: ").split()

while tweet:
  for word in tweet:
     if word[0] == '#':
        count[word.strip(string.punctuation).lower()] +=1 
              
  
  
  
  tweet = input("Tweet: ").split()
for htag in count:
    print(f"#{htag} {count[htag]}")
    


