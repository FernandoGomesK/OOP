from client import Client
class Bank:
    def __init__(self, name):  
        self.__name = name
        self.__accounts = ()
        self.__clients = []
        
    def add_client(self, client: Client):
        if isinstance(client, Client):
            self.__clients.append(client)
        else:
            raise ValueError("no can do")
        
    def get_clients(self):
        return [client.name for client in self.__clients]
    
    
bank = Bank("MyBank")
client1 = Client("Alice", 25)
client2 = Client("Bob", 30)

bank.add_client(client1)
bank.add_client(client2)

print("Bank Clients:", bank.get_clients())