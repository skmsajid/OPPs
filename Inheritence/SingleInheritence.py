"""
What is Inheritance?

Inheritance allows one class to reuse the properties and methods of another class.

Think of it like this:

Parent (Father)
    ↓
Child (Son)

If a father owns a house, the child inherits it. Similarly, 
if a parent class has methods and variables, the child class automatically gets access to them.

PLEASE GO THROUGH THE CHATGPT NOTES IN THIS DIRECTORY
"""
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):

    def barking(self):
        print("Dog barks...")

d = Dog()
d.eat()
d.barking()
