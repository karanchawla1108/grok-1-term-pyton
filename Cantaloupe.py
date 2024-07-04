# You have a friend in France who raves about her favourite fruity dessert: Cantaloupe.

# But where you live, it's totally called a Grokmelon! (well … Rockmelon) 😉

# Write a program to change every message from your friend to use the word Rockmelon instead of Cantaloupe.

# Your program should work like this:

# Message: I had some yummy Cantaloupe yesterday!
# I had some yummy Rockmelon yesterday!
# ​
# It should also work if Cantaloupe is mentioned more than once, like this:

# Message: Cantaloupe, sweet Cantaloupe, so delicious!
# Rockmelon, sweet Rockmelon, so delicious!
# ​
# 1.
# Ask the user for a message.

# 2.
# Use replace on the message to replace every Cantaloupe with Rockmelon, and store the result in a variable.





conv = input("Message: ")
new_mesage = conv.replace('Cantaloupe', 'Rockmelon')

print(new_mesage)

