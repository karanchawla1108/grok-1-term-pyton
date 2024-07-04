# The first step in this decision is based on the weather. If it is currently raining, you should take the bus.

# If it is not currently raining, your method of transport should be determined by the distance you need to travel. If the distance is greater than 10km, you should take the bus. If it is between 2km and 10km (inclusive), you should ride your bike, and if it less than 2km, you should walk. The distance should always be a whole number.

# Your program should only ask for the distance if it is relevant to the answer. That is, if it is raining, it shouldn't ask you how far you need to travel.

# Is it currently raining? Yes
# You should take the bus.
# ​
# Is it currently raining? No
# How far in km do you need to travel? 8
# You should ride your bike.
# ​
# Is it currently raining? No
# How far in km do you need to travel? 1
# You should walk.
# ​
# The answers provided will always be Yes, No or a whole number for distances.

# Hint




rain = input("Is it currently raining? ")
if rain.lower() == 'yes':
 print ("You should take the bus.")
 
else:
 km = int(input("How far in km do you need to travel? "))
 if (km>=2 and km <=10):
   print ("You should ride your bike.")
 elif km > 10 :
   print ("You should take the bus.")
 else :
   print ("You should walk.")
 



