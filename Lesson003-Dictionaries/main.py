import os
clear = lambda: os.system("clear")

clear()

#table
#Flavor: Vanilla, Chocolate, Strawberry, Cookies n Cream, Bubble Gum
#Toppings: Almonds, Banana Slices, Chocolate Syrup, Caramel Syrup, White Chocolate Chips

flavour = ["Vanilla", "Chocolate", "Strawberry", "Cookies n Cream", "Bubble Gum"]
toppings = ["Almonds", "Banana Slices", "Chocolate Syrup", "Caramel Syrup", "White Chocolate Chips"]

ice_cream = dict(zip(flavour, toppings))

print(ice_cream)

ice_cream["Chocolate"] = "BlueBerries"

print(ice_cream)

ice_cream.update({"Matcha": "Pistachios", "Ube": "Mango Slices"})

print(ice_cream)