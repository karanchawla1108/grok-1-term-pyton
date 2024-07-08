# As part of your new exercise regime, you're doing a lot of drills up and down stairs. In order to help you get motivated for tomorrow's set of stairs, you decide to write a program to visualise how many stairs you're going to need to run up.

# Write a program to ask the user for how many steps to draw. The user will always enter an integer greater than zero. For example, if the user entered 4, your program should output:

# How many steps? 4
# __
#   |_
#     |_
#       |_
# ________|
# ​
# The horizontal lines are created using underscores (_) and the vertical lines using the pipe character (|). Here is another example interaction between your program and the user:

# How many steps? 1
# __
# __|
# ​



steps = int(input("How many steps? "))
#print("__")
step= 0  # Define step before the loop
if steps == 1:
  print("__")
  print("__|")
  #print ("__")
else:
  print("__")
  for step in range(steps-1):
     print (2 * " " + " " * 2 * step + "|" + "_")
  print (step * "__" + "___"+ "_|")
  

