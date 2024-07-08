# Write a program that takes a list of student names and sorts them to create a class roll. The list of names will be given on a one line separated by a single space.

# Your program should work like this:

# Students: Peng Ivan Alan Jodi Macy
# Class Roll
# Alan
# Ivan
# Jodi
# Macy
# Peng
# ​
# The students' names will always be in title case (the first letter capitalised and the rest of the name in lower case)


student_names = input("Students: ").split()
student_names.sort()


print ("Class Roll")
for i in student_names:
  print(i)



