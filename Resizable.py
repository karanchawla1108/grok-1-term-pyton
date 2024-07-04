# One of the easiest emoticons to draw is these happy eyes ^ ^. Let's make a program that draws them any size we want, like this:

# Size? 30
# ​
  
# 1.
# Set the pencolor to skyblue and the pensize to 3. This will make it look happy.

# 2.
# Ask for the size and store it in a variable. Don't forget to convert it to an integer.

# 3.
# Turn left 60 degrees and move forward by the size variable you created. Then turn right by 120 degrees and move forward the same distance again.

# 4.
# Run your code to see where your turtle is.

# 5.
# Turn left 60 degrees, putting the turtle horizontal again. Then make a gap the same size as the other lines. Finally draw the right eye.

# 6.
# Run your code with different input, it should work for any size. If it looks right, then mark it!

# Size? 50
# ​



from turtle import *
pensize(3)
pencolor('skyblue')
size = int(input("Size? "))
left(60)
forward(size)
right(120)
forward(size)

left(60)
penup()
forward(size)
pendown()
left(60)
forward(size)
right(120)
forward(size)


