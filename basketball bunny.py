# The Guinness World Record for the most slam dunks in one minute by a rabbit is 7. This record is held by Bini the Bunny.

# Write a program that asks how many slam dunks your rabbit can do. If the number is greater than 7 then it should do this:

# How many slam dunks? 10
# New world record!
# ​
# Otherwise it should do this:

# How many slam dunks? 5
# No record yet. Keep training!
# ​
# 1.
# Ask for the number of slam dunks with input and convert it to a number with int.

# 2.
# Add an if to check if the number of slam dunks is greater than 7. If it is greater than 7 then print out New world record!

# Reminder: The greater than symbol is >

# 3.
# Add an else to the end. Inside the else statement, print out No record yet. Keep training!

# 4.
# Run your program and check it with the first example: 10. Then check it with the second example: 5.

# 5.
# Mark your program, to check your work!

rabbit = int(input("How many slam dunks? "))
if rabbit > 7:
 print ("New world record!")
else :
 print ("No record yet. Keep training!")