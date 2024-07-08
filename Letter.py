# You live in a big apartment block, and sorting mail and parcels is quite a complex task. Write a program that reads in a file with all the deliveries, asks for the user's name and prints out a summary of all the mail.

# Your program should read in a file named mail.txt that looks like this:

# Jane Fairfax,Letter
# Frank Churchill,Letter
# Emma Woodhouse,Letter
# Frank Churchill,Letter
# Harriet Smith,Package
# Emma Woodhouse,Letter
# Philip Elton,Package
# Emma Woodhouse,Package
# Your program should work like this:

# Name: Emma Woodhouse
# 2 Letters
# 1 Package
# ​
# Here is another example:

# Name: Jane Fairfax
# 1 Letter
# No Packages
# ​
# If the person doesn't have any mail, your program should work like this:

# Name: Elizabeth Bennet
# No mail
# ​
# Hint
# Be careful with the pluralisation of Letters and Packages.

with open ('mail.txt','r') as file:
  lines = file.readlines()
  #print (files)
letter = 0 
package = 0
name = input('Name: ')
for line in lines:
  #print(line.strip())
  part = line.split(',')
  # print(part[0])
  # print(part[1])
  if part[0].strip() == name and part[1].strip() == 'Letter':
    letter += 1
    #print(letter)
  elif part[0].strip() == name and part[1].strip() == 'Package':
    package +=1
    #print(package)
num = {'l1': 'Letter', 'p1': 'Package'}

if letter == 0 and package == 0:
    print('No mail')
elif letter == 0:
    print("No Letters")
    print(f"{package} {num.get('p'+str(package), 'Packages')}")
elif package == 0:
    print(f"{letter} {num.get('l'+str(letter), 'Letters')}")
    print("No Packages")
else:
    print(f"{letter} {num.get('p'+str(letter), 'Letters')}")
    print(f"{package} {num.get('p'+str(package), 'Packages')}")

