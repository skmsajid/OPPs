"""
In Python, a constructor is a special method automatically called when a new object of a class is created. 
Its main purpose is to initialize the object's attributes 
and set up its initial state.
While the __init__() method is universally referred to as the constructor in Python,
"""
class Computer:
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is having ", self.cpu ,self.ram)


obj1=Computer("i5",10)
obj2=Computer("3 generation",13)

obj1.config()
obj2.config()