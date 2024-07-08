# The Swedish Chef is one of our favourite characters on The Muppet Show, not just because of his unorthodox cooking techniques like Salad ala Boom-Boom, but also his crazy accented English, and his catch phrase bork bork bork!! There is a Swedish Chef translator you can play with online.

# In this problem, you'll write your own simplified Swedish Chef translator. Rather than write a whole program, this time you only need to write a function called eng2chef which converts a string of English into Swedish Chef speak.

# We'll even give you a simple function to start with:

# def eng2chef(s):
#   return s.lower()
# You need to replace the return s.lower() with code to perform the following translations:

# Input	Output
# tion	shun
# an	un
# th	z
# v	f
# w	v
# c	k
# o	oo
# i	ee
# Finally, if the input string ends with an exclamation mark, then the exclamation mark should be replaced with a full stop and followed by an excited bork bork bork!!. You only need to translate lowercase letters for this problem.

# Here are some examples:

# print(eng2chef('this is a chicken'))
# should print:

# zees ees a kheekken
# This example:

# print(eng2chef('have i got your knife'))
# should print:

# hafe ee goot yoour kneefe
# This example:

# print(eng2chef('action!'))
# should print:

# akshun. bork bork bork!!
# akshun. bork bork bork!!






def eng2chef(s):
  s = s.replace("tion","shun")
  s = s.replace("an","un")
  s = s.replace("th","z")
  s = s.replace("v","f")
  s = s.replace("w","v")
  s = s.replace("c","k")
  s = s.replace("o","oo")
  s = s.replace("i","ee")
  if s.endswith('!'):
    s = s[:-1] + '. bork bork bork!!'
  
  
  return s.lower()

translated_text = eng2chef('this is a chicken')


