# You're enjoying learning programming so much, you've decided to run your own class teaching programming basics. You've got plenty of students signing up, and now you need to make logins for each of them. Since usernames (but not first names) have to be unique, you decide to write a program to help generate them.

# You should read in the classlist.txt which contains <first name> <zero or more middle names> <last name> on each line. Your program should print out a list of usernames based on the following rules:

# Username should be a students' first and, if applicable, middle name(s), with no spaces, converted to lower case.
# If there already exists a student with that username, use their firstname plus first letter of last name converted to lower case.
# If that already exists, use firstname plus first letter of lastname, plus a number, starting at 1 and counting up as required.
# For example, given the following classlist.txt:

# classlist.txt
# Max Eisenhardt
# Katherine Pryde
# Anna Marie Darkholme
# James Howlett
# James Proudstar
# James Prindle
# James Bradley
# then your program should print out:

# max
# katherine
# annamarie
# james
# jamesp
# jamesp1
# jamesb
# ​
# You can print out the final list in the same ordering as the original file.

# Here is another example. Given the following classlist.txt:

# classlist.txt
# Sam Vimes
# Sam Flynn
# Sam Gamgee
# Sam Carter
# Sam Velo
# Sam Victory
# Sam Vega
# then your program should print out:

# sam
# samf
# samg
# samc
# samv
# samv1
# samv2
# ​


dict = []
usernames = []
with open('classlist.txt','r') as file:
  for line in file:
      first, middle, surname = '','',''
      if len(line.split())== 2:
         first, surname = line.lower().split()
         dict.append([first, '', surname])
      else:
         first,middle,surname = line.lower().split()
         dict.append([first, middle, surname])
#print(dict)

for name in dict:

  name1 = ''.join(name[0:2])
  name2 = name1 + name[2][0]
  number = 1
  if name1 not in usernames:
    usernames.append(name1)
  elif name1 in usernames and name2 not in usernames:
    usernames.append(name2)
  elif name1 in usernames and name2 in usernames:
      d = False
      while d == False:
        if name2 + str(number) not in usernames:
          usernames.append(name2+str(number))
          d = True
        else:
          number += 1
for name in usernames:
  print(name)
    

