import os
clear = lambda: os.system("clear")

clear()

class customers:
    greeting = "Welcome to Coffee Place!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = customers("Nate", "Espresso", "Pastrami on Rye", 220)
c_2 = customers("Elaine", "Strawberry Frappuccino", "Tuna Wrap", 270)
c_3 = customers("Samirah", "Iced Caffe Latte", "Cinnamon Roll", 225)
c_4 = customers("Jeremy", "Caramel Macchiato", "Glazed Doughnut", 230)
c_5 = customers("Paz", "Iced Tea", "Blueberry Pancakes", 315)

print(customers.greeting)

print("\n")

print(c_2.name)
print(c_2.beverage)
print(c_2.food)

print("\n")

print(c_4.name)
print(c_4.beverage)
print(c_4.food)