# 1. Инкапсуляция
class Person:
    def __init__(self):
        self.__age = None  # приватный атрибут

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.__age = age

    def get_age(self):
        return self.__age


# 2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# 3. Полиморфизм
class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()


# 4. Абстракция
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Примеры использования

# Инкапсуляция
p = Person()
p.set_age(25)
print("Person age:", p.get_age())  # 25
# p.set_age(-5)  # вызовет ValueError

# Наследование
dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())  # Buddy Woof
print(cat.name, cat.speak())  # Kitty Meow

# Полиморфизм
car = Car()
bike = Bicycle()
print(move(car))   # Car is driving
print(move(bike))  # Bicycle is pedaling

# Абстракция
rect = Rectangle(10, 5)
circle = Circle(7)
print("Rectangle area:", rect.area())   # 50
print("Circle area:", round(circle.area(), 2))  # ~153.94
