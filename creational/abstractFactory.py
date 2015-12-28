'''
Abstract Factory Pattern

Deliver a Car Specified by the user in his Color choice

Abstract Classes : Car, Color, AbstractFactory
Concrete Classes : MercedesCar, AudiCar, PorscheCar, RedColor, BlueColor, GreenColor, CarFactory, ColorFactory
FactoryProvider provides an appropriate factory.
CarFactory will provide the Car object depending on the type of car requested
CarFactory will provide the Color object depending on the color requested
'''
import abc
from abc import abstractmethod


class Car:
    __metaclass__ = abc.ABCMeta
    @abstractmethod
    def carName(self):
        pass
    
class MercedesCar(Car):
    def carName(self):
        return "Mercedes S750"

class AudiCar(Car):
    def carName(self):
        return "Audi R8"

class PorscheCar(Car):
    def carName(self):
        return "Porsche Cayenne"

class Color:
    __metaclass__ = abc.ABCMeta
    @abstractmethod
    def getColor(self):
        pass
    
class RedColor(Color):
    def getColor(self):
        return "Royal Red"

class BlueColor(Color):
    def getColor(self):
        return "Cool Blue"

class GreenColor(Color):
    def getColor(self):
        return "Earth Green"

class AbstractFactory():
    __metaclass__ = abc.ABCMeta
    @abstractmethod
    def getCar(self,name):pass
    
    @abstractmethod
    def getColor(self,color):pass

class CarFactory(AbstractFactory):
    def getCar(self,name):
        if name=="Mercedes":
            return MercedesCar()
        elif name=="Audi":
            return AudiCar()
        elif name=="Porsche":
            return PorscheCar()
        else:
            print "Car Not Available"
    
    def getColor(self,color):
        return null

class ColorFactory(AbstractFactory):
    def getColor(self,color):
        if color=="Red":
            return RedColor()
        elif color=="Blue":
            return BlueColor()
        elif color=="Green":
            return GreenColor()
        else:
            print "Color Not Available"
    
    def getCar(self,name):
        return null

class FactoryProvider:
    def getFactory(self,factory):
        if factory=="Car":
            return CarFactory()
        elif factory=="Color":
            return ColorFactory()
        else:
            print "No Such Factory Available"
    
def Main():
     carFactory = FactoryProvider()
     carFactory = carFactory.getFactory("Car")
     
     colorFactory = FactoryProvider()
     colorFactory = colorFactory.getFactory("Color")
     
     car = carFactory.getCar(raw_input("Input Car : Mercedes, Audi, Porsche"))
     color = colorFactory.getColor(raw_input("Input Color : Red, Blue, Green"))
    
     print "Brand New " +  car.carName() + " in " + color.getColor() + " color!"

if __name__ == '__main__':
    Main()