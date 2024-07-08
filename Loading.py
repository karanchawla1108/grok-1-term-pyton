# Don't you hate waiting for something to load?

  
# Let's draw our own loading indicator using two functions:

# draw_line(value) to draw a single line, and
# load_indicator(num_lines) to draw the full loading indicator.
# We will test each function separately.

# 1.
# Write the draw_line(value) function. It has one parameter, value, which we'll use to set an RGB colour. Inside the function:

# Set the pen colour by using the same value argument for the red value, the green value, and the blue value.
# Set the pensize to 8.
# Lift the pen and create a space of 30 steps, then put it back down.
# Draw a line 40 steps long.
# Testing draw_line
# Run your program to test it so far!

# We've called draw_line(100) inside the if __name__ == "__main__" block. It should look like this:

  
# 2.
# Now, define the second function: load_indicator(num_lines). load_indicator has one parameter, num_lines — the number of lines the indicator will have. Inside the function:

# Create a variable to store a colour value. We called ours colour_value. Set the variable to 0 to start. We'll change the colour value each time we loop!
# Calculate the angle you'll need to turn between each line: 360 divided by num_lines. Store it in another variable.
# Set up a for loop. It should repeat for each of the lines you need to draw.
# Inside the for loop, call the draw_line function we defined earlier. Pass in your colour_value variable as the argument.
# Inside the loop, get into position to draw the next line. Lift the pen and move back to the starting position (0, 0), then turn left, using the angle you calculated.
# Inside the loop, update the value of your colour_value variable by adding 20, like this:
#     colour_value = colour_value + 20
# Testing load_indicator
# Inside the if __name__ == "__main__" block delete draw_line(100).

# Then, call the load_indicator function instead. Calling load_indicator(12) should draw an indicator with 12 lines:

  
# You can call load_indicator passing in other numbers, but it won't work with more than 13 lines. Can you think why that is? Remember, RGB colour values have a maximum of 255!



from turtle import *

# Define the draw_line function here:
def draw_line(value):
  pencolor(value,value,value)
  pensize(8)
  penup()
  forward(30)
  pendown()
  forward(40)
  
  

# Define the load_indicator function here:
def load_indicator(num_lines):
    colour_value = 0 
    angle = 360/num_lines
    
    for _ in range(num_lines):
      draw_line(colour_value)
      penup()
      goto(0,0)
      left(angle)
      colour_value = colour_value + 20

if __name__ == "__main__":
  # Write your tests here!
  # Anything indented inside this block will be ignored by the marker.
  # Test draw_line:
  #draw_line(100)
  load_indicator(12) 
  
