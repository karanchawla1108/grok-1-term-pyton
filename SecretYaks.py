# You and your friends have created a secret code!

# The secret code is hidden inside the message: it's the first, sixth and twelfth letters of the line. Spaces count as letters.

# It looks like this:

# Just on my yak
# J + o + y spells Joy – which is what you feel riding a yak!

# Your program should read in the message and print the secret code:

# Message: Just on my yak
# Joy
# ​
# Here is another example:

# Message: I'm an old koala
# Ink
# ​
# 1.
# Ask the user for a message.

# 2.
# Get the first letter of the message and store it in a variable. Don't forget to start counting from 0!

# 3.
# Do the same thing for the sixth and twelfth characters.

# 4.
# Print the secret code!


# Remember: string indexes start from 0
# The first letter of a string has index 0, the second has index 1, and so on.a



msg = input("Message: ")
msg1 = msg[0], msg[5], msg[11]
msg2 = ''.join(msg1)
print(msg2)
