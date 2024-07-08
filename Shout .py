# The kitchen in any café is a noisy place. To make sure the orders which you have carefully written down on your notepad make it to the chef, you'll need to shout them! Write a program to read in lines of input from the file called orders.txt, and print out each line in uppercase.

# For example, if orders.txt contains:

# Tomato and cheese melt
# Pumpkin soup
# Chicken and avocado sandwich
# ​
# then your program should output:

# TOMATO AND CHEESE MELT
# PUMPKIN SOUP
# CHICKEN AND AVOCADO SANDWICH
# ​
# We've provided an example orders.txt file, but the marker will also test your program with different orders.txt files.



with open('orders.txt', 'r') as file:
  for line in file:
    print(line.upper().strip())