# Write a program to cheer for your favourite team at the sports carnival. Since I don't play any real world sports, my program would work like this:

# Cheer: gryffindor
# Give me a g, g!
# Give me a r, r!
# Give me a y, y!
# Give me a f, f!
# Give me a f, f!
# Give me a i, i!
# Give me a n, n!
# Give me a d, d!
# Give me a o, o!
# Give me a r, r!
# What does it spell?
# GRYFFINDOR
# ​
# Here's another example of how your program should work:

# Cheer: hello
# Give me a h, h!
# Give me a e, e!
# Give me a l, l!
# Give me a l, l!
# Give me a o, o!
# What does it spell?
# HELLO
# ​

number = input ("Cheer: ")
output = 0 

for i in number:
 print ("Give me a "+ str(i) + ", "+str(i) + "!")

print("What does it spell?")
print(number.upper())
  
 




