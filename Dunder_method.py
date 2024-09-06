class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

person = Person("Alice", 30)
print(person)



class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = point(1, 2)
p2 = point(3, 4)
p3 = p1 + p2  
print(p3)