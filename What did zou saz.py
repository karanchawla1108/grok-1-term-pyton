# Entschuldigung, können Sie Englisch sprechen?

# During your holiday in Germany, you decide its time to write some emails to your friends back home. Wandering into an Internet café, you soon realise that most German keyboards have a different layout to English keyboards.

# German Keyboard
# Image source
# The y and z keys swapping position is messing with your touch typing. You decide to write out your email as if the keys were in the correct position and then use Python to swap all ys and zs.

# Your task here is to write a function called fix_yz. This function takes a single argument which will be a string. Your function needs to return this string with all of the ys and zs swapped, and all of the Ys and Zs swapped.

# Here are some example calls to your function:

# s = fix_yz('What did zou saz?')
# print(s)
# What did you say?
# ​
# s = fix_yz('Zour tip about the yoo was a great one!')
# print(s)
# Your tip about the zoo was a great one!
# ​
# s = fix_yz('We onlz have one week left :(')
# print(s)
# We only have one week left :(
# ​
# Hint
# The auto-marker is expecting you to submit only your fix_yz function definition. You should not include any calls to your function.






def fix_yz(s):
    # Create a translation table to swap 'y' with 'z', 'z' with 'y', 'Y' with 'Z', and 'Z' with 'Y
    translation_table = str.maketrans('yzYZ', 'zyZY')
    
    # Use the translate method to apply the translation
    s = s.translate(translation_table)
    
    return s









