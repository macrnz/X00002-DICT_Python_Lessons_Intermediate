import os
clear = lambda: os.system("clear")

clear()

text = open("note.txt", "r")
print(text.read())
text.close()

text = open("note.txt", "r")
print("\n" + text.readline())
text.close()

text = open("note.txt", "r")
for x in text:
    print("\n")
    print(x)
text.close()