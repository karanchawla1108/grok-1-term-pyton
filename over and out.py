# Radio is a great way to communicate, it's been used for over 100 years! To make talking on the radio fast and understandable there are special code words we use, these are part of the radiotelephony procedure.

# Write a program to help explain a few of these code words.

# Radio Word	Explanation
# ROGER	Message received
# WILCO	Understood and will comply
# OVER AND OUT	Ending transmission
# Your program should ask for the radio message then print out the explanation. For example:

# Radio message: ROGER
# Message received
# ​
# Here is another example:

# Radio message: OVER AND OUT
# Ending transmission
# ​
# If the radio message isn't one of the three above, your program should print that it does not know and call for help: Unknown radio message! MAYDAY MAYDAY!
# For example:

# Radio message: BREAK
# Unknown radio message! MAYDAY MAYDAY!
# ​
# 1.
# Ask the user for the message using input.

# 2.
# Add an if statement to check if the message is ROGER. If it is, print out: Message received

# 3.
# Use elif statements to check the other two messages in the table.

# 4.
# Finally, use an else to print out Unknown radio message! MAYDAY MAYDAY! for all other messages.

# 5.
# Run your program and try it out!



radio = str(input("Radio message: "))

if radio.lower() == "roger":
 print ("Message received")
elif radio.lower() == "wilco":
 print ("Understood and will comply")
elif radio.lower() == "over and out":
 print ("Ending transmission")
else:
 print ("Unknown radio message! MAYDAY MAYDAY!")