# One of the first things we teach kindergarten children is to count to ten, but since computers are so good at maths, we can train ours to count to n instead.

# Write a program that asks for a number, n, and then prints out all the numbers between 1 and n. Your program should work like this:

# Enter a number: 7
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# ​



n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)
