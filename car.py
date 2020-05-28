# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
    
    
class ElectricCar(Car):
     
    def __init__(self):
        self.__numberFuelCells = 1
         
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, value):
        self.__numberFuelCells
        
class PetrolCar(Car):
   
    def __init__(self):
        self.__choke = 0
    
    def __getChoke(self):
        return self.__choke
    
    def __setChoke(self, value):
        self.__choke = value
        
class DieselCar(Car):
   
    def __init__(self):
        self.__dpf = 0
    
    def __getDpf(self):
        return self.__dpf
    
    def __setDpf(self, value):
        self.__dpf = value
        
        
class HybridCar(Car):
   
    def __init__(self):
        self.__regeneration = 0
    
    def __getRegeneration(self):
        return self.__regeneration
    
    def __setRegeneration(self, value):
        self.__regeneration = value
        
