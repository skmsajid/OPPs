#Inner class
""" we can create of object of inner class (2 ways)  1.in outerclass itself  2.outside the outerclass
the best practical way is 2nd way create outside"""

"""
#1.in outerclass itself
class Student:

    def __init__(self,name,roll,brand,cpu,ram):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop(brand,cpu,ram)
    
    def show(self):
        print(f"Name:{self.name} and Roll:{self.roll}")
    
    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def info(self):
            print(f"Brand: {self.brand} CPU: {self.cpu} RAM: {self.ram}")
        
s1=Student("sajid",44,"HP","i7",12)
s2=Student("Naveen",67,"Lenovo","i9",15)

s1.show()
s1.lap.ram=0
s1.lap.info() 
s2.lap.info()
"""
#2.outside class
class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    
    def show(self):
        print(f"Name:{self.name} and Roll:{self.roll}")
    
    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def info(self):
            print(f"Brand: {self.brand} CPU: {self.cpu} RAM: {self.ram}")
        
s1=Student("sajid",44)
s2=Student("Naveen",67)

s1.show()
lap1=s1.Laptop("HP","i7",12)
lap1.info()

