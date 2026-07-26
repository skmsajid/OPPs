"""CONSTRUCTOR, SELF
AND
COMPARING OBJECTS
IN
PYTHON"""
"""
class Computer :
    pass
obj= Computer ( ) 
print(id(obj)) #every object is having some space which stored in speacil memory called Heap Memory
#id() returns address of that memory
"""
class Computer:

    def __init__(self):
        self.name="rave"
        self.age=20

    def update(self):
        self.age=21
    
    def compare(self,obj2):
        return self.age==obj2.age
obj1=Computer()
obj1.age=21
obj2=Computer()

print(obj1.age)
print(obj2.age)
obj2.update()
print(obj2.age)

if  obj1.compare(obj2):
    print("they are same")
else:
    print("they are different")

""" self is a pointer that points to the object"""
# we cant compare two objects
#so 
