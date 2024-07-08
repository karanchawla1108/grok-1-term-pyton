


# Write a program that asks the user when it rained this week, and then tells them how many days were rain free.

# An interaction with your program should look like this:

# Which days had rain? Monday Tuesday Wednesday
# Number of days without rain: 4
# ​
# Or like this:

# Which days had rain? Thurs
# Number of days without rain: 6
# ​
# You don't need to check whether the user's input makes sense (i.e. whether they have entered valid days of the week).

# Hint
# Don't get caught out by the difference between data.split() and data.split(' ') when data = '', such as might occur when there were no rainy days!



rain = input("Which days had rain? ")
split = rain.split()
cal = 7 - len(split)
print ("Number of days without rain:", cal)
