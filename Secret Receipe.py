# You're opening a boutique pie shop. You have lots of crazy pie ideas, but you need to keep them secret!

# Write a program that takes each character in your pie idea and encodes it as its Unicode number, using the ord function.

# Print the code for each character on a new line. Here's an example:

# Pie idea: Cheese
# 67
# 104
# 101
# 101
# 115
# 101
# ​
# Here's another example:

# Pie idea: Lime and pea
# 76
# 105
# 109
# 101
# 32
# 97
# 110
# 100
# 32
# 112
# 101
# 97
# ​
# 1.
# Ask the user for their pie idea.

# 2.
# Create a for loop to loop over each character in the pie name.

# 3.
# Inside your loop, convert each character to its Unicode number and then print it.

# 4.
# Run your code and try both of the examples above. Does your code print the right output?

# 5.
# When you're ready, submit your code for marking!





dalo = input ("Pie idea: ")
for c in dalo:
  convert = ord(c)
  print (convert)
