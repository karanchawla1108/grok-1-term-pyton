# While spring cleaning your bedroom, you find a bunch of receipts for things you have purchased during the winter. Wanting to know whether you have kept to your budget or not, you decide to add up all the receipts.

# Write a Python program to read in a list of integer costs, and print out the total sum of all of the costs. For example:

# Enter the expenses: 10 2 5 15
# Total: $32
# ​
# Here is another example:

# Enter the expenses: 1 2 3 4 5 100
# Total: $115
# ​
# Hint
# Strings have a useful method to split them up into a list.



receipt = input("Enter the expenses: ").split()
result = 0
for i in receipt:
 result += int(i)

print(f"Total: ${result}")
