# Before you lay down railway tracks, you have to put down sleepers. Lets draw sleepers like this:

# How many sleepers? 5
# ​
  
# Each sleeper is 100 steps long, and the gap between each sleeper is 40 steps.

# 1.
# Ask for the number of sleepers and save it to a variable. Don't forget to convert it to an integer!

# 2.
# Set the colour of the pen to gray and the size of the pen to 10.

# Lift the pen, move back 160 steps, then put it back down. Now you're in position to draw the sleepers!

# 3.
# Create a for loop using range. It will repeat for each of the sleepers you need to draw.

# 4.
# Inside the for loop turn left, draw a sleeper 100 steps long, and then return back to the start of the sleeper.

# To create the gap, lift the pen up, turn, and move the turtle 40 steps. Don't forget to put the pen back down.

# 5.
# Run your program to check how it works. Remember, it should work for any number of sleepers:

# How many sleepers? 8
# ​
# Once you think it's working well, press mark!

from turtle import *

sleepers = int(input("How many sleepers? "))
color('gray')
pensize(10)
penup()
backward(160)
left(90)
pendown()

for i in range(sleepers):
  forward(100)
  backward(100)
  #create a gap.
  penup()
  right(90)
  forward(40)
  left(90)
  pendown()
  
  
done()
  
  




