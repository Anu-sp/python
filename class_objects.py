class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model  
        self.year = year    

    
    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

    
    def start(self):
        print(f"{self.brand} {self.model} is starting... Vroom!")

   
    def stop(self):
        print(f"{self.brand} {self.model} is stopping...")


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)


car1.display_info()  
car1.start()         
car1.stop()          
print()  

car2.display_info()  
car2.start()         
car2.stop()         


