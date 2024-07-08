# ou and your friends decide to play a game of multilingual scrabble. However, you've having trouble remembering how much each letter is worth in different languages.

# You decide to write a program to help you score each word, reading in the points for each letter from a file called scrabble_letters.txt, which looks like this:

# 1 E
# 1 A
# 1 I
# 1 N
# 1 O
# ... etc
# Your program should work like this:

# Word: hello
# 8 points
# ​
# Here is another example:

# Word: kiwi
# 11 points
# ​
# Here's an example when scrabble_letters.txt uses the scores from the letter scores from the French version of Scrabble:

# Word: kiwi
# 22 points
# ​


# Load letter scores from file
scores = {}
with open('scrabble_letters.txt', 'r') as file:
    for line in file:
        score, letter = line.split()
        scores[letter] = int(score)
        

user_input = input("Word: ").strip()
#print(user_input)
    

total_score = sum(scores[char] for char in user_input.upper() if char in scores)

print(f"{total_score} points")



