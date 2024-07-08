# With so much exciting programming on your mind, you want to solve everything with code. You decide to write a Python function to determine which is the middle number of three numbers.

# Write a function called find_middle to find the middle number of three numbers. Your function should take three arguments. Here is a template for you to copy and fill in:

# def find_middle(a, b, c):
#   # your code here to return middle number
#   # instead of just 0
#   return 0
# Here are some example calls to your function:

# m = find_middle(4, 1, 2)
# print(m)
# Should print:

# 2
# ​
# This example:

# m = find_middle(17.5, 17.5, 17.5)
# print(m)
# Should print:

# 17.5
# ​
# This example:

# m = find_middle(0, 400, -400)
# print(m)
# Should print:

# 0
# ​
# This example:

# m = find_middle(7, 3, -12)
# print(m)
# Should print:

# 3
# ​
# Hint
# The auto-marker is expecting you to submit only your function definition. You should not include any calls to your function. Remember also that your find_middle function should return the result to the caller rather than print the result.









def find_middle(a, b, c):
  # your code here to return middle number
 number = [a,b,c]
 number.sort()
  # instead of just 0
 return number[1]












