# Can you raed tihs stencence? Apparently, the human brain can read misspelt words fairly easily as long as two things are true — the misspelling is an anagram of the correct spelling, and the first and last letters of the word are still the same.


# Image source
# Two words are anagrams of each other if they contain the same letters in them. So left is an anagram of felt and vice-versa. A Super Anagram is a special kind of anagram. A Super Anagram is an anagram whose first and last letters are the same.

# Your program needs to read in two words on a single line. If the pair of words are Super Anagrams of each other, print out Super Anagram!. If the pair of words is not a Super Anagram (so a human couldn't read it), then print out Huh?. For one-letter words, the first letter is the last letter.

# So, for example:

# Enter words: brain brian
# Super Anagram!
# ​
# and another example:

# Enter words: too two
# Huh?
# ​
# Hint
# You should work out what list('monkey') returns




words = input("Enter words: ")
word_list = words.split()

# Check if the words are super anagrams
if sorted(word_list[0]) == sorted(word_list[1]) and word_list[0][0] == word_list[1][0]:
    print("Super Anagram!")
else:
    print("Huh?")
