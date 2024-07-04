# You are curious about the most popular and least popular colours of cars and decide to write a program to calculate the frequency of car colours.

# Your program should read in the colour of each car until a blank line is entered, and then print out (in any order) all the different colours of car with counts.

# For example:

# Car: red
# Car: white
# Car: blue
# Car: green
# Car: white
# Car: silver
# Car: 
# Cars that are red: 1
# Cars that are white: 2
# Cars that are blue: 1
# Cars that are green: 1
# Cars that are silver: 1
# ​
# Here is another example:

# Car: red
# Car: white
# Car: white
# Car: red
# Car: white
# Car: white
# Car: white
# Car: 
# Cars that are white: 5
# Cars that are red: 2
# ​


car_colors = {}  # Create an empty dictionary to store car color counts

while True:
    data = input("Car: ").strip()  # Read the car color from the user

    if not data:  # If the user presses Enter (blank line), exit the loop
        break

    # Check if the color is already in the dictionary, and update the count
    if data in car_colors:
        car_colors[data] += 1
    else:
        car_colors[data] = 1  # If it's a new color, set the count to 1

# Print the counts for each car color
for color, count in car_colors.items():
    print(f"Cars that are {color}: {count}")

