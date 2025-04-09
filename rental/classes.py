import json
from datetime import datetime

class Rental:
    def __init__(self, name):
        self.__name = name
        self.__branches = []
        
    ###########getters and setters##############
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    ############Methods################################
    def add_branch(self, branch):
        self.__branches.append(branch)
        
    def list_branches(self):
        for branch in self.__branches:
            print(branch.show_branches())
    
class Worker:
    def __init__(self, name, cpf, age, function):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        self.__function = function
    ###########getters and setters##############
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
    @property
    def function(self):
        return self.__function
    
    @function.setter
    def function(self, function):
        self.__function = function
    ############Methods################################
    
class Branch:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__clients = []
        self.__vehicles = []
        self.__workers = []
        
    def show_branches(self):
        return f"{self.__name}, {self.__location}"
        
    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)
        
    def add_client(self, client):
        self.__clients.append(client)
        
    def list_clients(self):
        for client in self.__clients:
            print(client.client_info())
        
    def list_vehicles(self):
        for vehicle in self.__vehicles:
            print(vehicle.vehicle_info())
        
class Client:   
    def __init__(self, name, cpf, age):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        
    def client_info(self):
        return f"{self.__name}, {self.__cpf}, {self.__age}"
        
    
        
class Vehicle:
    def __init__(self, brand, plate, model, year, base_price, mileage_price):
        self.__brand = brand
        self.__plate = plate
        self.__model = model
        self.__year = year
        self.__base_price = base_price
        self.__mileage_price = mileage_price
        
    def vehicle_info(self):
        return f"{self.__brand} {self.__model} ({self.__year}) plate: {self.__plate}"
    
class Car(Vehicle):
    def __init__(self, brand, plate, model, year, base_price, mileage_price):   
        super().__init__(brand, plate, model, year, base_price, mileage_price)
        
        
class Motorcycle(Vehicle):
    def __init__(self, brand, plate, model, year, base_price, mileage_price, cubic_capacity):
        self.__cubic_capacity = cubic_capacity
        super().__init__(brand, plate, model, year, base_price, mileage_price)

class Location:
    def __init__(self, client, vehicle, start_date, end_date):
        self.__client = client
        self.__vehicle = vehicle  
        self.__start_date = datetime.strptime(start_date, '%d-%m-%Y')
        self.__end_date = datetime.strptime(end_date, "%d-%m-%Y")
        self.__total_days = (self.__end_date - self.__start_date). days + 1 
        self.__price = self.price_calculation()
        
        
        
    def price_calculation(self):
        base = self.__vehicle._Vehicle__base_price
        daily_increment = self.__vehicle._Vehicle__mileage_price
        n = self.__total_days
        return n * base + daily_increment * ((n - 1) * n // 2)  
     
    
    def print_return(self):
        print(self.__client.client_info())
        print(self.__price)
        print(self.__start_date)
        print(self.__end_date)
        
        
class WaitList:
    def __init__(self):
        self.__
        

supercars = Rental("Supercars")


branch1 = Branch("Filial Central", "Rua das Alamedas, 123")

supercars.add_branch(branch1)

supercars.list_branches()

jonas = Client("jonas", 123, 25)
leo = Client("leonardo", 432, 22)
creo = Client("cero", 333, 23)

branch1.add_client(jonas)

branch1.list_clients()

supra1 = Car("Toyota", "br1", "Supra Mk4", 1995, 20, 20)
celta1 = Car("Chevrolet", "br2", "Celta", 2011, 10, 15)
altima = Car("Nissan", "Br3", "Altima", 2025, 30, 25)
ninja = Motorcycle("Kawasaki", "jp1", "ninja", 2011, 20, 10, 250)
branch1.add_vehicle(celta1)
branch1.add_vehicle(supra1)
branch1.add_vehicle(altima)
branch1.add_vehicle(ninja)

branch1.list_vehicles() 



rental1 = Location(jonas, supra1, "20-05-2025", "21-05-2025")
rental2 = Location(leo, altima, "20-05-2025", "21-05-2025")
rental3 = Location(creo, celta1, "20-05-2025", "21-05-2025")

rental1.print_return()
print("///////////////////////////////")
rental2.print_return()
print("///////////////////////////////")
rental3.print_return()

