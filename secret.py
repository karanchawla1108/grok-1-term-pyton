# Have you ever dreamed of being a spy? Well here's your chance! We need you to decode some coded messages.

# The code is fairly simple – you just need to select every third letter out of a sentence (starting from the first letter), and print out those letters with spaces in between them.

# So the program should look like this:

# Message? cxohawalkldflghemwnsegfaeap
# c h a l l e n g e
# ​
# or like this

# Message? pbaynatnahproarnsm
# p y t h o n
# ​



msg = input("Message? ")


cip = ""
for i in range (0,len(msg),3):
  cip += msg[i]+" "
 
cip = cip.rstrip()
  
print (cip)

