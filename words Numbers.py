# Write a function that takes a string like 'one five two' and returns the corresponding integer (in this case, 152). A function just like this would be used in a speech recognition system (e.g. automated phone taxi bookings) to convert a spoken number into an integer value.

# Here is an attempt that won't work. Your task is to replace the function body with something that works:

# def words2number(s):
#   return int(s)
# Our marking system will call your words2number function directly, so be sure to keep the name the same.

# Here is another example of how your program should work:

# print(words2number('one five two'))
# Should result in this being printed out:

# 152
# Hint
# Note that the number returned should be an integer, not a string!



def words2number(s):
    s = s.lower()
    result = 0
    words = s.split()
    word_to_number = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    for word in words:
        if word in word_to_number:
            result = result * 10 + word_to_number[word]
    return result
