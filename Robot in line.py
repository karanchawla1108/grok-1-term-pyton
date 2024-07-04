# Read a line of text from the user
line = input("Line: ")

# Convert the line to lowercase for case-insensitive comparison
line_lower = line.lower()
# Check if "robot" appears in the line in any form
if "robot" in line_lower.split():#this gonna check in the lowercase.
  
    if "robot" in line:# this gonna check in the original output.
        print("There is a small robot in the line.")
    elif "ROBOT" in line:
        print("There is a big robot in the line.")
    else:
        print("There is a medium sized robot in the line.")
else:
    print("No robots here.")
