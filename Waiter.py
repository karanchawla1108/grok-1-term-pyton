# There are aardvarks on the loose! We need you to check whether there are any aardvarks hidden in a text file.

# To start, your program should read in a file input.txt, one line at a time, numbering the lines from 1. You should check each line to see whether the letters in the line can be used to make the word "aardvark". Uppercase letters can be used as well. So, if the file input.txt contains this:

# No aardv*rks here!
# Only armadillos and anteaters.
# Animals are run down: very awful road kill.
# I prefer a quick guacamole made from avocados.
# then your program should output:

# Aardvark on line 3
# Aardvark on line 4
# ​
# If you check carefully, you should be able to see why.

# Hint
# There are a few ways to approach this problem, but if you're not sure where to start, what is the result of this Python code:

 
# print('guacamole'.count('a'))
  


with open('input.txt', 'r') as file:
 # files = file.read()
  line_number = 1
#print(files)
#change the text all to lowercase.
  for line in file:
    files1 = line.lower()
    if (
      files1.count('a') >= 3 and
      files1.count('r') >= 2 and
      files1.count('d') >= 1 and
      files1.count('v') >= 1 and
      files1.count('k') >= 1  
    ):
      print(f'Aardvark on line {line_number}')
    line_number += 1
