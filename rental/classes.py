class Rental:
    def __init__(self):
        pass
    
class Worker:
    def __init__(self, name, cpf, age, function):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        self.__function = function
    
class Branch:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__clients = []
        self.__vehicles = []
        self.__workers = []
        
    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)
        
    def list_vehicles(self):
        for vehicle in self.__vehicles:
            print(vehicle.car_info())
        
class Client:
    def __init__(self, name, cpf, age):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        
class Vehicle:
    def __init__(self, brand, plate, model, year, base_price, mileage_price):
        self.__brand = brand
        self.__plate = plate
        self.__model = model
        self.__year = year
        self.__base_price = base_price
        self.__mileage_price = mileage_price
        
    def car_info(self):
        return f"{self.__brand} {self.__model} ({self.__year}) plate: {self.__plate}"

class Location:
    def __init__(self, time, price, client, status):
        self.__time
        self.__price
        self.__client
        self.__status
        
class WaitList:
    def __init__(self):
        self.__
        

branch1 = Branch("Filial Central", "Rua das Alamedas, 123")


supra1 = Vehicle("Toyota", "br1", "Supra Mk4", 1995, 20, 5)
celta1 = Vehicle("Chevrolet", "br2", "Celta", 2011, 20, 2)
branch1.add_vehicle(celta1)
branch1.add_vehicle(supra1)

branch1.list_vehicles()