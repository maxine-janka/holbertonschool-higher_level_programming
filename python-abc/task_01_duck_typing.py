from abc import ABC, abstractmethod
import math

pi = math.pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius * self.__radius

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)


def shape_info(shape_object):
    print("Area: {}".format(shape_object.area()))
    print("Perimeter: {}".format(shape_object.perimeter()))
