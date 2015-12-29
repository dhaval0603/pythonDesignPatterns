'''
Builder Pattern

Build a Pizza

Items
Size of the Pizza - Mandatory
Cheese, Chicken, Bacon - Optional

Build a Pizza and Display the contents
'''
import abc
from abc import abstractmethod

class Pizza:
    size = None
    cheese = None
    chicken = None
    bacon = None
    
    class Builder:
        size = None
        cheese = None
        chicken = None
        bacon = None
        
        def __init__(self, size):
            self.size = size
        def cheese(self, boolean):
            self.cheese = boolean
            return self    
        def chicken(self, boolean):
            self.chicken = boolean
            return self
        def bacon(self, boolean):
            self.bacon = boolean
            return self                    
        def build(self):
            return Pizza(self)

    def __init__(self, builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.chicken = builder.chicken
        self.bacon = builder.bacon
    
    def printPizza(self):
        print "Size - ", self.size
        if self.cheese == True:
            print "Cheese"
        if self.chicken == True:
            print "Chicken"
        if self.bacon == True:
            print "Bacon"
    
def Main():
    print " Make your own Pizza "
    size = raw_input("Size of the Crust - 10/12/14 \n")
    hasCheese = True if raw_input("Cheese? Y/N \n") == "Y" else False
    hasChicken = True if raw_input("Chicken? Y/N \n") == "Y" else False 
    hasBacon = True if raw_input("Bacon? Y/N \n") == "Y" else False
    
    pizza = Pizza(Pizza.Builder(size).cheese(hasCheese).chicken(hasChicken).bacon(hasBacon))
    pizza.printPizza()
    
if __name__ == '__main__':
    Main()



'''
 Make your own Pizza 
Size of the Crust - 10/12/14 
14
Cheese? Y/N 
Y
Chicken? Y/N 
N
Bacon? Y/N 
Y
Size -  14
Cheese
Bacon
'''
