# You are trying to log in to your old computer, and can't remember the password. You sit for hours making random guesses... I'm sure you thought it was funny back when you came up with that password (chEEzburg3rz).

# Write a program that tells you whether your guess is correct. If it is correct, it should grant access like this:

# Enter password: chEEzburg3rz
# Access granted
# ​
# If your guess is incorrect it should deny access like this:

# Enter password: lolcatZ
# Access denied
# ​
# Remember the correct capitalization is important for passwords!




passwd = input("Enter password: ")

if passwd == "chEEzburg3rz":
 print ("Access granted")
else:
 print ("Access denied")