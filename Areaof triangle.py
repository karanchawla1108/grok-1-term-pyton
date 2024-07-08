# Define a function named triangle_area that calculates the area of a triangle using this formula:

# area = ½ ⨉ base ⨉ height

# Your function should have two parameters:

# base: the base of the triangle
# height: the height of the triangle
# It should return the area of the triangle as a number.

# For example, if we called your triangle_area function like this:

# answer = triangle_area(10, 6)
# print(answer)
# then it should return:

# 30.0
# ​
# Here's another example:

# answer = triangle_area(5, 3)
# print(answer)
# 7.5
# ​
# 1.
# Use def to define a function called triangle_area. It should have two parameters: base and height (in that order).

# 2.
# Inside your function, calculate the area of the triangle using the base and height, and return the answer.

# 3.
# Add another test case to calculate the area of a triangle with a base of 15 and a height of 10. Then run your program to see the output of the tests!

# Testing your function
# We've given you an if __name__ == '__main__': block. Any code inside this if statement will not affect the marking.

# Marking your function
# The automarker will look for the function called record_check:

# We mark your function with the exact function name given.
# It should not use input or print.
# It should return the result, rather than print it.



# Define your function here!
def triangle_area(base, height):
  area = 0.5*base*height
  return area

if __name__ == '__main__':
  # You can use this to test your function.
  # Any code inside this `if` statement will be ignored by the automarker.

  # Run your `triangle_area` function with the first example in the question.
  print(triangle_area(10, 6))
  
  # Run your `triangle_area` function with the second example in the question.
  print(triangle_area(5, 3))
  
  # You can add more tests here!
  print(triangle_area(15,10))
