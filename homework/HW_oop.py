class Animal():
    """ We create an animal class."""
    def __init__(self, name, age, weight ):
        """initialize name age weight attributes."""
        self.name = name
        self.age = age
        self.weight = weight


    def about_animals(self):
        """use the method of the animal"""
        print(f'Hi! this animal is named {self.name} and she is {self.age} years old, by the way, it {self.weight} kg')

# animal = Animal('Mi4man', '3', '20')
# animal.about_animals()

class Turtle(Animal):
    def hide(self):
        print('Hides in case of danger')

# turtle = Turtle('Leonardo', '5', '15')
# turtle.about_animals()
# turtle.hide()

class Panther(Animal):
    def friendship(self):
        print('Bagheera is a friend of Mowgli')

# panther = Panther('Bagheera', '10', '60')
# panther.about_animals()
# panther.friendship()

class Bear(Animal):
    def teacher(self):
        print('Ballu is teacher Mowgli')

# bear = Bear('Ballu', '30', '180')
# bear.about_animals()
# bear.teacher()

class Tiger(Animal):
    def enemy(self):
        print('Sherkhan is Mowgli enemy')

# tiger = Tiger('Sherkhan', '45', '120')
# tiger.about_animals()
# tiger.enemy()

class Snake(Animal):
    def neutral(self):
        print('The Kaa is neutral to Mowgli')

# snake = Snake('Kaa', '100', '120')
# snake.about_animals()
# snake.neutral()

