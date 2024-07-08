# In an attempt to fit in with the other kids, our Artificial Intelligence unit, Alice, likes to play guessing games. Her favourite game is Guess my favourite food.

# Write a program to play this game with Alice. An interaction with your program should look like this:

# What is my favourite food?
# Guess? chips
# Not even close.
# Guess? broccoli
# Not even close.
# Guess? electricity
# You guessed it! Buzzzz
# ​
# Sadly Alice isn't very creative, and so her answer is always electricity. Of course she never gets tired, and is happy to play this for hundreds of iterations until the other kids get it right (or pull the plug).



print ("What is my favourite food?")
guess = str(input("Guess? "))
while guess != "electricity":
  print("Not even close.")
  guess = str(input("Guess? "))
print ("You guessed it! Buzzzz")
  