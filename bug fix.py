# Write a program that asks the user for a Unicode number, and prints out the character it represents.

# We've started the program for you, but it isn't working yet!

# It should work like this:

# Number? 99
# c
# ​
# It should work with any Unicode number. Here's another example:

# Number? 113
# q
# ​
# 1.
# Run the program without changing anything, and try the number 99.

# 2.
# Edit the program so that it converts number to the character it represents in Unicode, and then prints it out.

# 3.
# Run the program and enter 99 again, and check that it prints c.

# 4.
# Here are a few other Unicode numbers to try:

# 65 should print A
# 77 should print M
# 36 should print $
# When you're ready, submit your code for marking!


# Can I start again?
# You can reset the program to its original code by clicking on the little arrow near the filename and choosing Reset:

# Reset your code
# Restore the code originally provided


number = int(input('Number? '))
letter = chr(number)
print(letter)
