# Lets make a sunset! We'll ask the user how long the rays should be.

# Our program will work like this:

# Length? 80
# ​
  
# Our sun has 7 rays, and the angle between each ray is 30°.

# 1.
# Set the pen to have a colour of orangered and a size of 5. Then ask for the length of the rays and save that to a variable. Remember to convert it to an integer!

# 2.
# Create a for loop. It should use range to draw 7 rays.

# 3.
# For each ray, move forward by the length you stored in the variable, then backward the same distance.

# Then, turn left 30 degrees.

# 4.
# Run your program to check how it works. Remember, it should work for any rays of any length:

# Length? 25
# ​
# Once you think it's working well, press mark!



from turtle import *

color('orangered')
pensize(5)

word = int(input("Length? "))
for i in range(7):
  forward(word)
  backward(word)
  left(30)


