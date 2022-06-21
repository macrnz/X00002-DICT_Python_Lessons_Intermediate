import os
clear = lambda: os.system("clear")

clear()

class clubmembers:

    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def output_1(self):
        print("Name: " + self.name)
        print("Birthday: " + self.birthday)
        print("Age: " + self.age)
        print("Favourite Food: " + self.favorite_food)
        print("Goal: " + self.goal)

class officer(clubmembers):

    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        clubmembers.__init__(self, name, birthday, age, favorite_food, goal)

    def output_2(self):
        print("Name: " + self.name)
        print("Birthday: " + self.birthday)
        print("Age: " + self.age)
        print("Favourite Food: " + self.favorite_food)
        print("Goal: " + self.goal)
        print("Position: " + self.position)

m_1 = clubmembers("Tom", "January 16", "14", "Ice Cream", "To be happy")
o_4 = officer("Vera", "June 22", "16", "Beef Stroganoff", "To be the World's Greatest Chef", "Treasurer")

m_1.output_1()
o_4.output_2()