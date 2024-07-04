# <!-- Australian tennis player Sam Groth has the record for the fastest recorded serve, at 263 km/h!

# To be on the top 20 list of fastest recorded ATP serves you need a serve that's at least 230 km/h.

# Write a program to see how your serve ranks:

# Serve Speed	Output
# Greater than 263	New ATP record!
# 230 to 263	Top 20!
# Less than 230	Keep working on that serve.
# Here's a record-breaking serve:

# Serve speed? 265
# New ATP record!
# ​
# This is what happens when it's fast (at least 230 km/h), but doesn't break the record:

# Serve speed? 240
# Top 20!
# ​ -->


speed = int (input("Serve speed? "))

if speed > 263:
 print ("New ATP record!")
elif speed >= 230 and speed <= 263 :
 print ("Top 20!")
else :
 print ("Keep working on that serve.")
