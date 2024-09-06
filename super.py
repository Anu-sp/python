class Vehical:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start_engine(self):
        print("vehical is started")

class Car(Vehical):
    def __init__(self, make, model, year,number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors=number_of_doors

    def start_engine(self):
        super().start_engine()
        print("The car's engine is purring smoothly.")

class Truck(Vehical):
    def __init__(self, make, model, year,cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity=cargo_capacity

    def start_engine(self):
        super().start_engine()
        print( "The truck's engine roars to life.")

car1 = Car(make="Toyota", model="Camry", year=2022, number_of_doors=4)
car1.start_engine()
truck1 = Truck(make="Ford", model="F-150", year=2021, cargo_capacity=5)
truck1.start_engine()

