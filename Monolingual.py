# After starting a new job, you observe that your workplace seems very multilingual. That is, a lot of people seem to be able to speak more than one language. You decide to do a survey of your coworkers to find out what languages they can all speak. Write a program to output the names of the people who can speak only one language (they are monolingual).

# Read in one or more lines of input from the user. Each line will be a space separated list of the names of your coworkers who can speak a certain language. The name of the language will be the first thing on the line.

# The first line of input will always be English, and you can assume that everyone at your workplace can speak English.

# Here is an example interaction between your program and the user:

# Line: English Tim Nicky James Tara John Ben
# Line: German Nicky Tim
# Line: Mandarin Tim John
# Line: 
# James is monolingual.
# Tara is monolingual.
# Ben is monolingual.
# Your program can output the names of your monolingual coworkers in any order. If there are no monolingual coworkers, your program should output Everyone is multilingual!.

# Line: English Boris Aleksei Dmitry Ivan
# Line: Russian Dmitry Ivan Boris Aleksei
# Line: 
# Everyone is multilingual!
# Hint
# You might want to consider using set difference for this question.




english_speakers = set()
non_english = set()

while True:
    line = input("Line: ")
    if not line:
        break

    language, *names = line.split()
    if language == "English":
        english_speakers.update(names)
    else:
        non_english.update(names)

if not (english_speakers - non_english):
    print("Everyone is multilingual!")
else:
    for monolingual in (english_speakers - non_english):
        print(f"{monolingual} is monolingual.")

