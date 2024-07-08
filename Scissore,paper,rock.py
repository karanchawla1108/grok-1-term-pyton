# Let's play a game of Scissors, Paper, Rock, throwing in an extra Lizard and Spock! This variant of the game adds a few extra rules:

# Scissors cut Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock melts Scissors
# Scissors decapitate Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock breaks Scissors

# Image source
# Your program should work like this, using the exact rules above. All hands will be in lower case.

# Hand 1: rock
# Hand 2: scissors
# Rock breaks Scissors
# ​
# Your program should play one game and then stop. Here are some more examples:

# Hand 1: paper
# Hand 2: lizard
# Lizard eats Paper
# ​
# Hand 1: rock
# Hand 2: rock
# Tie
# ​



RULES = {
    ('scissors', 'paper'): 'Scissors cut Paper',
    ('paper', 'rock'): 'Paper covers Rock',
    ('rock', 'lizard'): 'Rock crushes Lizard',
    ('lizard', 'spock'): 'Lizard poisons Spock',
    ('spock', 'scissors'): 'Spock melts Scissors',
    ('scissors', 'lizard'): 'Scissors decapitate Lizard',
    ('lizard', 'paper'): 'Lizard eats Paper',
    ('paper', 'spock'): 'Paper disproves Spock',
    ('spock', 'rock'): 'Spock vaporizes Rock',
    ('rock', 'scissors'): 'Rock breaks Scissors',
}

hand1 = input("Hand 1: ").lower()# hands gonna any output from the condition.

hand2 = input("Hand 2: ").lower() 

if hand1 == hand2:
    print("Tie")
elif (hand1, hand2) in RULES:
    print(RULES[(hand1, hand2)])
else:
    print(RULES[(hand2, hand1)])

