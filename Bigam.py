# In linguistics, a bigram is a pair of adjacent words in a sentence. The sentence The big red ball has three bigrams: The big, big red, and red ball.

# Write a program to read in multiple lines of input from the user, where each line is a space-separated sentence of words. Your program should then count up how many times each of the bigrams occur across all input sentences. The bigrams should be treated in a case insensitive manner by converting the input lines to lowercase. Once the user stops entering input, your program should print out each of the bigrams that appear more than once, along with their corresponding frequencies. For example:

# Line: The big red ball
# Line: The big red ball is near the big red box
# Line: I am near the box
# Line: 
# near the: 2
# red ball: 2
# the big: 3
# big red: 3
# ​
# The order of the output lines does not matter.


bigram_count = {}
while True:
    line = input("Line: ").lower()
    if not line:
        break

    words = line.split()
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_count[bigram] = bigram_count.get(bigram, 0) + 1

for bigram, count in bigram_count.items():
    if count > 1:
        print(f"{bigram[0]} {bigram[1]}: {count}")

