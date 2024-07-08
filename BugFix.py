# You want to automatically convert statements to questions. Let's write a program to do it!

# We've defined a function called questionify that takes one argument called text.

# Complete the function so it replaces all exclamation marks with question marks. For example:

# print(questionify('How did you do that!'))
# How did you do that?
# ​
# Here's another example:

# print(questionify('Oh no!!! Why!'))
# Oh no??? Why?
# ​
# 1.
# Inside your function, replace all ! with ? in the text.

# Remember to store the new string in a variable!

# 2.
# Your program should return the new string!

# 3.
# Run your program to see the output of the tests!

# Testing your function
# We've given you an if __name__ == '__main__': block. Any code inside this if statement will not affect the marking.

# Marking your function
# We mark your function with the exact function name given.
# It should not use input or print.
# It should return the result, rather than print it.


# Replace the exclamation marks with question marks.
def questionify(text):
  # Complete this function! Write your code below:
  repl1 = text.replace('!', '?')
  return repl1
  
  
if __name__ == '__main__':
  # You can use this to test your function.
  # Any code inside this if statement will be ignored by the automarker.
  
  # Test the first example in the question.
  print(questionify('How did you do that!'))
  
  # Test the second example in the question.
  print(questionify('Oh no!!! Why!'))

  # You can add more tests here!
  

