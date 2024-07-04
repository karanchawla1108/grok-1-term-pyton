# Write a program to read in lines from the user which are pairs of name and favourite colour, then print out everyone's favourite colours.

# For example:

# Name and colour: Nicky Blue
# Name and colour: James Yellow
# Name and colour: Sam Red
# Name and colour: 
# Nicky Blue
# James Yellow
# Sam Red
# ​
# You can print out the pairs of name and favourite colour in any order.

# All names will be unique, and occur only once.



choice = {}

line = input("Name and colour: ")
while line:
  split = line.split()
  name = split[0]
  colour = split[1]
  choice[name] = colour
  line = input("Name and colour: ")

for name, colour in choice.items():
    print( name + " " +colour)