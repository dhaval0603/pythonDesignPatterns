'''
Factory Pattern

Deliver a Car Specified by the user

Abstract Classes : Car
Concrete Classes : MercedesCar, AudiCar, PorscheCar, CarFactory
CarFactory will provide the Car object depending on the type of car requested
'''

from abc import abstractmethod
import abc

class Car:
    __metaclass__ = abc.ABCMeta
    @abstractmethod
    def getCarName(self):pass

class MercedesCar(Car):
    def getCarName(self):
        return "Mercedes S750"

class AudiCar(Car):
    def getCarName(self):
        return "Audi R8"

class PorscheCar(Car):
    def getCarName(self):
        return "Porsche Cayenne"

class CarFactory:
    def getCar(self, name):
        if name == "Mercedes":
            return MercedesCar()
        elif name == "Audi":
            return AudiCar()
        elif name == "Porsche":
            return PorscheCar()
        else:
            print "No Such Car"

def Main():
     carFactory = CarFactory()
     
     car = carFactory.getCar(raw_input("Input Car : Mercedes, Audi, Porsche\n"))
    
     print "Brand New " + car.getCarName()

if __name__ == '__main__':
    Main()
    
    
    
'''
Input Car : Mercedes, Audi, Porsche
Porsche
Brand New Porsche Cayenne
'''
