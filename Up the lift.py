# The lift is broken! It can still go up and down, but doesn't display what floor it's at anymore, which is causing confusion for people trying to use it.

# Write a program that will display the floor numbers on an elevator that is going up. Your program should read in the current floor and read in the destination floor, which will always be higher than the current floor. Your program should print out each of the floor numbers in-between.

# Current floor: 3
# Destination floor: 6
# Level 3
# Level 4
# Level 5
# Level 6
# ​
# Current floor: 1
# Destination floor: 2
# Level 1
# Level 2






floor_1=int(input("Current floor: "))
floor_2=int(input("Destination floor: "))
for i in range(floor_1, floor_2+1):
 print("Level", i)
              