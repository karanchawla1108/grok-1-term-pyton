# We all know how annoying it is when people on forums SHOUT all the time. Write a program to convert their SHOUTING (uppercase characters) to polite talking (lowercase characters).

# An interaction with your program should look like this:

# Loud: I AM SO AWESOME
# Quiet: i am so awesome
# ​
# Here is another example, with mixed case:

# Loud: LEARNING PYTHON is so FUN!
# Quiet: learning python is so fun!
# ​


sentence = input("Loud: ").lower()
print("Quiet: " + str(sentence))

