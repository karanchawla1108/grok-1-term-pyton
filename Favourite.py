# Toffy Apples! Chocolate pudding! Fruit Salad!

# You're running a poll to find out your friends' favourite dessert and decide to write a program to help you keep track of all the suggestions and who voted for each.

# Your program should keep reading in lines (until an empty line) which contain the person's name, then a colon (:) then their favourite dessert.

# Your program should work like this, printing out the results in any order:

# Name:vote Greg:chocolate
# Name:vote Teena:macaroons
# Name:vote Georgina:apple pie
# Name:vote Will:chocolate
# Name:vote Sophia:gelato
# Name:vote Sam:ice cream
# Name:vote James:chocolate
# Name:vote Kirsten:gelato
# Name:vote 
# apple pie 1 vote(s): Georgina
# gelato 2 vote(s): Sophia Kirsten
# chocolate 3 vote(s): Greg Will James
# macaroons 1 vote(s): Teena
# ice cream 1 vote(s): Sam
# ​
# Here's another example, with no two votes for the same dessert:

# Name:vote Harry:treacle tart
# Name:vote Hermione:chocolate frogs
# Name:vote Hagrid:rock cake
# Name:vote Ron:pumpkin pasties
# Name:vote 
# treacle tart 1 vote(s): Harry
# pumpkin pasties 1 vote(s): Ron
# rock cake 1 vote(s): Hagrid
# chocolate frogs 1 vote(s): Hermione
# ​
# When more than one person votes for a particular dessert, you should output their names in the order that the votes were received.







store = {}
name = input("Name:vote ")

while name != '':
  name,flavour = name.split(':') # spliting the input and giving them variables names.
 
  if flavour not in store:
     store[flavour] = [name] # i think [this gonna show the output].
  else:
    store[flavour].append(name)
  
  
  name = input("Name:vote ")
  #for x, y in thisdict.items():
  #print(x, y)

for flavour, votes in store.items(): 
    vote_count = len(votes) # flavour and votes put the key value with the help of .items() foe example the [sam, vanialla], where votes is vanialla and sam is flavour.
    print(f"{flavour} {vote_count} vote(s): {' '.join(votes)}")
