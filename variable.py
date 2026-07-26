#Viables
#1. instance variables(Non-static variables): these are created inside init function,
# which are diffrent with respect to object
#2. Class variable (Static variable) / study variables:  which are outside of init function, whose values are same in all objects of that class
# Namespace:
# namespace is an area where you create and store objects/variables
# namespace is of two types: - 1.Object/Instance namespace 2. class namespace
"""The key rule to remember

When you access an attribute through an object (obj.attribute), Python follows this lookup order:

Check the object's namespace (obj.__dict__).
If not found, check the class namespace (Class.__dict__).
If still not found, continue searching parent classes (inheritance).
If nowhere found, raise AttributeError.

When you access an attribute through the class (Class.attribute), Python goes directly to the class namespace"""


class car:
    wheels=4 #Class variable (Static variable)
    def __init__(self):
        self.mil=10 #instance varibales
        self.com='BMW'
    
c1=car()
c2=car()
val=car().wheels
print(val)

c1.mil=8

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)
car.wheels=5
print(car().wheels)
print(car.wheels)
