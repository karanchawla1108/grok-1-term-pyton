# Someone's written a program to convert 3600 seconds to hours.

# It's not working! It's got a bug (an error in the program).

# 1.
# Run the program and see what happens.

# Python gives a TypeError. What do you think this means?

# Remember, numbers and strings are different types of data. A TypeError says something in our program might be the wrong type.

# 2.
# Fix the bug!

# The error happens when we try to divide seconds by 60.

# That's because the seconds variable stores a string instead of a number. Can you fix it by changing only the first line?

# 3.
# Run the program again and see if it works.

# It should print:

# 1.0
# 4.
# Don't forget to mark your program!


seconds = 3600

hours = seconds / 60 / 60

print(hours)



