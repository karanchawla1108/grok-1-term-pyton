# he votes are in… and it's up to you to make sure the correct winner is announced!

# You've been given a CSV file called nominees.csv, which contains the names of various movies nominated for a prize, and the people who should be announced as the recipient. The file will look like this:

# title,director(s)
# Schindler's List,Steven Spielberg
# "O Brother, Where Art Thou?","Joel Coen, Ethan Coen"
# 2001: A Space Odyssey,Stanley Kubrick
# "Sherlock, Jr.","Buster Keaton, Roscoe Arbuckle"
# You should write a program that reads in nominees.csv, asks for the name of the winning title, and prints out specific congratulations. For example, with the above file, your program should work like this:

# Winning title: O Brother, Where Art Thou?
# Congratulations: Joel Coen, Ethan Coen
# ​
# Here is another example, using the same file:

# Winning title: Schindler's List
# Congratulations: Steven Spielberg
# ​
# Remember
# Don't hard-code these substitutions, as we will test your code with different sets of abbreviations in the nominees.csv file.



import csv
nominees = []
with open('nominees.csv', 'r') as file:
    for line in csv.DictReader(file):
        # print(line['title'])
        # print(line['director(s)'])
        nominees.append(line)
        #print(nominees)

word = input("Winning title: ")
#loop in nominees.
for i in nominees:
  if word == i['title']:
    print(f"Congratulations: {i['director(s)']}")
        