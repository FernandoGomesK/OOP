class Rental:
    def __init__(self):
        pass
    
class Workers:
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
        
class Clients:
    def __init__(self, name, cpf, age):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        
class Vehicles:
    def __init__(self, brand, plate, model, year, base_price, mileage_price):
        self.__brand = brand
        self.__plate = plate
        self.__model = model
        self.__year = year
        self.__base_price = base_price
        self.__mileage_price = mileage_price
        
class Location:
    def __init__(self):
        self.__time
        self.__price
        self.__client
        self.__client
        self.__status
        
supra1 = Vehicles("Toyota", "br1", "Supra Mk4", "1995", 20, 5 )
