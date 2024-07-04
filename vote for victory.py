# In Australia, you can only vote once you're 18 years old, and everyone 18 and over must vote.

# Write a program that asks your age and tells you if you should vote. If you're younger than 18, it should do this:

# How old are you? 13
# You are not old enough yet.
# ​
# If you're 18 or above, it should do this:

# How old are you? 25
# You have to vote!
# ​
# 1.
# Ask for the user's age with input and convert it to a number with int.

# 2.
# Add an if and an else to check the number. If it is less than 18 then print out You are not old enough yet. Otherwise print out You have to vote!

# 3.
# Run your program and check it with the first example: 13. Then check it with the second example: 25.

# 4.
# Mark your program to check your work!




vote = int(input("How old are you? "))
if vote >= 18 :
  print ("You have to vote!")
else:
  print ("You are not old enough yet.")