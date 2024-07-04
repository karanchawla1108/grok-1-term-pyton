# Write a program that checks how long a name is. The program should take a name as input from the user.

# If the name has 3 or fewer letters, your program should work like this:

# Enter your name: Lin
# Hi Lin, you have a short name.
# ​
# If the name has between 4 and 8 letters (inclusive), your program should work like this:

# Enter your name: Jimmy
# Hi Jimmy, nice to meet you.
# ​
# Otherwise, if the name has more than 8 letters, your program should work like this:

# Enter your name: Yaasmeena
# Hi Yaasmeena, you have a long name.
# ​
# Hint
# Do you remember how to calculate the length of a string? Take a look at this slide from Module 2 for a refresher.

# Hint
# Remember to give input the same prompt string as in our sample interaction above.

name = input("Enter your name: ")
name_len = len(name)
if name_len <= 3:
   print ("Hi "+ str(name) +", you have a short name." )
elif name_len >=4 and name_len <=8:
   print ("Hi "+ str(name) +", nice to meet you." )
else:
  print ("Hi "+ str(name) +", you have a long name." )
  
