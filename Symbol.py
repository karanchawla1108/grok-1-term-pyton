# You want to add lots of symbols to your messages, but it's a lot of effort typing them all out. Let's get a computer to do it!

# You need to define a function called make_symbols that takes two arguments: symbol and number.

# The function should return the given number of symbols, all in a line. For example:

# print(make_symbols('!', 5))
# !!!!!
# ​
# Here's another example:

# print(make_symbols('?', 3))
# ???
# ​
# 1.
# Use def to define a function called make_symbols. It should take two arguments: symbol and number.

# 2.
# Inside your function, multiply the symbol by the given number.

# 3.
# Return the result of the multiplication.

# 4.
# Run your program to see the output of the tests!

# Testing your function
# We've given you an if __name__ == '__main__': block. Any code inside this if statement will not affect the marking.

# Marking your function
# We mark your function with the exact function name given.
# It should not use input or print.
# It should return the result, rather than print it.


# Define your function here!
def make_symbols(dky, num):
  return dky*num
  
  
if __name__ == '__main__':
  # You can use this to test your function.
  # Any code inside this if statement will be ignored by the automarker.
  
  # Test the first example in the question.
  print(make_symbols('!', 5))
  
  # Test the second example in the question.
  print(make_symbols('?', 3))

  # You can add more tests here!
  

