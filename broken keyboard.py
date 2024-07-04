# Your friend's keyboard is misbehaving, and her "a", "e", and "o" keys are broken. To compensate, when she wants to type an o, she types ###. For an e she types ##, and for an a she types %%. Fed up with trying to interpret this ridiculous code, you decide to write a program to decipher her messages instead.

# Write a program to read in some text typed by your friend, and output the corrected text. Your program should work like this:

# What did she say? My k##yb0%%rd is br###k##n :(
# She meant to say: My keyb0ard is broken :(
# You can assume there will never be two vowels directly next to each other in the input text.

keyboard = input("What did she say? ")
new_keyboard = keyboard.replace("###", "o").replace("##", "e").replace("%%", "a")
print("She meant to say: " + str(new_keyboard))
 
