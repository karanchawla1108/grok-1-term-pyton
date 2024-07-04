# You're playing battleships, but you keep forgetting which squares in the grid you've already selected! Write a program to help you keep track of which squares you've hit.

# Your program should read in coordinates, one per line. If you haven't tried that square before, your program should print out Hit <co-ordinates>. If you have tried those coordinates already, you should print out You've chosen that square already.

# Your program should run until a blank line is entered, and should work like this:

# Guess: A3
# Hit A3
# Guess: C4
# Hit C4
# Guess: A3
# You've chosen that square already
# Guess: B2
# Hit B2
# Guess: 


battleship = set()

guess = input("Guess: ")

while guess:
  
  if guess in battleship:
    print("You've chosen that square already")
    
  elif guess not in battleship:
    battleship.add(guess)
    print ("Hit" + " " + str(guess).upper())
  guess = input("Guess: ")
    
    
