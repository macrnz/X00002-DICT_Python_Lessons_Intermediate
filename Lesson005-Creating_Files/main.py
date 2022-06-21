import os
clear = lambda: os.system("clear")

clear()

text = open("note.txt", "w")
text.write("What do I like about learning in Python?")

text = open("note.txt", "a")
text.write("\nWhat do I intent to do after learning Python?")
text.write("\nHow do I apply what I learned?")
text.write("\nWhat are my goals?")

text = open("note.txt", "r")
print(text.read())
text.close()