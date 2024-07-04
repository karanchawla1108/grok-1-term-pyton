# Let's cheer for your favourite team!

# Write a program that reads in a team name and turns it into a cheer! It should work like this:

# Team name? TIGERS
# Give me T
# Give me I
# Give me G
# Give me E
# Give me R
# Give me S
# Go TIGERS!
# ​
# Here's another example:

# Team name? CROWS
# Give me C
# Give me R
# Give me O
# Give me W
# Give me S
# Go CROWS!
# ​
# 1.
# Ask for a team name.

# 2.
# For each letter in the team name, print out Give me followed by each of the letters.

# Hint: remember f-strings from last week?

# 3.
# At the end, print out Go and the team name, followed by an exclamation mark.

# Don't forget to test and mark your code!




team = input("Team name? ")

for letters in team:
  print ("Give me "+ str(letters))
  
print ("Go " + str(team) + str("!") )