# Let's draw some dandelions! We'll write a function to draw one dandelion. Then we can call it as many times as we like to draw a whole field of flowers!

   
# 1.
# Use def to define a function called dandelion. It should have three parameters: x (the x-coordinate), y (the y-coordinate), and length (the length of each petal).

# 2.
# Inside the function, start by getting into position to draw the stem. Lift the pen and the move to the right coordinates. We'll use the x argument for the x-coordinate, and -150 for the y-coordinate. Don't forget to put the pen back down!

# 3.
# Now we'll draw the stem! Set the pensize to 3 and the pen colour to '#91F485'. To draw the stem, move to the coordinates x and y (the parameters of your function).

# 4.
# Before we start on the dandelion we need to calculate the angle to turn between each petal. There are 40 petals in all. Work out the angle the turtle will need to turn between each line to perform a full revolution, and save it to a variable.

# 5.
# Set up a for loop to draw the dandelion. We'll draw two petals in each loop, so we'll need to loop 20 times.

# 6.
# Inside the for loop, set the pen color to "#0085C7", then move forward using the length argument. Move backward to the starting position, then turn using the angle you calculated earlier.

# Then, set the pen to a different colour, "#009F3D", and repeat the same steps to draw a second petal. Remember to turn again at the end!

# 7.
# Run your code to test your function! We've already called the function to draw one dandelion. It should look like this:


# Want to draw a whole field of flowers? Add more tests inside the if __name__ == "__main__" block.




from turtle import *

# Define your dandelion function here:
# Define a function.
def dandelion(x, y, length):
# 2 position the stem.
  penup()
  goto(x,-150)
  pendown()
  
# 3 Draw the stem.
  pensize(3)
  pencolor('#91F485')
  goto(x,y)
  
# 4 start the dandelion.
  angle = 360/40
# 5 Draw the dandelion.
  for _ in range(20):
    pencolor("#0085C7")
    forward(length)
    backward(length)
    left(angle)
    pencolor("#009F3D")
   
    forward(length)
    backward(length)
    left(angle)

    

 
if __name__ == "__main__":
  # Test your function
  bgcolor('#ECFAF5')
  dandelion(-0, 50, 60)
  
  # Add your own tests here:
  