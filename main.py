class Village():
    population = 0 
    buildings = 0
    
    def __init__(self, name):
        self.name =  name
        

    def get_info(self):
        print(f"Welcome in {self.name} \n"
              +f"Population of the city is {Village.population} \n"
              +f"In the city are {Village.buildings} buildings")
        
    
    @classmethod
    def add_builidng(cls):
        cls.buildings += 1
        
class District():    
    def __init__(self, location):
        self.location = location
    
class Building(District):
    def __init__(self, name, location):
        self.name = name
        super().__init__(location)
        Village.add_builidng()
        
    def get_info(self):
        print(f"The location of {self.name} is {self.location}")
        
    
        
class Residents():
    def __init__(self, name, age):
        self.name = name
        self.age - age
        
class Elf(Residents):
    def __init__(self, name, age):
        super().__init__(name, age)
        

class Items():
    pass


Village = Village("Novigrad")
Village.get_info()

Bank = Building("Bank","Nowe miasto")
Bank.get_info()







