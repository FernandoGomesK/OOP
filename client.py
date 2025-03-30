from datetime import date, datetime

class Client:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    
fernando = Client("Fernando", "18")
print(f"my name is {fernando.name}, and i am {fernando.age} years old") 

fernando.age = "19"

print(f"my name is {fernando.name}, and i am {fernando.age} years old")