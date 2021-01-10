from abc import ABC, abstractmethod


class Human(ABC):
    """абстрактний клас людина від якого будемо наслідуватися"""

    @abstractmethod
    def about_yourself(self):
        raise NotImplementedError('summer. nothing happens. its from a board game of thrones')

    @abstractmethod
    def Make_money(self):
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
        print(f"My name {self.name}. I am {self.age} years old. I have {self.money} euros. I dont have my own house - {self.home}")

    def Make_money(self):
        """створюєм метод заробити гроші"""
        self.money += 2500
        print(f"{self.name} worked all week. Erned 2500 euros. at the moment I have {self.money}.")

    def to_buy_a_house(self):
        """створюєм метод придбати будинок"""
        pass

class House():
    """створюєм будинок"""
    def __init__(self, area, cost):
        """ініціалізуємо атрибути будинку"""
        self.area = area
        self.cost = cost

    def discount(self):
        """створюємо метод 15 відсоткової знижки"""
        pass


class SingeltonMetaClass(type):
    """створюєм метаклас для класу сінгелтон ріелтер """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Realtor(metaclass=SingeltonMetaClass):
    """створюєм основний клас на базі метакласу """
    def __init__(self, name, houses, discount):
        """ініціюємо атрибути ріелтора"""
        self.name = name
        self.houses = houses
        self.discount = discount

    def about_all_the_Houses(self):
        """створюємо метод який надає інформацію про будинки"""
        pass

    def realtor_gives_a_discount(self):
        """створюємо метод надання знижки"""
        pass

    def realtor_steals_money(self):
        """створюємо метод крадіжки грошей"""
        pass

