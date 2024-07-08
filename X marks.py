# You're familiar with the story of Hansel and Gretel, so when you decide to go exploring you always make sure to keep track of where you've come from. Since you know how unreliable leaving a trail of breadcrumbs is, you decide to write a program to help you map out your trail.

# Your program should first read in the size of the grid that you will be exploring, and then read in directions: left, right, up or down. You always start exploring at the top left of your map. After every step, you should print out the trail, reading in directions until a blank line is entered.

# Your program should work like this:

# Grid size: 3
# x..
# ...
# ...
# Direction: right
# xx.
# ...
# ...
# Direction: down
# xx.
# .x.
# ...
# Direction: right
# xx.
# .xx
# ...
# Direction: 
# ​
# You will never be directed off the edges of the map.



def go():
  for row in table:
    print (''.join(row))

table = []
colo = 0 
r = 0
ram = int(input("Grid size: "))
for i in range(ram):
  row = []
  for j in range(ram):
    row.append(".")
  table.append(row)
table[0][0] = 'x'

go()
dir = input("Direction: ")


while dir != '':
  
  if dir == 'right':
    colo += 1
    table[r][colo] = 'x'
  elif dir == 'left':
    
    colo -= 1
    table[r][colo]= 'x'
  elif dir == 'down':
    r += 1
    colo += 0
    table[r][colo]= 'x'
  elif dir == 'up':
    r -=1
    colo += 0
    table[r][colo]= 'x'
    
  
  
  go()

  dir = input("Direction: ")
  



    
