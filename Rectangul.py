# Let's draw a city! We'll use a function to draw each rectangle building so we don't have to keep repeating our code.

  
# We've started your function already; it's called draw_rect. It has three parameters:

# width — number of turtle steps
# height — number of turtle steps
# colour — the pencolor to use
# 1.
# First we'll set up the pen. Inside the draw_rect function, set the pen size to 3, and use the colour parameter to set the pen colour.

# 2.
# Draw the rectangle! Use the width parameter to draw the bottom side, then turn left 90 degrees. Draw the rest of the rectangle, using the height parameter for the left and right sides.

# After the last side, turn left again so the turtle is in position to draw the next rectangle!

# 3.
# Run your code! We've called your function like this:

# draw_rect(30, 120, 'royalblue')
# If your code is working, you should see the first building:

  
# 4.
# Let's call the function again to draw another building! We have already used goto to get into position at (-10, 0). Underneath, call the function again like this:

# draw_rect(80, 30, 'cornflowerblue')

# 5.
# Finally, let's draw the rest of the city. You should call the function twice more to draw two more buildings:

# A building at (-30, 0) with a width of 80, a height of 60, and the colour 'coral'
# A building at (-45, 0) with a width of 50, a height of 80, and the colour 'plum'



from turtle import *

def draw_rect(width, height, colour):
  # Finish the function to draw a rectangle:
  pencolor(colour)  
  pensize(3)
  forward(width)     
  left(90)  
  forward(height)
  left(90)
  forward(width)
  left(90)
  forward(height)
  left(90)
  

  
  

# Draw the first building:
draw_rect(30, 120, 'royalblue')
goto(-10, 0)

# Draw the rest of the buildings:
draw_rect(80, 30, 'cornflowerblue')

# final step1.
goto(-30,0)
draw_rect(80, 60, 'coral')

goto(-45, 0)
draw_rect(50, 80, 'plum')










