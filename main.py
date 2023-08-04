class Village():
    population = 0 
    buildings = 0
    districts = []
    
    def __init__(self, name):
        self.name =  name
        

    def get_info(self):
        print(f"Welcome in {self.name} \n"
              +f"Population of the city is {Village.population} \n"
              +f"In the city are {Village.buildings} buildings \n")
        
    
    @classmethod
    def add_builidng(cls):
        cls.buildings += 1
       
    @classmethod        
    def add_resident(cls):
        cls.population += 1
        
    #Dzielnice   
    def add_district(self, district):
        if not district in Village.districts:
            self.districts.append(district)
        
    def show_districts(self):
        print(f"Districts in the {self.name}: {Village.districts}")
        
    
class Building():
    registered_household_members = 0
    
    def __init__(self, name, district, max_residents):
        self.name = name
        self.district = district
        self.max_residents = max_residents
        self.residents = []
        Village.add_builidng()
        Village.add_district(district)
        
    def get_info(self):
        print(f"The {self.name} is located in {self.district}")
        
    def add_residents(self, resident):
        if len(self.residents) < self.max_residents:
            self.residents.append(resident)
            print(f"{resident.name} is added to {self.name} \n")
        else:
            print(f"There are no more places in the {self.name} \n")    
            
    def show_residents(self):
        print(f"Residents in {self.name}:")
        for resident in self.residents:
            print(resident.name)
            
class Toy_workshop(Building):
    gifts = []
    
    def __init__(self, name, district, max_residents):
        super().__init__(name, district, max_residents)
            
    def add_gift(self, gift):
        self.gifts.append(gift)
        
    def show_gifts(self):
        print(f"Gifts in {self.name}:")
        for gift in self.gifts:
            print(gift.name)
        

        
class Residents():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Village.add_resident()


class SantaClauss(Residents):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    
    def delete_from_village(self, who, where):
        if who in where.residents:
            where.residents.remove(who)
        else:
            print(f"Taka osoba nie zamieszkuje w {where}")
            
        
class Elf(Residents):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def make_gift(self, name, weight):
        name = Gift(name, weight)
        
    
         
class Gift():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

#Tworzenie miasta
Village = Village("Novigrad")

#Tworzenie budynków
Dom_swietego_mikolaja = Building("Dom Świętego Mikołaja", "Dzielnica Świątecznych Tradycji", 1)

Warsztat_zabawek = Toy_workshop("Warsztat Zabawek","Dzielnica Elfów", 10)
Swiatynia_elfa = Building("Świątynia Elfa", "Dzielnica Elfów", 2)
Dom_elfa = Building("Dom elfa", "Dzielnica Elfów", 2)

#Wyświeltanie dzielnic
Village.show_districts()

#Tworzenie osób
Swiety_mikolaj = SantaClauss("Świety Mikołaj", 99)

Maniek = Elf("Maniek", 18)
Mirek = Elf("Mirek", 20)
Coconi = Elf("Coconi", 21)
Kamil = Elf("Kamil", 40)
Polo = Elf("Polo", 45)


#Przypisywanie osób do budynków
Warsztat_zabawek.add_residents(Maniek)
Warsztat_zabawek.add_residents(Mirek)
Swiatynia_elfa.add_residents(Coconi)
Swiatynia_elfa.add_residents(Kamil)
Dom_elfa.add_residents(Polo)

#Uswanie osób z budynków
Warsztat_zabawek.show_residents()
Swiety_mikolaj.delete_from_village(Mirek, Warsztat_zabawek)
Warsztat_zabawek.show_residents()

#Informacje o wiosce
Village.get_info()

#Tworzenie prezentów
Samochod = Gift("Samochód", 2)
Klocki = Gift("Klocki", 3)


#Przechowanie prezentu w warsztacie zabawek
Warsztat_zabawek.add_gift(Samochod)
Warsztat_zabawek.show_gifts()

#Tworzenie prezentów przez elfy
Mirek.make_gift("Pluszak", 0.5)
















