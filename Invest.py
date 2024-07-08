# Everyone knows pirates are all about buried treasure. They need a way to hide where they've buried their gold!

# The way they hide their treasure is to encode the location inside a secret phrase: the first two and last two letters of the phrase.

# For example, simply hidden in the bank would mean the treasure is actually in the sink.

# Write a program that asks for a secret phrase and prints out the location of the treasure. It works like this:

# Secret phrase? try under the bee
# The treasure is in the tree!
# ​
# Here's another example:

# Secret phrase? big chance it's behind the fans
# The treasure is in the bins!
# ​
# 1.
# Ask the user for a secret phrase.

# 2.
# Get the first letter of the phrase and store it in a variable.

# 3.
# Do the same thing for the second, second last, and last letters of the phrase.

# Hint: Use a negative index to count backwards from the end of a string.

# 4.
# Print The treasure is in the followed by the four letters and an exclamation mark.


# Remember: string indexes start from 0
# The first letter of a string has index 0, the second has index 1, and so on.


msg = input("Secret phrase? ")
msg1 = msg[0],msg[1], msg[-2], msg[-1]
msg2 = ''.join(msg1)
print (f"The treasure is in the {msg2}!")


