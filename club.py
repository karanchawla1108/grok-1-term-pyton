# You and your friends have a super cool club house in Narnia. You want to send messages to each other about when to meet up, but you want to keep the location secret from prying eyes!

# Write a program that asks the user for a message. If it contains the word Narnia, replace it with REDACTED. Otherwise, it should print No words redacted.

# It should work like this:

# Message? Meet you at 3pm in Narnia.
# Meet you at 3pm in REDACTED.
# ​
# Here's what happens when no one mentions Narnia:

# Message? Wanna go to the movies later?
# No words redacted
# ​
# 1.
# Ask the user for a message.

# 2.
# Check if the word Narnia is in the message.

# 3.
# If it is, replace Narnia with REDACTED, and print out the new censored message.

# 4.
# Otherwise, print No words redacted instead.




message = input("Message? ")
if 'Narnia'in message:
 new_msg = message.replace('Narnia','REDACTED')

 
 print(new_msg)
else:
  print ("No words redacted")
   
