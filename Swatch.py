# Have you ever seen a colour swatch like the Pantone Colour of the Year?

# We're going to draw a grid of swatches. Just like the last problem, we'll use a function to draw each swatch.

# We've started your function as draw_swatch. It has three parameters:

# x (the x-coordinate)
# y (the y-coordinate)
# colour (the name of the fill colour)
# 1.
# First we need to get into the right position. Inside the function, lift the pen, go to the (x, y) coordinate (using the x and y parameters), then put the pen back down.

# 2.
# Now, let's set up the pen. Set the pen size to 2 and set the fill colour using the colour parameter.

# 3.
# Begin the fill. To draw the square, move forward 30 steps, then turn left. Repeat this three more times (you might want to use a for loop!). Make sure you turn left after drawing the last side so your turtle is in place for the next square.

# Don't forget to end the fill!

# 4.
# Run your program to see if it works. We've called your function like this:

# draw_swatch(-60, 50, 'yellow')
# If your code is working, you should see the first swatch:

  
# 5.
# Keep calling your draw_swatch function to draw more swatches, with these locations and colours:

# (-15, 50), 'gold'
# (30, 50), 'lightsalmon'
# (-60, 0), 'DarkSeaGreen2'
# (-15, 0), 'PaleGreen3'
# (30, 0), 'plum'
# (-60, -50), 'skyblue'
# (-15, -50), 'cornflowerblue'
# (30, -50), 'orchid3'


from turtle import *

# Draws one swatch
def draw_swatch(x, y, colour):
  # Complete the function to draw a swatch:
  penup()
  goto(x,y)
  pendown()
  #Instruction 2
  pensize(2)
  fillcolor(colour)
  begin_fill()
  #Instruction 3
  for _ in range(4):
   forward(30)
   left(90)
  end_fill()
  
  
  
# Draw the grid
draw_swatch(-60, 50, 'yellow')
# Add more swatches here:
draw_swatch(-15, 50, 'gold')
draw_swatch(30, 50, 'lightsalmon')
draw_swatch(-60, 0, 'DarkSeaGreen2')
draw_swatch(-15, 0, 'PaleGreen3')
draw_swatch(30, 0, 'plum')
draw_swatch(-60, -50, 'skyblue')
draw_swatch(-15, -50, 'cornflowerblue')
draw_swatch(30, -50, 'orchid3')


