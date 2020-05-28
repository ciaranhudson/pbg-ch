import csv
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar



class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    def create_current_stock(self):
        for i in range(6):
           self.electric_cars.append(ElectricCar())
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(10):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())
        
        

    def stock_count(self):
        print('petrol cars in stock ' + str(len(self.petrol_cars)))
        print('electric cars in stock ' + str(len(self.electric_cars)))
        print('diesel cars in stock ' + str(len(self.diesel_cars)))
        print('hybrid cars in stock ' + str(len(self.hybrid_cars)))
        
    def stock_count_write(self):
        file = open("cars.csv","w")
     
        file.write('petrol cars in stock ' + str(len(self.petrol_cars))) 
        file.write("\n")
        file.write('electric cars in stock ' + str(len(self.electric_cars)))
        file.write("\n")
        file.write('diesel cars in stock ' + str(len(self.diesel_cars))),
        file.write("\n")
        file.write('hybrid cars in stock ' + str(len(self.hybrid_cars))),
        file.close()

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print('Not enough cars in stock')
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
          
           

    def process_rental(self):
        answer = input('would you like to rent a car? y/n')
        if answer == 'y':
            self.stock_count()
            answer = input('what type would you like? p/e/d/h')
            amount = int(input('how many would you like?'))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            if answer == 'd':
                self.rent(self.diesel_cars, amount)
            if answer == 'h':
                self.rent(self.hybrid_cars, amount)
            else:
                self.rent(self.electric_cars, amount)
        self.stock_count()
        

        

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = input('continue? y/n')
dealership.stock_count_write()
    
   


    
    
    
    

