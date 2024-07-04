# Here's a program that's supposed to draw a rhombus, like this:

  
# 1.
# Run the program. It doesn't work!

# 2.
# It seems like the last turn and side are wrong. Try changing them to draw the rhombus correctly.

# 3.
# Don't forget to mark your program!

from turtle import *

small_turn = 60
big_turn = 180 - small_turn

forward(75)
left(small_turn)
forward(75)
left(big_turn)
forward(75)
left (small_turn)
forward (75)

#fix the bugs above
