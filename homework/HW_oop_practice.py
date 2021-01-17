from abc import ABC, abstractmethod
import random


class Human(ABC):
    """абстрактний клас людина від якого будемо наслідуватися"""

    @abstractmethod
    def about_yourself(self):
        raise NotImplementedError('summer. nothing happens. its from a board game of thrones')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('summer. nothing happens. its from a board game of thrones')

    @abstractmethod
    def to_buy_a_house(self):
        raise NotImplementedError('summer. nothing happens. its from a board game of thrones')


class Person(Human):
    """створюєм клас персона наслідуючись від класу людина"""

    def __init__(self, name, age, money, home):
        """ініціалізація атрибутів персони"""
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    def about_yourself(self):
        """створюємо метод інформація про себе"""
        print(
            f"My name {self.name}. I am {self.age} years old. I have {self.money} euros. I have my own house -\
            {self.home}")

    def make_money(self):
        """створюєм метод заробити гроші"""
        self.money += 2500
        print(f"{self.name} worked all week.  2500 euros. at the moment I have {self.money}.")

    def to_buy_a_house(self):
        """створюєм метод придбати будинок"""
        if self.home is False and self.money >= 2000:
            self.home = True
        print(f"I have a house - {self.home}")


class House(ABC):
    """створюєм будинок"""

    def __init__(self, area, cost):
        """ініціалізуємо атрибути будинку"""
        self.area = area
        self.cost = cost

    @abstractmethod
    def discount(self):
        raise NotImplementedError


class Home(House):
    """Створюєм клас дім наслідуючи клас будинок"""

    def __init__(self, area, cost, discounted):
        """застосовуємо властивості будинку"""
        super(Home, self).__init__(area, cost)
        self.cost = cost
        self.discounted = discounted

    def discount(self):
        print("\nDream house ")
        if self.cost >= 3000 and self.area >= 42:
            self.discounted = self.cost * 0.92
            print(f"your discount on this house {self.discounted}. ")
        elif self.cost >= 4000 and self.area >= 50:
            self.discounted = self.cost * 0.95
            print(f"your discount on this house {self.discounted}. ")
        else:
            print(f"no discount")


class RealtorMetaClass(type):
    """створюєм метаклас для класу сінгелтон ріелтер """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    """створюєм основний клас на базі метакласу """

    def __init__(self, name, houses, discount):
        """ініціюємо атрибути ріелтора"""
        self.name = name
        self.houses = houses
        self.discount = discount

    def about_all_the_houses(self):
        """створюємо метод який надає інформацію про будинки"""
        self.houses = [
            {"cost": 4500, "area": 42},
            {"cost": 5000, "area": 48}
        ]
        print("Now on sale: ")
        for house in self.houses:
            print(f"House with area {house['area']}  is for sale now for {house['cost']} ")

    def realtor_gives_a_discount(self):
        """створюємо метод надання знижки"""
        for house in self.houses:
            if house["area"] <= 42:
                self.discount = 300
            else:
                self.discount = 500

    @staticmethod
    def realtor_steals_money(self):
        """створюємо метод крадіжки грошей"""
        steal = random.randit(0, 9)
        if steal == 9:
            print(f"Your money has been stolen! Contact the police!")
        else:
            print(f"your money you have!")
