import os
clear = lambda: os.system("clear")

clear()

groceries = {"Chicken": 8, "Apples": 6, "Cucumbers": 3, "Milk": 2, "Oranges": 4}

print(groceries)

groceries.pop("Oranges")

print(groceries)

#----------------------------------------------------------------------------------
speakers = {"Sir Rafael": 54, "Ms Joan": 33, "Ms Dana": 67}

print("\n")
print(speakers)
print(speakers.keys())

#----------------------------------------------------------------------------------
results = {"Carl": "Passed", "Quentin": "Failed", "John Y": "Passed", "Peter": "Failed", "Max T": "Failed", "Joseph": "Passed", "Jone": "Failed", "Jorge": "Failed", "George": "Failed", "Ben": "Passed", "Jerome": "Passed", "Rick": "Failed", "Max G": "Failed", "John P": "Failed", "Vince": "Passed"}

print("\n")
print(results.get("Jorge"))