# Most non-smartphone mobile phones have keypads like this:


# Image source
# Given a word of input, all in uppercase letters, print the numbers you would need to type on a standard mobile phone keypad to enter that word. Assume that the phone can perfectly predict the word you want, and there are no numbers or punctuation symbols in the word.

# For example:

# Enter word: GROK
# 4765
# ​
# 4765 is printed out since GROK is entered by pressing 4, 7, 6, and 5.

# Hint
# You probably want to start with a dictionary something like this:

  
# KEYPAD = {
#     'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
#     'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
#     'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
#     'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
#     'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
#     'Z': '9',
# }



# A dictionary containing the letter to digit phone keypad mappings.
KEYPAD = {
    'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
    'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
    'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
    'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
    'Z': '9',
}
result = ""

word = input ("Enter word: ").upper()
for char in word:
  result += KEYPAD[char]
print (result)
  





