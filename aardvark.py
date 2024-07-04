# The aardvark ("digging foot") is a medium-sized, burrowing, nocturnal mammal native to Africa.

# Write a program to detect aardvarks in an input string. Your program needs to find cases where the exact string aardvark appears anywhere inside the input string. For example:

# Enter line: There are aardvarks under the bed.
# Aardvark!
# ​
# When the user enters a line without aardvark:

# Enter line: This line has none
# No aardvarks here :(


line = input("Enter line: ")
if 'aardvark' in line:
    print ("Aardvark!")
else: 
    print ("No aardvarks here :(")