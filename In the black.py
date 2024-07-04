# Write a program that works out whether your bank balance is in the red. If the number of dollars is zero or positive it should work like this:

# Number: 50
# In the black :)
# ​
# But when your balance goes negative, your program should work like this:
# Number: -1
# In the red :(
# ​


num = int(input("Number: "))

if num < 0 :
 print ("In the red :(")
else:
 print ("In the black :)")