# We're going to draw some shapes in different shades of blue!

# We'll ask the user how many sides the shape should have.

# Here is an example with 6 sides:

# How many sides? 6
# ​
  
# 1.
# Set the background colour to 'skyblue', and the fill colour to 'royalblue'. Also set the pen size to 7 and the pen colour to 'mediumblue'. Then ask for the number of sides and save that to a variable. Remember to convert it to an integer.

# 2.
# Calculate the angle you will need to turn between each side of your shape, and save it in a variable. The angle you need to turn is:

# turn angle
# =
# 360
# ∘
# number of sides
# 3.
# Start the fill.

# 4.
# Create a for loop to draw the right number of sides. Each side should be 45 turtle steps long. Turn between each side, using the angle you calculated earlier.

# 5.
# End the fill, so that we have colour inside our shape. Make sure to end the fill outside the loop!

# Here is another example of a shape with 10 sides.

# How many sides? 10










from turtle import *
bgcolor('skyblue')
pensize(7)
pencolor('mediumblue')

num = int(input("How many sides? "))
angle = 360 / num

fillcolor('royalblue')
begin_fill()

for i in range(num):
  forward(45)
  left(angle)
end_fill()
 
  
  
  