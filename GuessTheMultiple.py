# You've devised a new twist on the traditional 'What number am I thinking of?' game to help your cousins learn their 7 times tables! Write a game that asks the user to guess the number you are thinking of. (For this game, the number will always be 42.)

# The user is allowed 10 guesses, and makes a 'Mistake!' if they guess a number that isn't a multiple of 7. A user can make a maximum of one mistake, otherwise they lose the game. When the game is over, you should always print out That was fun.

# Here is an example:

# Guess a multiple of 7: 14
# Nope!
# Guess a multiple of 7: 32
# Mistake! That number isn't a multiple of 7.
# Guess a multiple of 7: 28
# Nope!
# Guess a multiple of 7: 86
# Another mistake. Too bad.
# That was fun.
# ​
# Here is another example:
# Guess a multiple of 7: 7
# Nope!
# Guess a multiple of 7: 14
# Nope!
# Guess a multiple of 7: 126
# Nope!
# Guess a multiple of 7: 133
# Nope!
# Guess a multiple of 7: 70
# Nope!
# Guess a multiple of 7: 77
# Nope!
# Guess a multiple of 7: 63
# Nope!
# Guess a multiple of 7: 35
# Nope!
# Guess a multiple of 7: 126
# Nope!
# Guess a multiple of 7: 77
# Nope!
# No guesses left!
# That was fun.
# ​
# If the user correctly enters 42, your program should print out You won! instead of Nope!, and then not ask for any more guesses. For example:

# Guess a multiple of 7: 42
# You won!
# That was fun.
# ​
# Hint
# You can use the modulo operator (%) to find the remainder after division of one number by another. For example, to find the remainder when 9 is divided by 7:

 
# print(9 % 7)
# 2
# ​





guess = int(input ("Guess a multiple of 7: "))
mistake = 0 
ans = 42
power = 9

while guess and power != 0:
  if guess % 7 == 0:
     if guess == 42:
        print ("You won!")
        break
     else:
        print ("Nope!")
        power -=1
  elif guess % 7 != 0:
      if mistake == 0 :
        print ("Mistake! That number isn't a multiple of 7.")
        mistake = 1
        power -=1
       
      else:
        print ("Another mistake. Too bad.")
        break

  
  
  
  
  
  
  
  

  guess = int(input ("Guess a multiple of 7: "))
if power == 0:
  print ("Nope!")
  print ("No guesses left!")
print ("That was fun.")




