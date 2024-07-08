# You were working hard writing a letter to your penpal, only to realise that your dog has been "helping" and contributing to the letter too! You notice that every few lines starts with WOOF! and includes things you simply didn't write!

# Write a program to read in lines from the file letter.txt and write out a new file, fixed.txt, which contains the only lines that do not start with WOOF!.

# For instance, given the following letter.txt:

# My vegetable garden is growing really well!
# WOOF! Let's play catch!
# The tomatoes and cucumbers are nearly ready to eat.
# How is your garden going?
# WOOF! I better chase that possum!
# your program should create the file fixed.txt that contains:

# My vegetable garden is growing really well!
# The tomatoes and cucumbers are nearly ready to eat.
# How is your garden going?
# ​



# Open the letter.txt file for reading
with open('letter.txt', 'r') as input_file:
    # Read all lines from the file
    lines = input_file.readlines()

# Filter out lines that start with "WOOF!" and exclude empty lines
filtered_lines = [line for line in lines if not line.startswith('WOOF!') and line.strip()]

# Open the fixed.txt file for writing
with open('fixed.txt', 'w') as output_file:
    # Write the filtered lines to the new file
    output_file.writelines(filtered_lines)


