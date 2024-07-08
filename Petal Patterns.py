# Now, we're going to combine everything we've learnt in this module to draw flowers with different numbers of petals.

# We've provided a function to draw a petal. You need to write a program to draw the whole flower.

# Here is an example of how your program should work with 5 petals:

# How many petals? 5
  
# 1.
# Set the pen size to 5, the background colour to 'lightgreen', and the fill colour to 'hotpink'.

# 2.
# Ask the user 'How many petals? ', and save it to a variable. Don't forget to save it as an int!

# 3.
# To draw the whole flower we'll draw the petals in a circle.

# Work out the angle you'll need to turn in between drawing each petal, and store the answer.

# angle
# =
# 360
# ∘
# number of petals
# 4.
# Begin the fill.

# 5.
# Time to draw the flower! Set up a for loop using the number of petals for the range.

# Inside your for loop, call draw_petal and give it the colour 'purple' as an argument.

# Finally, turn left using the angle you calculated earlier.

# 6.
# Finish off the flower by ending the fill outside the for loop.

# Here is an example of a flower with 7 petals:

# How many points? 7






from turtle import *

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

# Write your code below!
pensize(5)
bgcolor('lightgreen')
fillcolor('hotpink')
nm = int(input("How many petals? "))
angle = 360 / nm
begin_fill()

               
for i in range(nm):
 draw_petal('purple')
 left(angle)
end_fill()
 
               
               

