# Ali Baba is trying to open a cave door to find the treasure. His brother overhears thieves saying the password, but he can't quite work out what it is.

# Write a program to ask Ali for a password. If the password is correct, the cave door will be opened. Otherwise nothing will happen.

# Your program should work like this when Ali says "Open sesame!":

# What is the password Ali? Open sesame!
# The cave door opens!
# ​
# If Ali says anything else the program should do nothing:

# What is the password Ali? Open the door
# ​


gate = input("What is the password Ali? ")
if gate.lower() == "open sesame!":
 print ("The cave door opens!")

 



