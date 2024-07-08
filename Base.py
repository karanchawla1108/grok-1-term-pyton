# In the war against Skynet, humans are trying to pass messages to each other without the computers realising what's happening.

# To do this, they are using a simple code:

# They read the words in reverse order
# They only pay attention to the words in the message that start with an uppercase letter
# So, something like:

# BaSe fOO ThE AttAcK
# contains the message:

# attack the base
# However, the computers have captured you and forced you to write a program so they can understand all the human messages (we won't go into what terrible tortures you've undergone). Your program must work as follows:

# code: soMe SuPPLies liKE Ice-cREAm aRe iMPORtant oNly tO THeir cReaTORS. tO DestroY thEm iS pOInTLess.
# says: destroy their ice-cream supplies
# ​
# Notice that, as well as extracting the message, we make every word lowercase so it's easier to read.



def decode_message(encoded_message):
    words = encoded_message.split()
    decoded_words = [word.lower() for word in words if word[0].isupper()][::-1]
    return ' '.join(decoded_words)

# Ask for user input
encoded_message = input("code: ")

print("says:", decode_message(encoded_message))
