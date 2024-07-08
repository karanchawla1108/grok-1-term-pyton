# You're growing tomatoes in your smart garden. Make sure your tomato plants are kept at the right temperature — 21-29°C.

# Write a check_temp(temperature) function to check the temperature. If it is too warm the function should return 'Too hot!', if it's too cold it should return 'Too cold!', and if the temperature is within the optimal range it should return 'OK'.

# 1.
# Start defining a check_temp(temperature) function that always returns 'OK', then run your code to make sure you haven't made a syntax error.

# 2.
# Change your check_temp function to return 'Too hot!' if the temperature is over 29, and 'Too cold!' if the temperature is under 21.

# 3.
# Make sure you have lots of tests. You should test with temperatures that are in the optimal range, too hot, and too cold (we've provided a few tests to get you started!). Run your code and check that the output is correct.

# 4.
# Don't forget to mark it once you've finished!

# Testing your function
# We've given you an if __name__ == '__main__': block. Any code inside this if statement will not affect the marking. You can add more tests to the end of this.

# Marking your function
# Marking works by calling your function and checking what it returns, and not by running the program.

# We mark your function by calling the exact function name given.
# It should not use input or print.
# It should return the result, rather than print it.





### Write your function here
def check_temp(temperature):
  if int(temperature) > 29:
   return f'Too hot!'
  elif int(temperature) < 21:
   return f'Too cold!'
  else:
   return f'OK'

###


if __name__ == '__main__':
  print(check_temp(24))
  print(check_temp(10))

  # Add more testing here.
  print(check_temp(21))