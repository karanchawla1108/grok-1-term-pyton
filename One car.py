# You are watching cars go past you while you wait to cross the road and want to see whether red or blue is a more popular colour for cars. Write a program that reads in a string of the colour of each car that drives past, and then prints out the number of red cars and the number of blue cars.

# Cars: silver red white white blue white black green yellow silver white
# red: 1
# blue: 1
# ​
# Cars: blue green white black silver silver silver blue silver black silver white white silver white white yellow red red silver red
# red: 3
# blue: 2
# ​
# Cars: yellow green white silver white blue white silver yellow pink
# red: 0
# blue: 1
# ​




cars = input("Cars: ").split()

red_count = cars.count('red')
blue_count = cars.count('blue')

print(f"red: {red_count}")
print(f"blue: {blue_count}")

