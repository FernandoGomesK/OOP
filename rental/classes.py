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
        self.__workers = []
        
class Vehicles:
    def __init__(self):
        self.__brand
        self.__plate
        self.__model
        self.__base_price
        self.__mileage_price
        
class Location:
    def __init__(self):
        self.__time
        self.__price
        self.__client
        self.__client
        self.__status