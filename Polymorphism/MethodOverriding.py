# Method Overriding (Dynamic Binding / Runtime Polymorphism)
# Means when a child class redefines a method already present in its parent class 
# with the same name, same parameters, and same return type.
#  The method execution is chosen at runtime based on the object created.
class Parent:
    def show(self):
        print("Parent Show")

class Child(Parent):
    # Redefining parent's method
    def show(self):
        # super().show()  #if incase You want parent show also to be run
        print("Child Show")

c = Child()
c.show()  # Prints "Child Show"
